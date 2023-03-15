#
# -*- coding: utf-8 -*-
# Copyright 2021 Dell Inc. or its subsidiaries. All Rights Reserved
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
"""
The sfss zones fact class
It is in this file the configuration is collected from the device
for a given resource, parsed, and the facts tree is populated
based on the configuration.
"""
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible_collections.dellemc.sfss.plugins.module_utils.network.sfss.argspec.zones.zones import ZonesArgs
from ansible_collections.dellemc.sfss.plugins.module_utils.network.sfss.facts.base.sfss_facts_base import (
    StfsFactsBase,
)
from ansible_collections.dellemc.sfss.plugins.module_utils.network.sfss.utils.debug import debug
from ansible_collections.dellemc.sfss.plugins.module_utils.network.sfss.constants.tranformers import (
    zone_group_id,
    zone_id,
    get_orginate_nqn_by_instance,
    retransform_zone_member_type,
)
from ansible_collections.dellemc.sfss.plugins.module_utils.network.sfss.constants.urls import (
    ZONE_GROUP_ALL_URL,
    ZONES_ALL_URL,
    ZONE_MEMBER_ALL_URL,
)
from ansible_collections.dellemc.sfss.plugins.module_utils.network.sfss.utils.utils import (
    send_requests,
    get_instances,
    get_orginate_nqns,
)

GET = "get"
ZONE_GROUPS = "ZoneGroups"
ZONES = "Zones"
ZONE_MEMBERS = "ZoneMembers"


class ZonesFacts(StfsFactsBase):
    """ The sfss zones fact class
    """
    def __init__(self, module, subspec='config', options='options'):
        self.argument_spec = ZonesArgs.argument_spec
        self.resource_name = "zones"

        super(ZonesFacts, self).__init__(module)

    def get_all_data(self):
        instances = get_instances(self)
        self.orginate_nqns = get_orginate_nqns(self)
        ret = []
        for instance in instances:
            instance_id = instance.get("id")
            data = self.get_resource_data(instance_id)
            ret.extend(data)
        return ret

    def get_resource_data(self, instance_id):
        """Get all the endpoints available in instance"""
        requests = [{"path": ZONE_GROUP_ALL_URL.format(instance_id=instance_id, config_type="config"),
                     "method": GET}]
        responses = send_requests(self, requests)
        debug("get_zone_groups: req", requests)
        debug("get_zone_groups: responses", responses)
        ret_zone_groups = []
        for response in responses:
            if response and response[1].get(ZONE_GROUPS):
                for zone_group in response[1][ZONE_GROUPS]:
                    zones_by_group = self.get_zones(instance_id, zone_group.get('zoneGroupName', ''))
                    ret_zone_groups.extend(zones_by_group)

        return ret_zone_groups

    def get_zones(self, instance_id, zone_group):
        """Get all the endpoints available in instance"""
        orginate_nqn_id = get_orginate_nqn_by_instance(self.orginate_nqns, instance_id)
        debug("get_zones: orginate_nqns", self.orginate_nqns)
        debug("get_zones: orginate_nqn_id", orginate_nqn_id)
        zone_group_id_val = zone_group_id(zone_group, orginate_nqn_id)
        requests = [{"path": ZONES_ALL_URL.format(instance_id=instance_id, config_type="config",
                                                  zone_group_id=zone_group_id_val),
                     "method": GET}]
        debug("get_zones: requests", requests)
        responses = send_requests(self, requests)
        debug("get_zones: responses", responses)
        ret_zones = []
        for response in responses:
            if response and response[1].get(ZONES):
                for zone in response[1][ZONES]:
                    zone_data = {
                        "name": zone["ZoneName"],
                        "group_name": zone_group,
                        "instance_id": instance_id,
                    }
                    ret_zone = self.get_zone_members(zone_data)
                    ret_zones.append(ret_zone)
        debug("ret_zones: ", ret_zones)
        return ret_zones

    def get_zone_members(self, zone_data):
        """Get all the endpoints available in instance"""

        instance_id = zone_data["instance_id"]
        zone_group_name = zone_data["group_name"]
        zone_name = zone_data["name"]

        orginate_nqn_id = get_orginate_nqn_by_instance(self.orginate_nqns, instance_id)
        zone_group_id_val = zone_group_id(zone_group_name, orginate_nqn_id)

        zone_id_val = zone_id(zone_group_id_val, zone_name)

        requests = [{"path": ZONE_MEMBER_ALL_URL.format(instance_id=instance_id, config_type="config",
                                                        zone_group_id=zone_group_id_val,
                                                        zone_id=zone_id_val),
                     "method": GET}]
        responses = send_requests(self, requests)
        debug("get_zone_members: responses", responses)

        for response in responses:
            if response and response[1].get(ZONE_MEMBERS):
                member_list = []
                for zone_member in response[1][ZONE_MEMBERS]:
                    zone_member_db_id = zone_member["ZoneMemberId"]
                    member_name = zone_member_db_id.replace(zone_id_val + ':', '')
                    member_type = zone_member["ZoneMemberType"]
                    member = {
                        "id": member_name,
                        "id_type": retransform_zone_member_type(zone_member["ZoneMemberType"]),
                    }
                    if "ZoneAlias" not in member_type:
                        member.update({"role": zone_member["Role"].lower()})

                    member_list.append(member)
                zone_data.update({"members": {"data": member_list}})
        debug("get_zone_members: ", zone_data)
        return zone_data
    # def get_zone_member_name(self, zone_member_db_id, zone_id_val):
    #     member_name = zone_member_db_id.replace(zone_id_val)
