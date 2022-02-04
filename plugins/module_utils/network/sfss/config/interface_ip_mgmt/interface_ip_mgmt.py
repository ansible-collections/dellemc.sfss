#
# -*- coding: utf-8 -*-
# Copyright 2021 Dell Inc. or its subsidiaries. All Rights Reserved
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
"""
The sfss_interface_ip_mgmt class
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
from ansible_collections.dellemc.sfss.plugins.module_utils.network.sfss.facts.facts import Facts
from ansible_collections.dellemc.sfss.plugins.module_utils.network.sfss.constants.urls import (
    INF_IP_MGMT_BASE_URL,
    INF_IP_MGMT_UPDATE_URL,
)
from ansible_collections.dellemc.sfss.plugins.module_utils.network.sfss.constants.tranformers import (
    zone_group_id,
)


class Interface_ip_mgmt(StfsConfigBase):
    """
    The sfss_interface_ip_mgmt class
    """

    gather_subset = [
        '!all',
        '!min',
    ]

    gather_network_resources = [
        'interface_ip_mgmt',
    ]

    def __init__(self, module):
        super(Interface_ip_mgmt, self).__init__(module)

    def __init__(self, module):
        super(Interface_ip_mgmt, self).__init__(module)
        self.resource_name = "interface_ip_mgmt"
        self.test_keys = [{'config': {'ipv4_address': '', 'ipv4_config_type': '', 'ipv4_gateway': '',
                                      'ipv4_netmask': '', 'ipv6_address': '', 'ipv6_config_type': '',
                                      'ipv6_gateway': '', 'ipv6_netmask': '', 'parent_interface': '',
                                      'vlan_id': ''}}]

    def resource_id(self, data):
        parent_interface = data.get('parent_interface')
        vlan_id = data.get('vlan_id')
        return "{parent_interface}:{vlan_id}".format(parent_interface=parent_interface,
                                                     vlan_id=vlan_id)

    def build_delete_all_requests(self, commands):
        ret_requests = []
        ret_commands = []
        if commands:
            for app_image in commands:
                if "1.0.0" in app_image.get('version'):
                    continue
                ret_requests.append(self.build_delete_request(app_image))
                ret_commands.append(app_image)

        return ret_commands, ret_requests

    def build_delete_requests(self, commands, want, have, diff):
        debug("build_delete_requests", want)
        ret_requests = []
        ret_commands = []
        if want:
            for app_image in want:
                matched_have = self.matches(app_image, have)
                if matched_have:
                    ret_requests.append(self.build_delete_request(app_image))
                    ret_commands.append(app_image)

        return ret_commands, ret_requests

    def build_create_request(self, have, data):
        url = INF_IP_MGMT_BASE_URL
        method = "POST"
        return self.build_request(url, method, data)

    def build_update_requests(self, have, matched_have, data):
        parent_interface = data.get('parent_interface')
        vlan_id = data.get('vlan_id')
        interface_name = parent_interface
        if vlan_id:
            interface_name = "{parent_interface}.{vlan_id}".format(parent_interface=parent_interface,
                                                                   vlan_id=vlan_id)

        url = INF_IP_MGMT_UPDATE_URL.format(interface_name=interface_name)
        method = "PUT"
        return self.build_request(url, method, data)

    def build_request(self, url, method, data):
        ipv4_address = data.get('ipv4_address')
        ipv4_config_type = data.get('ipv4_config_type').upper()
        ipv4_gateway = data.get('ipv4_gateway')
        ipv4_netmask = data.get('ipv4_netmask')

        ipv6_address = data.get('ipv6_address')
        ipv6_config_type = data.get('ipv6_config_type').upper()
        ipv6_gateway = data.get('ipv6_gateway')
        ipv6_netmask = data.get('ipv6_netmask')

        parent_interface = data.get('parent_interface')
        vlan_id = data.get('vlan_id')

        payload = {"IPV6Config": ipv6_config_type,
                   "IPV4Config": ipv4_config_type}

        if vlan_id:
            payload.update({"ParentInterface": parent_interface,
                            "VlanId": vlan_id})

        if ipv4_config_type in "MANUAL":
            payload.update({
                "IPV4Address": [ipv4_address],
                "IPV4Gateway": ipv4_gateway,
                "IPV4PrefixLength": ipv4_netmask
            })

        if ipv6_config_type in "MANUAL":
            payload.update({"IPV6Address": [ipv6_address],
                            "IPV6Gateway": ipv6_gateway,
                            "IPV6PrefixLength": ipv6_netmask})

        request = {"method": method,
                   "path": url,
                   "data": payload}
        debug("IP Interface request", request)
        return [request]

    def build_delete_request(self, data):
        parent_interface = data.get('parent_interface')
        vlan_id = data.get('vlan_id')
        interface_name = parent_interface
        if vlan_id:
            interface_name = "{parent_interface}.{vlan_id}".format(parent_interface=parent_interface,
                                                                   vlan_id=vlan_id)

        url = INF_IP_MGMT_UPDATE_URL.format(interface_name=interface_name)
        method = "DELETE"

        request = {"method": method,
                   "path": url}
        debug("Zone_group_ delete request", request)
        return request
