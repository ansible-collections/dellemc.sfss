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
The module file for sfss_zones
"""

from __future__ import absolute_import, division, print_function
__metaclass__ = type


DOCUMENTATION = """
---
module: sfss_zones
version_added: 1.0.0
notes:
- Idempotent is supported.
- Supports C(check_mode).
short_description: Manage the SFSS zone and zone member attributes
description:
  - This module is used to manage the SFSS zone and zone member attributes.
author: Mohamed Javeed (@javeedf)

options:
  config:
    description: A list of SFSS zones.
    type: list
    elements: dict
    suboptions:
      instance_id:
        description:
          - Instance ID.
        type: int
        required: True
      name:
        description:
          - Name of the zone.
        type: str
        required: True
      group_name:
        description:
          - Name of the zone group.
        type: str
        required: True
      members:
        description:
          - List of members associated with the zone.
        type: dict
        suboptions:
          data:
            description:
              - List of members associated with the zone.
            type: list
            elements: dict
            suboptions:
              id:
                description:
                  - ID of SFSS endpoints such as hosts, subsystems, or direct discovery controllers (DDCs).
                type: str
                required: True
              id_type:
                description:
                  - Endpoint ID type NQN, FQN, or zone alias.
                type: str
                choices:
                - nqn
                - fqn
                - zone_alias
                default: nqn
              role:
                description:
                  - Endpoint role.
                type: str
                choices:
                - host
                - subsystem
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
# Using merged
#
# Before state:
# -------------
#
#redfish/v1/SFSS/1/ZoneDBs('config')/ZoneGroups?$source=config&$expand=ZoneGroups
# "ZoneGroups": [
# {
#   "NumberZones": 1,
#   "Type": "Manual",
#   "ActivateStatus": "Activate",
#   "zoneGroupName": "zg1",
#   "OriginatorNQN": "nqn.1988-11.com.dell:SFSS:1:20210624220526e8",
#   "ZoneDBType": "config",
#   "Zones": "config:zg1:nqn.1988-11.com.dell:SFSS:1:20210624220526e8:z1",
#   "ZoneGroupId": "config:zg1:nqn.1988-11.com.dell:SFSS:1:20210624220526e8",
#   "ActivationState": "NotActive",
#   "@odata.id": "/redfish/v1/SFSS/1/ZoneDBs('config')/ZoneGroups('config:zg1:nqn.1988-11.com.dell:SFSS:1:20210624220526e8')",
#   "@odata.type": "#ZoneGroups.ZoneGroups",
#   "@odata.context": "/redfish/v1/SFSS/1/ZoneDBs('config')/$metadata#ZoneGroups/ZoneGroups/$entity"
# },
# {
#   "ActivationState": "NotActive",
#   "OriginatorNQN": "nqn.1988-11.com.dell:SFSS:1:20210624220526e8",
#   "ZoneDBType": "config",
#   "ActivateStatus": "Activate",
#   "Type": "Manual",
#   "ZoneGroupId": "config:reg.zone_group1:nqn.1988-11.com.dell:SFSS:1:20210624220526e8",
#   "zoneGroupName": "reg.zone_group1",
#   "@odata.id": "/redfish/v1/SFSS/1/ZoneDBs('config')/ZoneGroups('config:reg.zone_group1:nqn.1988-11.com.dell:SFSS:1:20210624220526e8')",
#   "@odata.type": "#ZoneGroups.ZoneGroups",
#   "@odata.context": "/redfish/v1/SFSS/1/ZoneDBs('config')/$metadata#ZoneGroups/ZoneGroups/$entity"
# },
# {
#   "ActivationState": "NotActive",
#   "OriginatorNQN": "nqn.1988-11.com.dell:SFSS:1:20210624220526e8",
#   "ZoneDBType": "config",
#   "ActivateStatus": "Activate",
#   "Type": "Manual",
#   "ZoneGroupId": "config:test-zg1:nqn.1988-11.com.dell:SFSS:1:20210624220526e8",
#   "zoneGroupName": "test-zg1",
#   "NumberZones": 1,
#   "Zones": "config:test-zg1:nqn.1988-11.com.dell:SFSS:1:20210624220526e8:zone-test1",
#   "@odata.id": "/redfish/v1/SFSS/1/ZoneDBs('config')/ZoneGroups('config:test-zg1:nqn.1988-11.com.dell:SFSS:1:20210624220526e8')",
#   "@odata.type": "#ZoneGroups.ZoneGroups",
#   "@odata.context": "/redfish/v1/SFSS/1/ZoneDBs('config')/$metadata#ZoneGroups/ZoneGroups/$entity"
# },
# {
#   "ActivationState": "NotActive",
#   "OriginatorNQN": "nqn.1988-11.com.dell:SFSS:1:20210624220526e8",
#   "ZoneDBType": "config",
#   "ActivateStatus": "Activate",
#   "Type": "Manual",
#   "ZoneGroupId": "config:play.zone_group1:nqn.1988-11.com.dell:SFSS:1:20210624220526e8",
#   "zoneGroupName": "play.zone_group1",
#   "@odata.id": "/redfish/v1/SFSS/1/ZoneDBs('config')/ZoneGroups('config:play.zone_group1:nqn.1988-11.com.dell:SFSS:1:20210624220526e8')",
#   "@odata.type": "#ZoneGroups.ZoneGroups",
#   "@odata.context": "/redfish/v1/SFSS/1/ZoneDBs('config')/$metadata#ZoneGroups/ZoneGroups/$entity"
# }
# ]
- name: Stfs zones create
  dellemc.sfss.zones:
    config:
      - name: Ansible_Zone
        instance_id: 1
        group_name: Zone_group_11
        members:
          data:
            - id: nqn.2014-08.org.nvmexpress:uuid:host
              id_type: nqn
              role: host
