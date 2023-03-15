#
# -*- coding: utf-8 -*-
# Copyright 2021 Dell Inc. or its subsidiaries. All Rights Reserved
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
"""
The sfss_zones class
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
    ZONE_CREATE_URL,
    ZONE_MEMBER_CREATE_URL,
    ZONE_MEMBER_UPDATE_URL,
    ZONE_DELETE_URL,
)
from ansible_collections.dellemc.sfss.plugins.module_utils.network.sfss.constants.tranformers import (
    zone_group_id,
    zone_id,
    zone_member_id,
    transform_zone_member_type,
    transform_end_point_type,
    get_orginate_nqn_by_instance,
)
from ansible_collections.dellemc.sfss.plugins.module_utils.network.sfss.utils.utils import (
    get_orginate_nqns,
)


class Zones(StfsConfigBase):
    """
    The sfss_zones class
    """

    gather_subset = [
        '!all',
        '!min',
    ]

    gather_network_resources = [
        'zones',
    ]

    def __init__(self, module):
        super(Zones, self).__init__(module)
        self.resource_name = "zones"
        self.test_keys = [{'config': {'name': '', 'instance_id': '', 'group_name': '', 'members': ''}}]

    def get_orginate_nqns_data(self):
        return get_orginate_nqns(self)

    def resource_id(self, want):
        eid = zone_id(want["group_name"], want["name"])
        return eid

    def build_delete_all_requests(self, commands):
        requests = []
        for command in commands:
            instance_id = command.get("instance_id")
            zone_name = command.get('name')
            zone_group_name = command.get('group_name')

            requests.append(self.build_delete_zone_req(instance_id, zone_group_name, zone_name))

        return commands, requests

    # Delete specific data
    def build_delete_requests(self, commands, want, have, diff):
        ret_requests = []
        ret_commands = []
        debug("into build_delete_requests", want)
        for command in want:
            command_requests = []
            instance_id = command.get("instance_id")
            zone_name = command.get('name')
            zone_group_name = command.get('group_name')
            want_members = command.get('members')
            matched_have = self.matches(command, have)
            if not matched_have:
                # Resource not available in have
                continue

            # if members: None. Delete zone
            if not want_members:
                command_requests.append(self.build_delete_zone_req(instance_id, zone_group_name, zone_name))
            else:  # if members. Delete zone
                debug("into delete zonemembers", command)
                want_members_data = command.get('members').get('data')
                debug("into delete matched_have", matched_have)
                have_members_data = []
                if matched_have.get('members'):
                    have_members_data = matched_have.get('members').get('data')
                # members.data is None, Delete all available zone members from have
                zone_members = want_members_data
                if not want_members_data:
                    zone_members = have_members_data
                for want_member in zone_members:
                    matched_member = self.member_match(want_member, have_members_data, zone_group_name, zone_name)
                    if matched_member:
                        command_requests.append(self.build_delete_zone_member_req(instance_id, zone_group_name,
                                                                                  zone_name, matched_member))
            if command_requests:
                ret_commands.append(command)
                ret_requests.extend(command_requests)

        return ret_commands, ret_requests

    def build_create_request(self, have, want):
        instance_id = want.get("instance_id")
        zone_name = want.get('name')
        zone_group_name = want.get('group_name')
        want_zone_members = []
        if want.get('members'):
            want_zone_members = want.get('members').get('data')
        requests = []
        # requests.append(self.build_create_zone_group_req(instance_id, zone_group_name))
        requests.append(self.build_create_zone_req(instance_id, zone_group_name, zone_name))
        requests.extend(self.build_create_zone_members_req(instance_id, zone_group_name, zone_name, want_zone_members))

        return requests

    def build_update_requests(self, have, matched_have, want):
        debug("into update request")
        instance_id = want.get("instance_id")
        zone_name = want.get('name')
        zone_group_name = want.get('group_name')
        want_zone_members = have_zone_members = []
        if want.get('members'):
            want_zone_members = want.get('members').get('data')
        if matched_have.get('members'):
            have_zone_members = matched_have.get('members').get('data')
        ret_reqs = []
        create_want_members = []
        update_want_members = []
        for want_member in want_zone_members:
            # want_member_id = want_member['id']
            want_member_id = want_member['id']
            debug("want_member_id", want_member_id)
            want_member_role = want_member.get('role', '')
            want_member_id_type = want_member['id_type']
            matched = False
            for have_member in have_zone_members:
                have_member_id = have_member['id']
                debug("have_member_id", have_member_id)
                have_member_role = have_member.get('role', '')
                have_member_id_type = have_member['id_type']
                if want_member_id == have_member_id and want_member_id_type == have_member_id_type:
                    matched = True
                    if want_member_role != have_member_role:
                        update_want_members.append(want_member)

            if not matched:
                create_want_members.append(want_member)

        if create_want_members:
            create_reqs = self.build_create_zone_members_req(instance_id, zone_group_name, zone_name, create_want_members)
            ret_reqs.extend(create_reqs)
            debug("create_reqs", create_reqs)

        if update_want_members:
            update_reqs = self.build_update_zone_members_req(instance_id, zone_group_name, zone_name, update_want_members)
            ret_reqs.extend(update_reqs)
            debug("update_reqs", update_reqs)

        debug("create_want_members", create_want_members)
        debug("update_want_members", update_want_members)
        return ret_reqs

    def build_create_zone_members_req(self, instance_id, zone_group_name, zone_name, zone_members):
        members_requests = []
        if not zone_members:
            return members_requests
        for zone_member in zone_members:
            member_req = self.build_create_zone_member_req(instance_id, zone_group_name, zone_name, zone_member)
            members_requests.append(member_req)

        return members_requests

    def build_update_zone_members_req(self, instance_id, zone_group_name, zone_name, zone_members):
        members_requests = []
        if not zone_members:
            return members_requests
        for zone_member in zone_members:
            member_req = self.build_update_zone_member_req(instance_id, zone_group_name, zone_name, zone_member)
            members_requests.append(member_req)

        return members_requests

    def member_match(self, want_member, have_members, zone_group_name, zone_name):
        ep_id = want_member['id']
        debug("want ep_id", ep_id)
        macthed_member = None
        if not have_members:
            return macthed_member
        for have_member in have_members:
            have_ep_id = have_member['id']
            debug("have_ep_id", have_ep_id)
            if ep_id == have_ep_id:
                macthed_member = have_member
                break
        # debug("matches", matches)
        return macthed_member

# Request creations start ####

    def build_create_zone_member_req(self, instance_id, zone_group_name, zone_name, zone_member):
        orginate_nqn_id = get_orginate_nqn_by_instance(self.orginate_nqns, instance_id)
        zone_group_id_val = zone_group_id(zone_group_name, orginate_nqn_id)
        zone_id_val = zone_id(zone_group_id_val, zone_name)
        url = ZONE_MEMBER_CREATE_URL.format(instance_id=instance_id, config_type="config",
                                            zone_group_id=zone_group_id_val,
                                            zone_id=zone_id_val)
        method = "POST"

        member_type = zone_member['id_type']

        payload = {"ZoneMemberId": zone_member['id'],
                   "ZoneMemberType": transform_zone_member_type(zone_member['id_type'])}

        if 'zone_alias' not in member_type:
            payload.update({"Role": transform_end_point_type(zone_member['role'])})

        request = {
            "method": method,
            "path": url,
            "data": payload,
        }
        debug("Zone member_request", request)
        return request

    def build_update_zone_member_req(self, instance_id, zone_group_name, zone_name, zone_member):
        orginate_nqn_id = get_orginate_nqn_by_instance(self.orginate_nqns, instance_id)
        zone_group_id_val = zone_group_id(zone_group_name, orginate_nqn_id)
        zone_id_val = zone_id(zone_group_id_val, zone_name)
        zone_member_id_val = zone_member_id(zone_group_name, zone_name, zone_member['id'])
        url = ZONE_MEMBER_UPDATE_URL.format(instance_id=instance_id, config_type="config",
                                            zone_group_id=zone_group_id_val,
                                            zone_id=zone_id_val,
                                            zone_member_id=zone_member_id_val)
        method = "PUT"
        payload = {"Role": transform_end_point_type(zone_member['role'])}

        request = {"method": method,
                   "path": url,
                   "data": payload}
        debug("Zone member_request", request)
        return request

    def build_create_zone_req(self, instance_id, zone_group_name, zone_name):
        orginate_nqn_id = get_orginate_nqn_by_instance(self.orginate_nqns, instance_id)
        zone_group_id_val = zone_group_id(zone_group_name, orginate_nqn_id)
        url = ZONE_CREATE_URL.format(instance_id=instance_id, config_type="config",
                                     zone_group_id=zone_group_id_val)
        method = "POST"

        payload = {
            "ZoneName": zone_name
        }

        request = {
            "method": method,
            "path": url,
            "data": payload,
        }
        debug("Zone_request", request)
        return request

    def build_create_zone_group_req(self, instance_id, zone_group_name):
        url = ZONE_GRP_CREATE_URL.format(instance_id=instance_id, config_type="config")
        method = "POST"

        payload = {
            "ZoneDBType": "config",
            "ZoneGroupName": zone_group_name
        }

        request = {
            "method": method,
            "path": url,
            "data": payload,
        }
        debug("Zone_group_request", request)
        return request

    def build_delete_zone_req(self, instance_id, zone_group_name, zone_name):
        orginate_nqn_id = get_orginate_nqn_by_instance(self.orginate_nqns, instance_id)
        zone_group_id_val = zone_group_id(zone_group_name, orginate_nqn_id)
        zone_id_val = zone_id(zone_group_id_val, zone_name)
        url = ZONE_DELETE_URL.format(instance_id=instance_id, config_type="config",
                                     zone_group_id=zone_group_id_val,
                                     zone_id=zone_id_val)
        method = "DELETE"

        request = {
            "method": method,
            "path": url,
        }
        debug("Zone delete request", request)
        return request

    def build_delete_zone_member_req(self, instance_id, zone_group_name, zone_name, zone_member):
        debug(" build_delete_zone_member_req zone_member ", zone_member)
        orginate_nqn_id = get_orginate_nqn_by_instance(self.orginate_nqns, instance_id)
        zone_group_id_val = zone_group_id(zone_group_name, orginate_nqn_id)
        zone_id_val = zone_id(zone_group_id_val, zone_name)
        zone_member_id_val = zone_member_id(zone_id_val, zone_member['id'])

        url = ZONE_MEMBER_UPDATE_URL.format(instance_id=instance_id, config_type="config",
                                            zone_group_id=zone_group_id_val,
                                            zone_id=zone_id_val,
                                            zone_member_id=zone_member_id_val)
        method = "DELETE"

        request = {
            "method": method,
            "path": url,
        }

        debug("Zone member delete request ", request)
        return request

# Request creations start ####
