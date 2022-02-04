#
# -*- coding: utf-8 -*-
# Copyright 2021 Dell Inc. or its subsidiaries. All Rights Reserved
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
"""
The sfss_zone_alias class
It is in this file where the current configuration (as dict)
is compared to the provided configuration (as dict) and the command set
necessary to bring the current configuration to it's desired end-state is
created
"""
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type
from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.cfg.base import (
    ConfigBase,
)
from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.utils import (
    to_list,
)
from ansible_collections.dellemc.sfss.plugins.module_utils.network.sfss.facts.facts import Facts
from ansible_collections.dellemc.sfss.plugins.module_utils.network.sfss.config.base.sfss_config_base import (
    StfsConfigBase,
)
from ansible_collections.dellemc.sfss.plugins.module_utils.network.sfss.utils.debug import debug
from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.utils import (
    to_list,
)
from ansible_collections.dellemc.sfss.plugins.module_utils.network.sfss.facts.facts import Facts
from ansible_collections.dellemc.sfss.plugins.module_utils.network.sfss.constants.urls import (
    ZA_CONFIG_URL,
    ZA_MEMBER_CONFIG_URL,
    ZA_DELETE_URL,
    ZA_MEMBER_SPECIFIC_URL,
    ZA_ALL_MEMBER_DELETE_URL
)
from ansible_collections.dellemc.sfss.plugins.module_utils.network.sfss.constants.tranformers import (
    transform_end_point_name_type,
    transform_end_point_type,
)
from ansible_collections.dellemc.sfss.plugins.module_utils.network.sfss.utils.utils import (
    get_orginate_nqns,
)