# After state:
# -------------
#
#redfish/v1/SFSS/1/ZoneDBs('config')/ZoneGroups?$source=config&$expand=ZoneGroups
# "ZoneGroups": [
# {
#   "NumberZones": 1,
#   "Type": "Manual",
#   "ActivateStatus": "Activate",
#   "zoneGroupName": "zg1",
#   "OriginatorNQN": "nqn.1988-11.com.dell:SFSS:1:20210624220526e8",
#   "ZoneDBType": "config",
#   "Zones": "config:zg1:nqn.1988-11.com.dell:SFSS:1:20210624220526e8:z1",
#   "ZoneGroupId": "config:zg1:nqn.1988-11.com.dell:SFSS:1:20210624220526e8",
#   "ActivationState": "NotActive",
#   "@odata.id": "/redfish/v1/SFSS/1/ZoneDBs('config')/ZoneGroups('config:zg1:nqn.1988-11.com.dell:SFSS:1:20210624220526e8')",
#   "@odata.type": "#ZoneGroups.ZoneGroups",
#   "@odata.context": "/redfish/v1/SFSS/1/ZoneDBs('config')/$metadata#ZoneGroups/ZoneGroups/$entity"
# },
# {
#   "ActivationState": "NotActive",
#   "OriginatorNQN": "nqn.1988-11.com.dell:SFSS:1:20210624220526e8",
#   "ZoneDBType": "config",
#   "ActivateStatus": "Activate",
#   "Type": "Manual",
#   "ZoneGroupId": "config:reg.zone_group1:nqn.1988-11.com.dell:SFSS:1:20210624220526e8",
#   "zoneGroupName": "reg.zone_group1",
#   "@odata.id": "/redfish/v1/SFSS/1/ZoneDBs('config')/ZoneGroups('config:reg.zone_group1:nqn.1988-11.com.dell:SFSS:1:20210624220526e8')",
#   "@odata.type": "#ZoneGroups.ZoneGroups",
#   "@odata.context": "/redfish/v1/SFSS/1/ZoneDBs('config')/$metadata#ZoneGroups/ZoneGroups/$entity"
# },
# {
#   "ActivationState": "NotActive",
#   "OriginatorNQN": "nqn.1988-11.com.dell:SFSS:1:20210624220526e8",
#   "ZoneDBType": "config",
#   "ActivateStatus": "Activate",
#   "Type": "Manual",
#   "ZoneGroupId": "config:test-zg1:nqn.1988-11.com.dell:SFSS:1:20210624220526e8",
#   "zoneGroupName": "test-zg1",
#   "NumberZones": 1,
#   "Zones": "config:test-zg1:nqn.1988-11.com.dell:SFSS:1:20210624220526e8:zone-test1",
#   "@odata.id": "/redfish/v1/SFSS/1/ZoneDBs('config')/ZoneGroups('config:test-zg1:nqn.1988-11.com.dell:SFSS:1:20210624220526e8')",
#   "@odata.type": "#ZoneGroups.ZoneGroups",
#   "@odata.context": "/redfish/v1/SFSS/1/ZoneDBs('config')/$metadata#ZoneGroups/ZoneGroups/$entity"
# },
# {
#   "ActivationState": "NotActive",
#   "OriginatorNQN": "nqn.1988-11.com.dell:SFSS:1:20210624220526e8",
#   "ZoneDBType": "config",
#   "ActivateStatus": "Activate",
#   "Type": "Manual",
#   "ZoneGroupId": "config:play.zone_group1:nqn.1988-11.com.dell:SFSS:1:20210624220526e8",
#   "zoneGroupName": "play.zone_group1",
#   "@odata.id": "/redfish/v1/SFSS/1/ZoneDBs('config')/ZoneGroups('config:play.zone_group1:nqn.1988-11.com.dell:SFSS:1:20210624220526e8')",
#   "@odata.type": "#ZoneGroups.ZoneGroups",
#   "@odata.context": "/redfish/v1/SFSS/1/ZoneDBs('config')/$metadata#ZoneGroups/ZoneGroups/$entity"
# },
# {
#   "ActivationState": "NotActive",
#   "OriginatorNQN": "nqn.1988-11.com.dell:SFSS:1:20210624220526e8",
#   "Type": "Manual",
#   "ZoneGroupId": "config:Zone_group_11:nqn.1988-11.com.dell:SFSS:1:20210624220526e8",
#   "ZoneDBType": "config",
#   "ActivateStatus": "Activate",
#   "zoneGroupName": "Zone_group_11",
#   "NumberZones": 2,
#   "Zones": "config:Zone_group_11:nqn.1988-11.com.dell:SFSS:1:20210624220526e8:Ansible_Zone|
#             config:Zone_group_11:nqn.1988-11.com.dell:SFSS:1:20210624220526e8:",
#   "@odata.id": "/redfish/v1/SFSS/1/ZoneDBs('config')/ZoneGroups('config:Zone_group_11:nqn.1988-11.com.dell:SFSS:1:20210624220526e8')",
#   "@odata.type": "#ZoneGroups.ZoneGroups",
#   "@odata.context": "/redfish/v1/SFSS/1/ZoneDBs('config')/$metadata#ZoneGroups/ZoneGroups/$entity"
# }
# ]
#redfish/v1/SFSS/1/ZoneDBs('config')/ZoneGroups('config:Zone_group_11:nqn.1988-11.com.dell:SFSS:1:20210624220526e8')/Zones?$source=config
# "Zones": [
# {
#   "@odata.id": "/redfish/v1/SFSS/1/ZoneDBs('config')/ZoneGroups('config:Zone_group_11:nqn.1988-11.com.dell:SFSS:1:20210624220526e8')
#                 /Zones('config:Zone_group_11:nqn.1988-11.com.dell:SFSS:1:20210624220526e8:Ansible_Zone')"
# }
# ]
#redfish/v1/SFSS/1/ZoneDBs('config')/ZoneGroups('config:Zone_group_11:nqn.1988-11.com.dell:SFSS:1:20210624220526e8')/Zones('config:Zone_group_11:nqn.1988-11.com.dell:SFSS:1:20210624220526e8:Ansible_Zone')/ZoneMembers?$source=config
# "ZoneMembers": [
# {
#   "ZoneMemberId": "config:Zone_group_11:nqn.1988-11.com.dell:SFSS:1:20210624220526e8:Ansible_Zone:nqn.2014-08.org.nvmexpress:uuid:host",
#   "Role": "Host",
#   "ZoneMemberType": "NQN",
#   "@odata.id": "/redfish/v1/SFSS/1/ZoneDBs('config')/ZoneGroups('config:Zone_group_11:nqn.1988-11.com.dell:SFSS:1:20210624220526e8')
# /Zones('config:Zone_group_11:nqn.1988-11.com.dell:SFSS:1:20210624220526e8:Ansible_Zone')
# /ZoneMembers('config:Zone_group_11:nqn.1988-11.com.dell:SFSS:1:20210624220526e8:Ansible_Zone:nqn.2014-08.org.nvmexpress:uuid:host')",
#   "@odata.type": "#ZoneMembers.ZoneMembers",
#   "@odata.context": "/redfish/v1/SFSS/1/ZoneDBs('config')/ZoneGroups('config:Zone_group_11:nqn.1988-11.com.dell:SFSS:1:20210624220526e8')
# /Zones('config:Zone_group_11:nqn.1988-11.com.dell:SFSS:1:20210624220526e8:Ansible_Zone')/$metadata#ZoneMembers/ZoneMembers/$entity"
# }
# ]
# Using deleted
#
# Before state:
# -------------
#
#redfish/v1/SFSS/1/ZoneDBs('config')/ZoneGroups('config:Zone_group_11:nqn.1988-11.com.dell:SFSS:1:20210624220526e8')/Zones('config:Zone_group_11:nqn.1988-11.com.dell:SFSS:1:20210624220526e8:Ansible_Zone')/ZoneMembers?$source=config
# "ZoneMembers": [
# {
#   "ZoneMemberId": "config:Zone_group_11:nqn.1988-11.com.dell:SFSS:1:20210624220526e8:Ansible_Zone:nqn.2014-08.org.nvmexpress:uuid:host",
#   "Role": "Host",
#   "ZoneMemberType": "NQN",
#   "@odata.id": "/redfish/v1/SFSS/1/ZoneDBs('config')/ZoneGroups('config:Zone_group_11:nqn.1988-11.com.dell:SFSS:1:20210624220526e8')
# /Zones('config:Zone_group_11:nqn.1988-11.com.dell:SFSS:1:20210624220526e8:Ansible_Zone')
# /ZoneMembers('config:Zone_group_11:nqn.1988-11.com.dell:SFSS:1:20210624220526e8:Ansible_Zone:nqn.2014-08.org.nvmexpress:uuid:host')",
#   "@odata.type": "#ZoneMembers.ZoneMembers",
#   "@odata.context": "/redfish/v1/SFSS/1/ZoneDBs('config')/ZoneGroups('config:Zone_group_11:nqn.1988-11.com.dell:SFSS:1:20210624220526e8')
# /Zones('config:Zone_group_11:nqn.1988-11.com.dell:SFSS:1:20210624220526e8:Ansible_Zone')/$metadata#ZoneMembers/ZoneMembers/$entity"
# }
# ]
- name: Stfs zones create
  dellemc.sfss.zones:
    config:
      - name: Ansible_Zone
        instance_id: 1
        group_name: Zone_group_11
        members:
          data:
            - id: nqn.2014-08.org.nvmexpress:uuid:host
              id_type: nqn
              role: host
    state: deleted

