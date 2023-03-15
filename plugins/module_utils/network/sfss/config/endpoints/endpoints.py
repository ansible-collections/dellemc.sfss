#
# -*- coding: utf-8 -*-
# Copyright 2021 Dell Inc. or its subsidiaries. All Rights Reserved
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
"""
The sfss_endpoints class
It is in this file where the current configuration (as dict)
is compared to the provided configuration (as dict) and the command set
necessary to bring the current configuration to it's desired end-state is
created
"""
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type
from ansible_collections.dellemc.sfss.plugins.module_utils.network.sfss.config.base.sfss_config_base import (
    StfsConfigBase,
)
from ansible_collections.dellemc.sfss.plugins.module_utils.network.sfss.utils.debug import debug
from ansible_collections.dellemc.sfss.plugins.module_utils.network.sfss.constants.urls import (
    EP_SPECIFIC_URL,
    EP_CREATE_URL,
)
from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.utils import (
    to_list,
)
from ansible_collections.dellemc.sfss.plugins.module_utils.network.sfss.constants.tranformers import (
    get_endpoint_id,
)


class Endpoints(StfsConfigBase):
    """
    The sfss_endpoints class
    """

    gather_subset = [
        '!all',
        '!min',
    ]

    gather_network_resources = [
        'endpoints',
    ]

    def __init__(self, module):
        super(Endpoints, self).__init__(module)
        self.resource_name = "endpoints"
        self.test_keys = [{'config': {'type': '', 'instance_id': '', 'nqn_id': '', 'port_id': '',
                           'transport_address': '', 'transport_address_family': '', 'transport_type': '', 'transport_service_id': ''}}]

    # Port id of DDC is defaults to 8009 in Rest API.
    # This is reason for
    def set_config(self, existing_facts):
        """ Collect the configuration from the args passed to the module,
            collect the current configuration (as a dict from facts)

        :rtype: A list
        :returns: the commands necessary to migrate the current configuration
                  to the desired configuration
        """
        org_want = self._module.params['config']
        modified_want = []
        # Port id of DDC is defaults to 8009 in Rest API.
        for endpoint in org_want:
            if 'ddc' in endpoint.get('type') and endpoint.get('port_id') == 0:
                endpoint['port_id'] = 8009
            modified_want.append(endpoint)

        have = existing_facts
        debug("set_config from config/endpoint.py: modified_want", modified_want)
        resp = self.set_state(modified_want, have)
        debug("set_config from config/endpoint.py: resp", resp)
        return to_list(resp)

    def build_delete_all_requests(self, commands):
        return self.build_delete_requests(commands, None, None, None)

    def build_delete_requests(self, commands, want, have, diff):
        requests = []
        if not commands:
            return commands, requests
        # Create URL and payload
        method = "DELETE"
        for endpoint in commands:
            instance_id = endpoint.get("instance_id", 1)
            endpoint_type = endpoint.get('type')
            endpoint_type_str = self.get_endpoint_str(endpoint_type)
            endpoint_id = self.resource_id(endpoint)
            url = EP_SPECIFIC_URL.format(instance_id=instance_id, endpoint_type_str=endpoint_type_str,
                                         endpoint_id=endpoint_id)

            request = {
                "method": method,
                "path": url,
            }
            requests.append(request)
        return commands, requests

    def get_endpoint_str(self, endpoint_type):
        ret = "Hosts"
        if endpoint_type == 'subsystem':
            ret = 'Subsystems'
        elif endpoint_type == 'ddc':
            ret = 'DDCs'

        return ret

    def resource_id(self, endpoint):
        nqn_id = ""
        port = 0
        transport_srv_id = ""
        ip = endpoint.get('transport_address')
        if endpoint.get('nqn_id'):
            nqn_id = endpoint.get('nqn_id')
        if endpoint.get('port_id'):
            port = endpoint.get('port_id')
        transport_type = endpoint.get('transport_type').upper()
        transport_addr_family = endpoint.get('transport_address_family')
        if endpoint.get('transport_service_id'):
            transport_srv_id = endpoint.get('transport_service_id')

        ret = get_endpoint_id(nqn_id=nqn_id, ip=ip, ip_type=transport_addr_family, transport_service_id=transport_srv_id,
                              port_id=port, transport_type=transport_type)

        return ret

    def build_update_requests(self, have, matched_have, command):
        endpoint = command
        instance_id = endpoint.get("instance_id", 1)
        endpoint_type = endpoint.get('type')
        endpoint_type_str = self.get_endpoint_str(endpoint_type)
        endpoint_id = self.resource_id(endpoint)
        url = EP_SPECIFIC_URL.format(instance_id=instance_id, endpoint_type_str=endpoint_type_str,
                                     endpoint_id=endpoint_id)

        payload = {
            "TransportServiceId": endpoint.get('transport_service_id')
        }
        if "ddc" in endpoint_type:
            payload = {
                "Activate": endpoint.get('ddc_activate')
            }

        request = {
            "method": "PUT",
            "path": url,
            "data": payload,
        }
        return [request]

    def build_create_request(self, have, endpoint):
        instance_id = endpoint.get("instance_id", 1)
        endpoint_type = endpoint.get('type')
        endpoint_type_str = self.get_endpoint_str(endpoint_type)
        url = EP_CREATE_URL.format(instance_id=instance_id, endpoint_type_str=endpoint_type_str)
        method = "POST"

        endpoint_payload = {}
        if endpoint_type != 'host':
            if endpoint.get('port_id'):  # Optional
                endpoint_payload.update({"PortId": endpoint.get('port_id')})
        if endpoint.get('transport_type'):  # Mandatory
            endpoint_payload.update({"TransportType": endpoint.get('transport_type').upper()})

        endpoint_payload.update({"TransportAddress": endpoint.get('transport_address'),
                                 "TransportAddressFamily": endpoint.get('transport_address_family').upper()})
        if endpoint.get('nqn_id'):  # Optional
            endpoint_payload.update({"NQN": endpoint.get('nqn_id')})

        if "subsystem" in endpoint_type:  # Optional
            if endpoint.get('transport_service_id'):
                endpoint_payload.update({"TransportServiceId": endpoint.get('transport_service_id')})

        if "ddc" in endpoint_type:  # Mandatory
            if endpoint.get('nqn_id'):
                self._module.fail_json(msg="NQN not applicable for DDC, Please remove from the input",
                                       input=endpoint)
            if endpoint.get('ddc_activate') is not None:
                endpoint_payload.update({"Activate": endpoint.get('ddc_activate')})

        request = {
            "method": method,
            "path": url,
            "data": endpoint_payload,
        }
        debug("endpoint", request)
        return [request]
