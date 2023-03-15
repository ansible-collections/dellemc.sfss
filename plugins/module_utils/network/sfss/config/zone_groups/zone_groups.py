#
# -*- coding: utf-8 -*-
# Copyright 2021 Dell Inc. or its subsidiaries. All Rights Reserved
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
"""
The sfss_zone_groups class
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
    ZONE_GRP_CREATE_URL,
    ZONE_GRP_UPDATE_URL,
)
from ansible_collections.dellemc.sfss.plugins.module_utils.network.sfss.constants.tranformers import (
    transform_zone_group_active_state,
    zone_group_id,
    get_orginate_nqn_by_instance,
)
from ansible_collections.dellemc.sfss.plugins.module_utils.network.sfss.utils.utils import (
    get_orginate_nqns,
)


class Zone_groups(StfsConfigBase):
    """
    The sfss_zone_groups class
    """

    gather_subset = [
        '!all',
        '!min',
    ]

    gather_network_resources = [
        'zone_groups',
    ]

    def __init__(self, module):
        super(Zone_groups, self).__init__(module)
        self.resource_name = "zone_groups"
        self.test_keys = [{'config': {'instance_id': '', 'name': '', 'activate_status': '', 'activation_state': ''}}]

    def get_orginate_nqns_data(self):
        return get_orginate_nqns(self)

    def build_create_request(self, have, want):
        debug("into create request")
        instance_id = want.get("instance_id")
        zone_group_name = want.get('name')
        activate_status = want.get('activate_status')
        activate_status = transform_zone_group_active_state(activate_status)
        requests = []
        requests.append(self.build_create_zone_group_req(instance_id, zone_group_name, activate_status))
        if activate_status == 'Activate':
            requests.append(self.build_activate_status_req(instance_id, zone_group_name, True))
        return requests

    def build_update_requests(self, have, matched_have, want):
        debug("into update request")
        instance_id = want.get("instance_id")
        zone_group_name = want.get('name')
        want_activate_status = want.get('activate_status')
        have_activate_status = matched_have.get('activate_status')
        requests = []
        if want_activate_status != have_activate_status:
            requests.append(self.build_activate_status_req(instance_id, zone_group_name, want_activate_status))
        if matched_have.get('activation_state') == 'ReActivationNeeded' and want_activate_status:
            requests.append(self.build_activate_status_req(instance_id, zone_group_name, want_activate_status))

        return requests

    def build_delete_all_requests(self, commands):
        debug("into delete all")
        requests = []
        for command in commands:
            instance_id = command.get("instance_id")
            zone_group_name = command.get('name')
            activate_status = command.get('activate_status')
            if activate_status:
                requests.append(self.build_activate_status_req(instance_id, zone_group_name, False))
            requests.append(self.build_zone_grp_delete_req(instance_id, zone_group_name))
        return commands, requests

    # Delete specific data
    def build_delete_requests(self, commands, want, have, diff):
        debug("into delete")
        ret_requests = []
        ret_commands = []
        debug("into build_delete_requests", want)
        for command in want:
            command_requests = []
            instance_id = command.get("instance_id")
            zone_group_name = command.get('name')
            matched_have = self.matches(command, have)
            if matched_have:
                activate_status = matched_have.get('activate_status')
                if activate_status:
                    command_requests.append(self.build_activate_status_req(instance_id, zone_group_name, False))
                command_requests.append(self.build_zone_grp_delete_req(instance_id, zone_group_name))

            if command_requests:
                ret_commands.append(command)
                ret_requests.extend(command_requests)

        return ret_commands, ret_requests

    def build_create_zone_group_req(self, instance_id, zone_group_name, activate_status):
        url = ZONE_GRP_CREATE_URL.format(instance_id=instance_id, config_type="config")
        method = "POST"

        payload = {
            "ZoneDBType": "config",
            "ZoneGroupName": zone_group_name,
            "ActivateStatus": activate_status
        }

        request = {
            "method": method,
            "path": url,
            "data": payload,
        }
        debug("Zone_group_request", request)
        return request

    def build_activate_status_req(self, instance_id, zone_group_name, activate_status):
        orginate_nqn_id = get_orginate_nqn_by_instance(self.orginate_nqns, instance_id)
        config_type = "config"
        if not activate_status:
            config_type = "active"
        zone_group_id_val = zone_group_id(zone_group_name, orginate_nqn_id, config_type=config_type)

        url = ZONE_GRP_UPDATE_URL.format(instance_id=instance_id, config_type=config_type,
                                         zone_group_id=zone_group_id_val)
        method = "PUT"

        activate_status_str = transform_zone_group_active_state(activate_status)

        payload = {"ActivateStatus": activate_status_str}

        request = {
            "method": method,
            "path": url,
            "data": payload,
        }
        debug("Zone_group_activation state request", request)
        return request

    def build_zone_grp_delete_req(self, instance_id, zone_group_name):
        orginate_nqn_id = get_orginate_nqn_by_instance(self.orginate_nqns, instance_id)
        zone_group_id_val = zone_group_id(zone_group_name, orginate_nqn_id)

        url = ZONE_GRP_UPDATE_URL.format(instance_id=instance_id, config_type='config',
                                         zone_group_id=zone_group_id_val)
        method = "DELETE"

        request = {
            "method": method,
            "path": url,
        }
        debug("Zone_group_activation state request", request)
        return request

    def resource_id(self, want):
        name = want["name"]
        instance_id = want["instance_id"]
        orginate_nqn_id = get_orginate_nqn_by_instance(self.orginate_nqns, instance_id)
        zone_group_id_val = zone_group_id(name, orginate_nqn_id)

        return zone_group_id_val