#
# After state:
# -------------
#
#redfish/v1/SFSS/1/ZoneDBs('config')/ZoneGroups('config:Zone_group_11:nqn.1988-11.com.dell:SFSS:1:20210624220526e8')/Zones('config:Zone_group_11:nqn.1988-11.com.dell:SFSS:1:20210624220526e8:Ansible_Zone')/ZoneMembers?$source=config&$expand=ZoneMembers
# {
#   "ZoneMembers@odata.count": 0,
#   "@odata.id": "/redfish/v1/SFSS/1/ZoneDBs('config')/ZoneGroups('config:Zone_group_11:nqn.1988-11.com.dell:SFSS:1:20210624220526e8')
#   /Zones('config:Zone_group_11:nqn.1988-11.com.dell:SFSS:1:20210624220526e8:Ansible_Zone')/ZoneMembers?$source=config&$expand=ZoneMembers",
#   "@odata.context": "/redfish/v1/SFSS/1/ZoneDBs('config')/ZoneGroups('config:Zone_group_11:nqn.1988-11.com.dell:SFSS:1:20210624220526e8')
#   /Zones('config:Zone_group_11:nqn.1988-11.com.dell:SFSS:1:20210624220526e8:Ansible_Zone')/$metadata#ZoneMembers",
#   "@odata.type": "#ZoneMembersCollection.ZoneMembersCollection"
# }

