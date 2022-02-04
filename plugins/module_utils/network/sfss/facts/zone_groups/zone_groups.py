#
# -*- coding: utf-8 -*-
# Copyright 2021 Dell Inc. or its subsidiaries. All Rights Reserved
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
"""
The sfss zone_groups fact class
It is in this file the configuration is collected from the device
for a given resource, parsed, and the facts tree is populated
based on the configuration.
"""
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type
from ansible_collections.dellemc.sfss.plugins.module_utils.network.sfss.facts.base.sfss_facts_base import (
    StfsFactsBase,
)
from ansible_collections.dellemc.sfss.plugins.module_utils.network.sfss.utils.debug import debug
from ansible_collections.dellemc.sfss.plugins.module_utils.network.sfss.constants.tranformers import (
    retransform_zone_group_active_state,
)
from ansible_collections.dellemc.sfss.plugins.module_utils.network.sfss.constants.urls import (
    ZONE_GROUP_ALL_URL,
)
from ansible_collections.dellemc.sfss.plugins.module_utils.network.sfss.utils.utils import (
    send_requests,
    get_instances,
    get_orginate_nqns,
)
from ansible_collections.dellemc.sfss.plugins.module_utils.network.sfss.argspec.zone_groups.zone_groups import Zone_groupsArgs

GET = "get"
ZONE_GROUPS = "ZoneGroups"


class Zone_groupsFacts(StfsFactsBase):
    """ The sfss zone_groups fact class
    """

    def __init__(self, module):
        self.argument_spec = Zone_groupsArgs.argument_spec
        self.resource_name = "zone_groups"
        super(Zone_groupsFacts, self).__init__(module)

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
                    name = zone_group.get('zoneGroupName')
                    activate_state_str = zone_group.get('ActivateStatus')
                    active_state = retransform_zone_group_active_state(activate_state_str)
                    ret_zone_groups.append({
                        "instance_id": instance_id,
                        "name": name,
                        "activate_status": active_state
                    })

        return ret_zone_groups
