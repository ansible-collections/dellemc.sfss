#
# -*- coding: utf-8 -*-
# Copyright 2021 Dell Inc. or its subsidiaries. All Rights Reserved
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
"""
The sfss_cdc_instances class
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
from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.utils import (
    to_list,
)
from ansible_collections.dellemc.sfss.plugins.module_utils.network.sfss.facts.facts import Facts
from ansible_collections.dellemc.sfss.plugins.module_utils.network.sfss.constants.tranformers import (
    retransform_cdc_state
)
from ansible_collections.dellemc.sfss.plugins.module_utils.network.sfss.constants.urls import (
    CDC_SPECIFIC_INSTANCE_URL,
    CDC_BASE_URL,
)


class Cdc_instances(StfsConfigBase):
    """
    The sfss_cdc_instances class
    """

    gather_subset = [
        '!all',
        '!min',
    ]

    gather_network_resources = [
        'cdc_instances',
    ]

    def __init__(self, module):
        super(Cdc_instances, self).__init__(module)
        self.resource_name = "cdc_instances"
        self.test_keys = [{'config': {'instance_id': '', 'interfaces': '', 'admin_state': '',
                           'discovery_svc_admin_state': ''}}]

    def get_interfaces_str(self, cdc_instance):
        ret = []
        user_interfaces = cdc_instance["interfaces"]
        for user_interface in user_interfaces:
            ret.append(user_interface['name'])
        return ret

    def build_delete_all_requests(self, commands):
        debug("build_delete_all_requests", commands)
        ret_requests = []
        ret_commands = []
        if commands:
            for cdc_instance in commands:
                ret_requests.append(self.build_delete_request(cdc_instance))
                ret_commands.append(cdc_instance)

        return ret_commands, ret_requests

    def build_delete_requests(self, commands, want, have, diff):
        debug("build_delete_requests", want)
        ret_requests = []
        ret_commands = []
        if want:
            for cdc_instance in want:
                matched_have = self.matches(cdc_instance, have)
                if matched_have:
                    ret_requests.append(self.build_delete_request(cdc_instance))
                    ret_commands.append(cdc_instance)

        return ret_commands, ret_requests

    def build_create_request(self, have, cdc_instance):
        url = CDC_BASE_URL
        method = "POST"
        instance_id = cdc_instance["instance_id"]
        payload = {
            "InstanceIdentifier": str(instance_id),
            "Interfaces": self.get_interfaces_str(cdc_instance),
            "CDCAdminState": retransform_cdc_state(cdc_instance["admin_state"]),
            "Version": "1.0.0",
            "DiscoverySvcAdminState": retransform_cdc_state(cdc_instance["discovery_svc_admin_state"]),
        }

        request = {
            "method": method,
            "path": url,
            "data": payload,
        }
        debug("Zone_group_request", request)
        return [request]

    def build_update_requests(self, have, matched_have, cdc_instance):
        debug("build_update_requests", cdc_instance)
        instance_id = cdc_instance["instance_id"]
        url = CDC_SPECIFIC_INSTANCE_URL.format(instance_id=instance_id)
        method = "PUT"

        payload = {
            "InstanceIdentifier": str(instance_id),
            "Interfaces": self.get_interfaces_str(cdc_instance),
            "CDCAdminState": retransform_cdc_state(cdc_instance["admin_state"]),
            "Version": "1.0.0",
            "DiscoverySvcAdminState": retransform_cdc_state(cdc_instance["discovery_svc_admin_state"]),
        }

        request = {
            "method": method,
            "path": url,
            "data": payload,
        }
        debug("Zone_group_request", request)
        return [request]

    def build_delete_request(self, cdc_instance):
        instance_id = cdc_instance["instance_id"]
        url = CDC_SPECIFIC_INSTANCE_URL.format(instance_id=instance_id)
        method = "DELETE"

        request = {
            "method": method,
            "path": url,
        }
        debug("Zone_group_ delete request", request)
        return request

    def resource_id(self, cdc_instance):
        return cdc_instance["instance_id"]