# Using deleted
#
# Before state:
# -------------
#
#redfish/v1/SFSS/1/ZoneDBs('config')/ZoneGroups?$source=config&$expand=ZoneGroups
# "ZoneGroups": [
# {
#   "NumberZones": 1,
#   "Type": "Manual",
#   "ActivateStatus": "Activate",
#   "zoneGroupName": "zg1",
#   "OriginatorNQN": "nqn.1988-11.com.dell:SFSS:1:20210624220526e8",
#   "ZoneDBType": "config",
#   "Zones": "config:zg1:nqn.1988-11.com.dell:SFSS:1:20210624220526e8:z1",
#   "ZoneGroupId": "config:zg1:nqn.1988-11.com.dell:SFSS:1:20210624220526e8",
#   "ActivationState": "NotActive",
#   "@odata.id": "/redfish/v1/SFSS/1/ZoneDBs('config')/ZoneGroups('config:zg1:nqn.1988-11.com.dell:SFSS:1:20210624220526e8')",
#   "@odata.type": "#ZoneGroups.ZoneGroups",
#   "@odata.context": "/redfish/v1/SFSS/1/ZoneDBs('config')/$metadata#ZoneGroups/ZoneGroups/$entity"
# },
# {
#   "ActivationState": "NotActive",
#   "OriginatorNQN": "nqn.1988-11.com.dell:SFSS:1:20210624220526e8",
#   "ZoneDBType": "config",
#   "ActivateStatus": "Activate",
#   "Type": "Manual",
#   "ZoneGroupId": "config:reg.zone_group1:nqn.1988-11.com.dell:SFSS:1:20210624220526e8",
#   "zoneGroupName": "reg.zone_group1",
#   "@odata.id": "/redfish/v1/SFSS/1/ZoneDBs('config')/ZoneGroups('config:reg.zone_group1:nqn.1988-11.com.dell:SFSS:1:20210624220526e8')",
#   "@odata.type": "#ZoneGroups.ZoneGroups",
#   "@odata.context": "/redfish/v1/SFSS/1/ZoneDBs('config')/$metadata#ZoneGroups/ZoneGroups/$entity"
# },
# {
#   "ActivationState": "NotActive",
#   "OriginatorNQN": "nqn.1988-11.com.dell:SFSS:1:20210624220526e8",
#   "ZoneDBType": "config",
#   "ActivateStatus": "Activate",
#   "Type": "Manual",
#   "ZoneGroupId": "config:test-zg1:nqn.1988-11.com.dell:SFSS:1:20210624220526e8",
#   "zoneGroupName": "test-zg1",
#   "NumberZones": 1,
#   "Zones": "config:test-zg1:nqn.1988-11.com.dell:SFSS:1:20210624220526e8:zone-test1",
#   "@odata.id": "/redfish/v1/SFSS/1/ZoneDBs('config')/ZoneGroups('config:test-zg1:nqn.1988-11.com.dell:SFSS:1:20210624220526e8')",
#   "@odata.type": "#ZoneGroups.ZoneGroups",
#   "@odata.context": "/redfish/v1/SFSS/1/ZoneDBs('config')/$metadata#ZoneGroups/ZoneGroups/$entity"
# },
# {
#   "ActivationState": "NotActive",
#   "OriginatorNQN": "nqn.1988-11.com.dell:SFSS:1:20210624220526e8",
#   "ZoneDBType": "config",
#   "ActivateStatus": "Activate",
#   "Type": "Manual",
#   "ZoneGroupId": "config:play.zone_group1:nqn.1988-11.com.dell:SFSS:1:20210624220526e8",
#   "zoneGroupName": "play.zone_group1",
#   "@odata.id": "/redfish/v1/SFSS/1/ZoneDBs('config')/ZoneGroups('config:play.zone_group1:nqn.1988-11.com.dell:SFSS:1:20210624220526e8')",
#   "@odata.type": "#ZoneGroups.ZoneGroups",
#   "@odata.context": "/redfish/v1/SFSS/1/ZoneDBs('config')/$metadata#ZoneGroups/ZoneGroups/$entity"
# }
# ]
- name: Stfs zones create
  dellemc.sfss.zones:
    config: []
    state: deleted
