#
# -*- coding: utf-8 -*-
# Copyright 2021 Dell Inc. or its subsidiaries. All Rights Reserved
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
"""
The sfss endpoints fact class
It is in this file the configuration is collected from the device
for a given resource, parsed, and the facts tree is populated
based on the configuration.
"""
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type
from ansible_collections.dellemc.sfss.plugins.module_utils.network.sfss.utils.debug import debug
from ansible_collections.dellemc.sfss.plugins.module_utils.network.sfss.argspec.endpoints.endpoints import EndpointsArgs
from ansible_collections.dellemc.sfss.plugins.module_utils.network.sfss.facts.base.sfss_facts_base import (
    StfsFactsBase,
)
from ansible_collections.dellemc.sfss.plugins.module_utils.network.sfss.constants.urls import (
    EP_EXPNAD_URL
)
from ansible_collections.dellemc.sfss.plugins.module_utils.network.sfss.utils.utils import (
    send_requests,
    get_instances,
)
from ansible.module_utils.connection import ConnectionError

GET = "get"


class EndpointsFacts(StfsFactsBase):
    """ The sfss endpoints fact class
    """
    def __init__(self, module):
        self.argument_spec = EndpointsArgs.argument_spec
        self.resource_name = "endpoints"
        super(EndpointsFacts, self).__init__(module)

    def get_resource_data(self, instance_id):
        """Get all the endpoints available in instance"""
        requests = [{"path": EP_EXPNAD_URL.format(instance_id=instance_id, endpoint_type_str="Hosts"),
                     "method": GET},
                    {"path": EP_EXPNAD_URL.format(instance_id=instance_id, endpoint_type_str="Subsystems"),
                     "method": GET},
                    {"path": EP_EXPNAD_URL.format(instance_id=instance_id, endpoint_type_str="DDCs"),
                     "method": GET}]
        responses = send_requests(self, requests)

        endpoints = []
        for response in responses:
            if response and response[1].get('Hosts'):
                for host_data in response[1]['Hosts']:
                    endpoints.append(self.transform_config("host", instance_id, host_data))
            if response and response[1].get('Subsystems'):
                for host_data in response[1]['Subsystems']:
                    endpoints.append(self.transform_config("subsystem", instance_id, host_data))
            if response and response[1].get('DDCs'):
                for host_data in response[1]['DDCs']:
                    endpoints.append(self.transform_config("ddc", instance_id, host_data))

        return endpoints

    def transform_config(self, endpoint_type, instance_id, data):
        debug("instance id", instance_id)
        debug("endpoint_type", endpoint_type)
        debug("transform_config", data)
        if endpoint_type == 'host':
            endpoint = {
                "type": endpoint_type,
                "transport_type": data["TransportType"].lower(),
                "instance_id": instance_id,
                "transport_address": data.get("TransportAddress"),
                "transport_address_family": data.get("TransportAddressFamily").lower(),
                "nqn_id": data.get("NQN"),
            }
        else:
            endpoint = {
                "port_id": data["PortId"],
                "type": endpoint_type,
                "transport_type": data["TransportType"].lower(),
                "instance_id": instance_id,
                "transport_address": data.get("TransportAddress"),
                "transport_address_family": data.get("TransportAddressFamily").lower(),
                "nqn_id": data.get("NQN"),
            }

        if "ddc" in endpoint_type:
            endpoint.update({
                "ddc_activate": data.get("Activate")
            })

        if "subsystem" in endpoint_type:
            endpoint.update({
                "transport_service_id": data.get("TransportServiceId"),
            })
        return endpoint
