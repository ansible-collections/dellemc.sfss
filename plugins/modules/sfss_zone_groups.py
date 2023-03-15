#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright 2021 Dell Inc. or its subsidiaries. All Rights Reserved
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

#############################################
#                WARNING                    #
#############################################
#
# This file is auto generated by the resource
#   module builder playbook.
#
# Do not edit this file manually.
#
# Changes to this file will be over written
#   by the resource module builder.
#
# Changes should be made in the model used to
#   generate this file or in the resource module
#   builder template.
#
#############################################

"""
The module file for sfss_zone_groups
"""

from __future__ import absolute_import, division, print_function
__metaclass__ = type


DOCUMENTATION = """
---
module: sfss_zone_groups
version_added: 1.0.0
notes:
- Idempotent is supported.
- Supports C(check_mode).
short_description: Manage SFSS zone groups
description:
  - This module is used to manage SFSS zone groups.
author: Mohamed Javeed (@javeedf)
options:
  config:
    description: A list of zone groups.
    type: list
    elements: dict
    suboptions:
      name:
        description:
          - Name of the zone group.
        type: str
        required: True
      instance_id:
        description:
          - Instance ID.
        type: int
        required: True
      activate_status:
        description:
          - Activate the zone group.
        type: bool
      activation_state:
        description:
          - Activation status of the zone group.
        type: str
  state:
    description:
      - The state the configuration should be left in.
    type: str
    choices:
     - merged
     - deleted
    default: merged
"""
EXAMPLES = """
# Using deleted
#
# Before state:
# -------------
#
# redfish/v1/SFSS/1/ZoneDBs('config')/ZoneGroups?$source=config&$expand=ZoneGroups
# "ZoneGroups": [
# {
#   "Type": "Manual",
#   "ZoneDBType": "config",
#   "ZoneGroupId": "config:play.zone_group1:nqn.1988-11.com.dell:SFSS:1:20210803224020e8",
#   "ActivateStatus": "DeActivate",
#   "zoneGroupName": "play.zone_group1",
#   "OriginatorNQN": "nqn.1988-11.com.dell:SFSS:1:20210803224020e8",
#   "ActivationState": "NotActive",
#   "@odata.id": "/redfish/v1/SFSS/1/ZoneDBs('config')/ZoneGroups('config:play.zone_group1:nqn.1988-11.com.dell:SFSS:1:20210803224020e8')",
#   "@odata.type": "#ZoneGroups.ZoneGroups",
#   "@odata.context": "/redfish/v1/SFSS/1/ZoneDBs('config')/$metadata#ZoneGroups/ZoneGroups/$entity"
# },
# {
#   "Type": "Manual",
#   "ZoneDBType": "config",
#   "ZoneGroupId": "config:reg.zone_group1:nqn.1988-11.com.dell:SFSS:1:20210803224020e8",
#   "ActivateStatus": "Activate",
#   "NumberZones": 1,
#   "zoneGroupName": "reg.zone_group1",
#   "OriginatorNQN": "nqn.1988-11.com.dell:SFSS:1:20210803224020e8",
#   "Zones": "config:reg.zone_group1:nqn.1988-11.com.dell:SFSS:1:20210803224020e8:reg.zone1",
#   "ActivationState": "ReActivationNeeded",
#   "@odata.id": "/redfish/v1/SFSS/1/ZoneDBs('config')/ZoneGroups('config:reg.zone_group1:nqn.1988-11.com.dell:SFSS:1:20210803224020e8')",
#   "@odata.type": "#ZoneGroups.ZoneGroups",
#   "@odata.context": "/redfish/v1/SFSS/1/ZoneDBs('config')/$metadata#ZoneGroups/ZoneGroups/$entity"
# },
# {
#   "Type": "Manual",
#   "ZoneDBType": "config",
#   "ZoneGroupId": "config:reg.zone_group2:nqn.1988-11.com.dell:SFSS:1:20210803224020e8",
#   "ActivateStatus": "Activate",
#   "NumberZones": 2,
#   "zoneGroupName": "reg.zone_group2",
#   "OriginatorNQN": "nqn.1988-11.com.dell:SFSS:1:20210803224020e8",
#   "Zones": "config:reg.zone_group2:nqn.1988-11.com.dell:SFSS:1:20210803224020e8:reg.zone2|
# config:reg.zone_group2:nqn.1988-11.com.dell:SFSS:1:20210803224020e8:reg.zone3",
#   "ActivationState": "ReActivationNeeded",
#   "@odata.id": "/redfish/v1/SFSS/1/ZoneDBs('config')/ZoneGroups('config:reg.zone_group2:nqn.1988-11.com.dell:SFSS:1:20210803224020e8')",
#   "@odata.type": "#ZoneGroups.ZoneGroups",
#   "@odata.context": "/redfish/v1/SFSS/1/ZoneDBs('config')/$metadata#ZoneGroups/ZoneGroups/$entity"
# },
# {
#   "Type": "Manual",
#   "ZoneDBType": "config",
#   "ZoneGroupId": "config:ansible.zone_grp1:nqn.1988-11.com.dell:SFSS:1:20210803224020e8",
#   "ActivateStatus": "Activate",
#   "zoneGroupName": "ansible.zone_grp1",
#   "OriginatorNQN": "nqn.1988-11.com.dell:SFSS:1:20210803224020e8",
#   "ActivationState": "Active",
#   "@odata.id": "/redfish/v1/SFSS/1/ZoneDBs('config')/ZoneGroups('config:ansible.zone_grp1:nqn.1988-11.com.dell:SFSS:1:20210803224020e8')",
#   "@odata.type": "#ZoneGroups.ZoneGroups",
#   "@odata.context": "/redfish/v1/SFSS/1/ZoneDBs('config')/$metadata#ZoneGroups/ZoneGroups/$entity"
# }
# ]
- name: Stfs zones create
  dellemc.sfss.zone_groups:
    config:
      - name: ansible.zone_grp1
        instance_id: 1
        activate_status: true
    state: deleted
#
# After state:
# -------------
#
# redfish/v1/SFSS/1/ZoneDBs('config')/ZoneGroups?$source=config&$expand=ZoneGroups
# "ZoneGroups": [
# {
#   "Type": "Manual",
#   "ZoneDBType": "config",
#   "ZoneGroupId": "config:play.zone_group1:nqn.1988-11.com.dell:SFSS:1:20210803224020e8",
#   "ActivateStatus": "DeActivate",
#   "zoneGroupName": "play.zone_group1",
#   "OriginatorNQN": "nqn.1988-11.com.dell:SFSS:1:20210803224020e8",
#   "ActivationState": "NotActive",
#   "@odata.id": "/redfish/v1/SFSS/1/ZoneDBs('config')/ZoneGroups('config:play.zone_group1:nqn.1988-11.com.dell:SFSS:1:20210803224020e8')",
#   "@odata.type": "#ZoneGroups.ZoneGroups",
#   "@odata.context": "/redfish/v1/SFSS/1/ZoneDBs('config')/$metadata#ZoneGroups/ZoneGroups/$entity"
# },
# {
#   "Type": "Manual",
#   "ZoneDBType": "config",
#   "ZoneGroupId": "config:reg.zone_group1:nqn.1988-11.com.dell:SFSS:1:20210803224020e8",
#   "ActivateStatus": "Activate",
#   "NumberZones": 1,
#   "zoneGroupName": "reg.zone_group1",
#   "OriginatorNQN": "nqn.1988-11.com.dell:SFSS:1:20210803224020e8",
#   "Zones": "config:reg.zone_group1:nqn.1988-11.com.dell:SFSS:1:20210803224020e8:reg.zone1",
#   "ActivationState": "ReActivationNeeded",
#   "@odata.id": "/redfish/v1/SFSS/1/ZoneDBs('config')/ZoneGroups('config:reg.zone_group1:nqn.1988-11.com.dell:SFSS:1:20210803224020e8')",
#   "@odata.type": "#ZoneGroups.ZoneGroups",
#   "@odata.context": "/redfish/v1/SFSS/1/ZoneDBs('config')/$metadata#ZoneGroups/ZoneGroups/$entity"
# },
# {
#   "Type": "Manual",
#   "ZoneDBType": "config",
#   "ZoneGroupId": "config:reg.zone_group2:nqn.1988-11.com.dell:SFSS:1:20210803224020e8",
#   "ActivateStatus": "Activate",
#   "NumberZones": 2,
#   "zoneGroupName": "reg.zone_group2",
#   "OriginatorNQN": "nqn.1988-11.com.dell:SFSS:1:20210803224020e8",
#   "Zones": "config:reg.zone_group2:nqn.1988-11.com.dell:SFSS:1:20210803224020e8:reg.zone2|
# config:reg.zone_group2:nqn.1988-11.com.dell:SFSS:1:20210803224020e8:reg.zone3",
#   "ActivationState": "ReActivationNeeded",
#   "@odata.id": "/redfish/v1/SFSS/1/ZoneDBs('config')/ZoneGroups('config:reg.zone_group2:nqn.1988-11.com.dell:SFSS:1:20210803224020e8')",
#   "@odata.type": "#ZoneGroups.ZoneGroups",
#   "@odata.context": "/redfish/v1/SFSS/1/ZoneDBs('config')/$metadata#ZoneGroups/ZoneGroups/$entity"
# }
# ]
#
# Using deleted
#
# Before state:
# -------------
#
# redfish/v1/SFSS/1/ZoneDBs('config')/ZoneGroups?$source=config&$expand=ZoneGroups
#
# "ZoneGroups": [
# {
#   "Type": "Manual",
#   "ZoneDBType": "config",
#   "ZoneGroupId": "config:play.zone_group1:nqn.1988-11.com.dell:SFSS:1:20210803224020e8",
#   "ActivateStatus": "DeActivate",
#   "zoneGroupName": "play.zone_group1",
#   "OriginatorNQN": "nqn.1988-11.com.dell:SFSS:1:20210803224020e8",
#   "ActivationState": "NotActive",
#   "@odata.id": "/redfish/v1/SFSS/1/ZoneDBs('config')/ZoneGroups('config:play.zone_group1:nqn.1988-11.com.dell:SFSS:1:20210803224020e8')",
#   "@odata.type": "#ZoneGroups.ZoneGroups",
#   "@odata.context": "/redfish/v1/SFSS/1/ZoneDBs('config')/$metadata#ZoneGroups/ZoneGroups/$entity"
# },
# {
#   "Type": "Manual",
#   "ZoneDBType": "config",
#   "ZoneGroupId": "config:reg.zone_group1:nqn.1988-11.com.dell:SFSS:1:20210803224020e8",
#   "ActivateStatus": "Activate",
#   "NumberZones": 1,
#   "zoneGroupName": "reg.zone_group1",
#   "OriginatorNQN": "nqn.1988-11.com.dell:SFSS:1:20210803224020e8",
#   "Zones": "config:reg.zone_group1:nqn.1988-11.com.dell:SFSS:1:20210803224020e8:reg.zone1",
#   "ActivationState": "ReActivationNeeded",
#   "@odata.id": "/redfish/v1/SFSS/1/ZoneDBs('config')/ZoneGroups('config:reg.zone_group1:nqn.1988-11.com.dell:SFSS:1:20210803224020e8')",
#   "@odata.type": "#ZoneGroups.ZoneGroups",
#   "@odata.context": "/redfish/v1/SFSS/1/ZoneDBs('config')/$metadata#ZoneGroups/ZoneGroups/$entity"
# },
# {
#   "Type": "Manual",
#   "ZoneDBType": "config",
#   "ZoneGroupId": "config:reg.zone_group2:nqn.1988-11.com.dell:SFSS:1:20210803224020e8",
#   "ActivateStatus": "Activate",
#   "NumberZones": 2,
#   "zoneGroupName": "reg.zone_group2",
#   "OriginatorNQN": "nqn.1988-11.com.dell:SFSS:1:20210803224020e8",
#   "Zones": "config:reg.zone_group2:nqn.1988-11.com.dell:SFSS:1:20210803224020e8:reg.zone2|
# config:reg.zone_group2:nqn.1988-11.com.dell:SFSS:1:20210803224020e8:reg.zone3",
#   "ActivationState": "ReActivationNeeded",
#   "@odata.id": "/redfish/v1/SFSS/1/ZoneDBs('config')/ZoneGroups('config:reg.zone_group2:nqn.1988-11.com.dell:SFSS:1:20210803224020e8')",
#   "@odata.type": "#ZoneGroups.ZoneGroups",
#   "@odata.context": "/redfish/v1/SFSS/1/ZoneDBs('config')/$metadata#ZoneGroups/ZoneGroups/$entity"
# }
# ]
- name: Stfs zones create
  dellemc.sfss.zone_groups:
    config: []
    state: deleted
#
#
# After state:
# -------------
# redfish/v1/SFSS/1/ZoneDBs('config')/ZoneGroups?$source=config&$expand=ZoneGroups
# {
#   "ZoneGroups@odata.count": 0,
#   "@odata.id": "/redfish/v1/SFSS/1/ZoneDBs('config')/ZoneGroups?$source=config&$expand=ZoneGroups",
#   "@odata.context": "/redfish/v1/SFSS/1/ZoneDBs('config')/$metadata#ZoneGroups",
#   "@odata.type": "#ZoneGroupsCollection.ZoneGroupsCollection"
# }
#
# Using merged
#
# Before state:
# -------------
#
# redfish/v1/SFSS/1/ZoneDBs('config')/ZoneGroups?$source=config&$expand=ZoneGroups
# "ZoneGroups": [
# {
#   "Type": "Manual",
#   "ZoneDBType": "config",
#   "ZoneGroupId": "config:play.zone_group1:nqn.1988-11.com.dell:SFSS:1:20210803224020e8",
#   "ActivateStatus": "DeActivate",
#   "zoneGroupName": "play.zone_group1",
#   "OriginatorNQN": "nqn.1988-11.com.dell:SFSS:1:20210803224020e8",
#   "ActivationState": "NotActive",
#   "@odata.id": "/redfish/v1/SFSS/1/ZoneDBs('config')/ZoneGroups('config:play.zone_group1:nqn.1988-11.com.dell:SFSS:1:20210803224020e8')",
#   "@odata.type": "#ZoneGroups.ZoneGroups",
#   "@odata.context": "/redfish/v1/SFSS/1/ZoneDBs('config')/$metadata#ZoneGroups/ZoneGroups/$entity"
# },
# {
#   "Type": "Manual",
#   "ZoneDBType": "config",
#   "ZoneGroupId": "config:reg.zone_group1:nqn.1988-11.com.dell:SFSS:1:20210803224020e8",
#   "ActivateStatus": "Activate",
#   "NumberZones": 1,
#   "zoneGroupName": "reg.zone_group1",
#   "OriginatorNQN": "nqn.1988-11.com.dell:SFSS:1:20210803224020e8",
#   "Zones": "config:reg.zone_group1:nqn.1988-11.com.dell:SFSS:1:20210803224020e8:reg.zone1",
#   "ActivationState": "ReActivationNeeded",
#   "@odata.id": "/redfish/v1/SFSS/1/ZoneDBs('config')/ZoneGroups('config:reg.zone_group1:nqn.1988-11.com.dell:SFSS:1:20210803224020e8')",
#   "@odata.type": "#ZoneGroups.ZoneGroups",
#   "@odata.context": "/redfish/v1/SFSS/1/ZoneDBs('config')/$metadata#ZoneGroups/ZoneGroups/$entity"
# },
# {
#   "Type": "Manual",
#   "ZoneDBType": "config",
#   "ZoneGroupId": "config:reg.zone_group2:nqn.1988-11.com.dell:SFSS:1:20210803224020e8",
#   "ActivateStatus": "Activate",
#   "NumberZones": 2,
#   "zoneGroupName": "reg.zone_group2",
#   "OriginatorNQN": "nqn.1988-11.com.dell:SFSS:1:20210803224020e8",
#   "Zones": "config:reg.zone_group2:nqn.1988-11.com.dell:SFSS:1:20210803224020e8:reg.zone2|
# config:reg.zone_group2:nqn.1988-11.com.dell:SFSS:1:20210803224020e8:reg.zone3",
#   "ActivationState": "ReActivationNeeded",
#   "@odata.id": "/redfish/v1/SFSS/1/ZoneDBs('config')/ZoneGroups('config:reg.zone_group2:nqn.1988-11.com.dell:SFSS:1:20210803224020e8')",
#   "@odata.type": "#ZoneGroups.ZoneGroups",
#   "@odata.context": "/redfish/v1/SFSS/1/ZoneDBs('config')/$metadata#ZoneGroups/ZoneGroups/$entity"
# }
# ]
- name: Stfs zones create
  dellemc.sfss.zone_groups:
    config:
      - name: ansible.zone_grp1
        instance_id: 1
        activate_status: true
#
# After state:
# -------------
#
# redfish/v1/SFSS/1/ZoneDBs('config')/ZoneGroups?$source=config&$expand=ZoneGroups
# "ZoneGroups": [
# {
#   "Type": "Manual",
#   "ZoneDBType": "config",
#   "ZoneGroupId": "config:play.zone_group1:nqn.1988-11.com.dell:SFSS:1:20210803224020e8",
#   "ActivateStatus": "DeActivate",
#   "zoneGroupName": "play.zone_group1",
#   "OriginatorNQN": "nqn.1988-11.com.dell:SFSS:1:20210803224020e8",
#   "ActivationState": "NotActive",
#   "@odata.id": "/redfish/v1/SFSS/1/ZoneDBs('config')/ZoneGroups('config:play.zone_group1:nqn.1988-11.com.dell:SFSS:1:20210803224020e8')",
#   "@odata.type": "#ZoneGroups.ZoneGroups",
#   "@odata.context": "/redfish/v1/SFSS/1/ZoneDBs('config')/$metadata#ZoneGroups/ZoneGroups/$entity"
# },
# {
#   "Type": "Manual",
#   "ZoneDBType": "config",
#   "ZoneGroupId": "config:reg.zone_group1:nqn.1988-11.com.dell:SFSS:1:20210803224020e8",
#   "ActivateStatus": "Activate",
#   "NumberZones": 1,
#   "zoneGroupName": "reg.zone_group1",
#   "OriginatorNQN": "nqn.1988-11.com.dell:SFSS:1:20210803224020e8",
#   "Zones": "config:reg.zone_group1:nqn.1988-11.com.dell:SFSS:1:20210803224020e8:reg.zone1",
#   "ActivationState": "ReActivationNeeded",
#   "@odata.id": "/redfish/v1/SFSS/1/ZoneDBs('config')/ZoneGroups('config:reg.zone_group1:nqn.1988-11.com.dell:SFSS:1:20210803224020e8')",
#   "@odata.type": "#ZoneGroups.ZoneGroups",
#   "@odata.context": "/redfish/v1/SFSS/1/ZoneDBs('config')/$metadata#ZoneGroups/ZoneGroups/$entity"
# },
# {
#   "Type": "Manual",
#   "ZoneDBType": "config",
#   "ZoneGroupId": "config:reg.zone_group2:nqn.1988-11.com.dell:SFSS:1:20210803224020e8",
#   "ActivateStatus": "Activate",
#   "NumberZones": 2,
#   "zoneGroupName": "reg.zone_group2",
#   "OriginatorNQN": "nqn.1988-11.com.dell:SFSS:1:20210803224020e8",
#   "Zones": "config:reg.zone_group2:nqn.1988-11.com.dell:SFSS:1:20210803224020e8:reg.zone2|
# config:reg.zone_group2:nqn.1988-11.com.dell:SFSS:1:20210803224020e8:reg.zone3",
#   "ActivationState": "ReActivationNeeded",
#   "@odata.id": "/redfish/v1/SFSS/1/ZoneDBs('config')/ZoneGroups('config:reg.zone_group2:nqn.1988-11.com.dell:SFSS:1:20210803224020e8')",
#   "@odata.type": "#ZoneGroups.ZoneGroups",
#   "@odata.context": "/redfish/v1/SFSS/1/ZoneDBs('config')/$metadata#ZoneGroups/ZoneGroups/$entity"
# },
# {
#   "Type": "Manual",
#   "ZoneDBType": "config",
#   "ZoneGroupId": "config:ansible.zone_grp1:nqn.1988-11.com.dell:SFSS:1:20210803224020e8",
#   "ActivateStatus": "DeActivate",
#   "NumberZones": 0,
#   "zoneGroupName": "ansible.zone_grp1",
#   "OriginatorNQN": "nqn.1988-11.com.dell:SFSS:1:20210803224020e8",
#   "ActivationState": "ReActivationNeeded",
#   "@odata.id": "/redfish/v1/SFSS/1/ZoneDBs('config')/ZoneGroups('config:ansible.zone_grp1:nqn.1988-11.com.dell:SFSS:1:20210803224020e8')",
#   "@odata.type": "#ZoneGroups.ZoneGroups",
#   "@odata.context": "/redfish/v1/SFSS/1/ZoneDBs('config')/$metadata#ZoneGroups/ZoneGroups/$entity"
# }
# ]
"""
RETURN = """
before:
  description: The configuration prior to the model invocation.
  returned: always
  sample: >
    The configuration returned will always be in the same format
     of the parameters above.
  type: list

after:
  description: The resulting configuration model invocation.
  returned: when changed
  sample: >
    The configuration returned will always be in the same format
     of the parameters above.
  type: list

commands:
  description: The set of commands pushed to the remote device.
  returned: always
  type: list
  sample: ['command 1', 'command 2', 'command 3']
"""


from ansible.module_utils.basic import AnsibleModule
from ansible_collections.dellemc.sfss.plugins.module_utils.network.sfss.argspec.zone_groups.zone_groups import Zone_groupsArgs
from ansible_collections.dellemc.sfss.plugins.module_utils.network.sfss.config.zone_groups.zone_groups import Zone_groups


def main():
    """
    Main entry point for module execution

    :returns: the result form module invocation
    """
    module = AnsibleModule(argument_spec=Zone_groupsArgs.argument_spec,
                           supports_check_mode=True)

    result = Zone_groups(module).execute_module()
    module.exit_json(**result)


if __name__ == '__main__':
    main()