#
# After state:
# -------------
#
#redfish/v1/SFSS/1/ZoneDBs('config')/ZoneGroups?$source=config&$expand=ZoneGroups
# {
#   "ZoneGroups@odata.count": 0,
#   "@odata.id": "/redfish/v1/SFSS/1/ZoneDBs('config')/ZoneGroups?$source=config&$expand=ZoneGroups",
#   "@odata.context": "/redfish/v1/SFSS/1/ZoneDBs('config')/$metadata#ZoneGroups",
#   "@odata.type": "#ZoneGroupsCollection.ZoneGroupsCollection"
# }
"""
RETURN = """
before:
  description: The configuration prior to the model invocation.
  returned: always
  sample: ['ZoneName: ansible_zone1', 'numberZoneMembers: 0', 'zoneId: config:AutoZonegroupnew:nqn.1988-11.com.dell:SFSS:1:20230314033523e8:ansible_zone1']
  type: list

after:
  description: The resulting configuration model invocation.
  returned: when changed
  sample: ['ZoneName: ansible_zone1', 'numberZoneMembers: 0', 'zoneId: config:AutoZonegroupnew:nqn.1988-11.com.dell:SFSS:1:20230314033523e8:ansible_zone1']
  type: list

commands:
  description: The set of commands pushed to the remote device.
  returned: always
  type: list
  sample: ['command 1', 'command 2', 'command 3']
"""


from ansible.module_utils.basic import AnsibleModule
from ansible_collections.dellemc.sfss.plugins.module_utils.network.sfss.argspec.zones.zones import ZonesArgs
from ansible_collections.dellemc.sfss.plugins.module_utils.network.sfss.config.zones.zones import Zones


def main():
    """
    Main entry point for module execution

    :returns: the result form module invocation
    """
    module = AnsibleModule(argument_spec=ZonesArgs.argument_spec,
                           supports_check_mode=True)

    result = Zones(module).execute_module()
    module.exit_json(**result)


if __name__ == '__main__':
    main()
