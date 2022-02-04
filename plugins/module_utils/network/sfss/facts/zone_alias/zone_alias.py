#
# -*- coding: utf-8 -*-
# Copyright 2021 Dell Inc. or its subsidiaries. All Rights Reserved
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
"""
The sfss zone_alias fact class
It is in this file the configuration is collected from the device
for a given resource, parsed, and the facts tree is populated
based on the configuration.
"""
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type
from ansible_collections.dellemc.sfss.plugins.module_utils.network.sfss.argspec.zone_alias.zone_alias import Zone_aliasArgs
from ansible_collections.dellemc.sfss.plugins.module_utils.network.sfss.utils.debug import debug
from ansible_collections.dellemc.sfss.plugins.module_utils.network.sfss.facts.base.sfss_facts_base import (
    StfsFactsBase,
)
from ansible_collections.dellemc.sfss.plugins.module_utils.network.sfss.constants.urls import (
    ZONE_ALIAS_URL,
    ZA_MEMBER_SPECIFIC_GET_URL,
)
from ansible_collections.dellemc.sfss.plugins.module_utils.network.sfss.utils.utils import (
    send_requests,
    get_instances,
)
from ansible.module_utils.connection import ConnectionError

from ansible_collections.dellemc.sfss.plugins.module_utils.network.sfss.constants.tranformers import (
    transform_end_point_name_type,
    transform_end_point_type,
    retransform_end_point_name_type,
)

GET = "get"
TYPE_STR = "ZoneAlias"


class Zone_aliasFacts(StfsFactsBase):
    """ The sfss zone_alias fact class
    """

    def __init__(self, module):
        self.argument_spec = Zone_aliasArgs.argument_spec
        self.resource_name = "zone_alias"
        super(Zone_aliasFacts, self).__init__(module)

    def get_resource_data(self, instance_id):
        """Get all the zone_alias available in instance"""
        requests = [{"path": ZONE_ALIAS_URL.format(instance_id=instance_id, zonealias_str=TYPE_STR),
                     "method": GET}]
        responses = send_requests(self, requests)

        ret = []
        for response in responses:
            if response and response[1].get(TYPE_STR):
                for zone_alias_data in response[1][TYPE_STR]:
                    name = zone_alias_data.get("ZoneAliasName")
                    za_member_ids = zone_alias_data.get("ZoneAliasMembers", [])
                    members_data = []
                    for member_id in za_member_ids:
                        member_data = self.get_zone_alias_members(name, instance_id, member_id)
                        members_data.append(member_data)

                    ret_data = {
                        "name": name,
                        "instance_id": instance_id,
                        "members": {
                            "data": members_data
                        }
                    }
                    # ret_data.update({"members": {"data" : members_data}})
                    ret.append(ret_data)

        return ret

    def get_zone_alias_members(self, name, instance_id, member_id):
        url = ZA_MEMBER_SPECIFIC_GET_URL.format(instance_id=instance_id, zone_alias_name=name,
                                                member_id=member_id, zonealias_str=TYPE_STR)
        requests = [{"path": url,
                     "method": GET}]
        debug("requests", requests)
        responses = send_requests(self, requests)
        debug("responses", responses)
        member_data_res = responses[0][1]
        debug("member_data_res", member_data_res)
        member_data = {"id": member_data_res.get('ZoneAliasMemberId'),
                       "type": retransform_end_point_name_type(member_data_res.get('ZoneAliasMemberType')),
                       "role": member_data_res.get('Role').lower()}
        debug("get_zone_alias_members", member_data)
        return member_data