class Zone_alias(StfsConfigBase):
    """
    The sfss_zone_alias class
    """

    gather_subset = [
        '!all',
        '!min',
    ]

    gather_network_resources = [
        'zone_alias',
    ]

    def __init__(self, module):
        super(Zone_alias, self).__init__(module)
        self.resource_name = "zone_alias"
        self.test_keys = [{'config': {'name': '', 'instance_id': '', 'members': ''}}]

    def resource_id(self, want):
        zone_alias_name = want.get('name')
        ret = "config:{zone_alias_name}"
        ret = ret.format(zone_alias_name=zone_alias_name)
        return ret

    def get_orginate_nqns_data(self):
        return get_orginate_nqns(self)

    def build_create_request(self, have, want):
        requests = []
        instance_id = want.get("instance_id")
        zone_alias_name = want.get('name')
        requests.append(self.build_create_zone_alias_req(instance_id, zone_alias_name))
        if want.get('members'):
            if want['members'].get('data'):
                zone_alias_members = want['members'].get('data')
                for zone_alias_member in zone_alias_members:
                    requests.append(self.build_create_zone_alias_member_req(instance_id, zone_alias_name, zone_alias_member))

        return requests

    def build_create_zone_alias_req(self, instance_id, zone_alias_name):
        method = "POST"
        zone_alias_url = ZA_CONFIG_URL.format(instance_id=instance_id, zonealias_str='ZoneAlias')
        zone_alias_payload = {}
        zone_alias_payload.update({'ZoneAliasName': zone_alias_name})
        zone_alias_payload.update({'ZoneDBType': 'config'})
        zone_alias_request = {'method': method, 'path': zone_alias_url, 'data': zone_alias_payload}

        return zone_alias_request

    def build_create_zone_alias_member_req(self, instance_id, zone_alias_name, zone_alias_member):
        method = "POST"
        zone_alias_member_url = ZA_MEMBER_CONFIG_URL.format(instance_id=instance_id, zonealias_str='ZoneAlias', zone_alias_name=zone_alias_name)
        zone_alias_member_payload = {}
        if zone_alias_member.get('id'):
            zone_alias_member_payload.update({'ZoneAliasMemberId': zone_alias_member.get('id')})
        if zone_alias_member.get('type'):
            member_type = transform_end_point_name_type(zone_alias_member.get('type'))
            zone_alias_member_payload.update({'ZoneAliasMemberType': member_type})
        if zone_alias_member.get('role'):
            zone_alias_member_payload.update({'Role': transform_end_point_type(zone_alias_member.get('role'))})
        zone_alias_member_request = {'method': method, 'path': zone_alias_member_url, 'data': zone_alias_member_payload}
        return zone_alias_member_request

    def build_delete_all_requests(self, commands):
        requests = []
        for zone_alias in commands:
            requests.append(self.build_delete_zone_alias_req(zone_alias))

        return commands, requests

    def build_delete_requests(self, commands, want, have, diff):
        ret_requests = []
        ret_commands = []
        debug("member zone_alias want", want)
        # if not commands:
        #     return commands, requests
        for zone_alias in want:
            debug("member zone_alias", zone_alias)
            requests = []
            matched_have = self.matches(zone_alias, have)
            if not matched_have:
                # Resource not available in have
                continue

            if not zone_alias.get('members'):
                requests.append(self.build_delete_zone_alias_req(zone_alias))
            elif not zone_alias['members'].get('data'):
                requests.extend(self.build_delete_zone_alias_all_members_req(zone_alias, have))
            else:
                for member in zone_alias['members'].get('data'):
                    debug("member delete", member)
                    instance_id = zone_alias.get("instance_id")
                    zone_alias_name = zone_alias.get('name')
                    request = self.build_delete_zone_alias_member_req(member, instance_id, zone_alias_name, have, zone_alias)
                    if len(request) > 0:
                        requests.append(request)

            if requests:
                ret_requests.extend(requests)
                ret_commands.append(zone_alias)

        return ret_commands, ret_requests

    def build_delete_zone_alias_req(self, zone_alias):
        method = "DELETE"
        instance_id = zone_alias.get("instance_id", 1)
        zone_alias_name = zone_alias.get('name')
        url = ZA_DELETE_URL.format(instance_id=instance_id, zone_alias_name=zone_alias_name)
        request = {"method": method,
                   "path": url}
        return request

    def build_delete_zone_alias_all_members_req(self, zone_alias, have):
        method = "DELETE"
        zone_alias_eid = self.resource_id(zone_alias)
        instance_id = zone_alias.get("instance_id", 1)
        zone_alias_name = zone_alias.get('name')
        members = []
        for have_za in have:
            have_eid = self.resource_id(have_za)
            if have_eid == zone_alias_eid:
                if have_za['members'].get('data'):
                    members = have_za['members'].get('data')
                    break
        requests = []
        for member in members:
            request = {
                "method": method,
                "path": ZA_ALL_MEMBER_DELETE_URL.format(instance_id=instance_id, zone_alias_name=zone_alias_name, member_id=member['id'])
            }
            requests.append(request)
        return requests

    def build_delete_zone_alias_member_req(self, member, instance_id, zone_alias_name, have, zone_alias):
        request = {}
        have_members = {}
        zone_alias_eid = self.resource_id(zone_alias)
        for have_za in have:
            have_eid = self.resource_id(have_za)
            if have_eid == zone_alias_eid:
                if have_za['members'].get('data'):
                    have_members = have_za['members'].get('data')
                    break
        debug("matched have members", have_members)
        matches, role = self.member_match(member, have_members, zone_alias_name)
        if matches:
            debug("matched have members1", True)
            method = "DELETE"
            url = ZA_MEMBER_SPECIFIC_URL.format(instance_id=instance_id, zone_alias_name=zone_alias_name, id=member['id'])
            request = {"method": method,
                       "path": url}
        return request

    def build_update_requests(self, have, matched_have, command):
        requests = []
        want_eid = self.resource_id(command)
        want_zone_alias_name = command['name']
        want_instance_id = command['instance_id']
        if command.get('members'):
            want_members = command['members']['data']
            for have_zone_alias in have:
                have_eid = self.resource_id(have_zone_alias)
                if have_eid == want_eid:
                    have_members = have_zone_alias['members'].get('data')
                    break
            requests.extend(self.build_update_member_req(want_members, have_members, want_zone_alias_name, want_instance_id))
        return requests

    def build_update_member_req(self, want_members, have_members, zone_alias_name, instance_id):
        requests = []
        for want_member in want_members:
            match, role = self.member_match(want_member, have_members, zone_alias_name)
            if match:
                if want_member['role'] != role:  # update want_member's role
                    method = "PUT"
                    URL = ZA_MEMBER_SPECIFIC_URL.format(instance_id=instance_id, zone_alias_name=zone_alias_name, id=want_member['id'])
                    payload = {
                        "Role": transform_end_point_type(want_member.get('role'))
                    }
                    requests.append(
                        {
                            "method": method,
                            "path": URL,
                            "data": payload
                        }
                    )
            else:
                # create want_member
                requests.append(self.build_create_zone_alias_member_req(instance_id, zone_alias_name, want_member))
        return requests

    def member_match(self, want_member, have_members, zone_alias_name):
        ep_id = "config:" + zone_alias_name + ":" + self.member_resource_id(want_member)
        matches = False
        for have_member in have_members:
            have_ep_id = self.member_resource_id(have_member)
            if ep_id == have_ep_id:
                matches = True
                debug("matches3", matches)
                return matches, have_member['role']

        debug("matches2", matches)
        return matches, None

    def member_resource_id(self, member):
        return member['id']
