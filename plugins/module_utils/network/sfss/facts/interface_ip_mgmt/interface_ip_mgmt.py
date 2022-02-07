#
# -*- coding: utf-8 -*-
# Copyright 2021 Dell Inc. or its subsidiaries. All Rights Reserved
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
"""
The sfss interface_ip_mgmt fact class
It is in this file the configuration is collected from the device
for a given resource, parsed, and the facts tree is populated
based on the configuration.
"""
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type
from ansible_collections.dellemc.sfss.plugins.module_utils.network.sfss.argspec.interface_ip_mgmt.interface_ip_mgmt import Interface_ip_mgmtArgs
from ansible_collections.dellemc.sfss.plugins.module_utils.network.sfss.utils.debug import debug
from ansible_collections.dellemc.sfss.plugins.module_utils.network.sfss.constants.urls import (
    INF_IP_MGMT_URL,
)
from ansible_collections.dellemc.sfss.plugins.module_utils.network.sfss.constants.tranformers import (
    transform_cdc_state,
)
from ansible_collections.dellemc.sfss.plugins.module_utils.network.sfss.facts.base.sfss_facts_base import (
    StfsFactsBase,
)
from ansible_collections.dellemc.sfss.plugins.module_utils.network.sfss.utils.utils import (
    send_requests,
    get_instances,
)

GET = "get"


class Interface_ip_mgmtFacts(StfsFactsBase):
    """ The sfss interface_ip_mgmt fact class
    """
    def __init__(self, module):
        self.argument_spec = Interface_ip_mgmtArgs.argument_spec
        self.resource_name = "interface_ip_mgmt"
        super(Interface_ip_mgmtFacts, self).__init__(module)

    def get_all_data(self):
        ret = self.get_resource_data()
        debug("get_all_data", ret)
        return ret

    def get_resource_data(self):
        path = INF_IP_MGMT_URL
        requests = [{"path": path, "method": GET}]
        responses = send_requests(self, requests)
        debug("Images get", responses)
        ret = []
        if responses and responses[0][1].get('IpAddressManagements'):
            for data in responses[0][1]['IpAddressManagements']:
                ret.append(self.transform_config(data))

        return ret

    def transform_config(self, data):
        inf_type = data.get('Type')
        parent_interface = data.get('ParentInterface')
        interface = data.get('Interface')
        ipv4_config_type = data.get('IPV4Config').lower()
        ipv6_config_type = data.get('IPV6Config').lower()

        vlan_id = data.get('VlanId')

        ret = {"ipv4_config_type": ipv4_config_type,
               "ipv6_config_type": ipv6_config_type}

        if inf_type == "VLAN":
            ret.update({
                "parent_interface": parent_interface,
                "vlan_id": vlan_id
            })
        else:
            ret.update({
                "parent_interface": interface
            })

        if ipv4_config_type == "manual":
            ret.update({
                "ipv4_address": data.get('IPV4Address')[0],
                "ipv4_netmask": data.get('IPV4PrefixLength'),
                "ipv4_gateway": data.get('IPV4Gateway')
            })

        if ipv6_config_type == "manual":
            ret.update({
                "ipv6_address": data.get('IPV6Address')[0],
                "ipv6_netmask": data.get('IPV6PrefixLength'),
                "ipv6_gateway": data.get('IPV6Gateway')
            })

        return ret
