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
The module file for sfss_cdc_instances
"""

from __future__ import absolute_import, division, print_function
__metaclass__ = type


DOCUMENTATION = """
---
module:  sfss_cdc_instances
version_added: 1.0.0
notes:
- Idempotent is supported.
- Supports C(check_mode).
short_description: Manage the SFSS CDC Instance Manager attributes
description:
  - This module is used to manage the SFSS CDC Instance Manager attributes.
author: Namrata Chatterjee (@nchatterjee)

options:
  config:
    description: A list of CDC instances.
    type: list
    elements: dict
    suboptions:
      instance_id:
        type: int
        description: The instance identifier.
        required: True
      interfaces:
        description: A list of interface members.
        type: list
        elements: dict
        suboptions:
          name:
            description:
            - Name of the interface.
            type: str
            required: True
      admin_state:
        type: bool
        description:
        - Administrative state of the interface, enable or disable.
        required: True
      discovery_svc_admin_state:
        type: bool
        required: True
        description:
        - Administrative state of the discovery service, enable or disable.
  state:
    description:
    - The state the configuration should be left in
    type: str
    choices:
    - merged
    - deleted
    default: merged
"""
EXAMPLES = """
# Using deleted
#
#
# Before state:
# -------------
#
# redfish/v1/SFSSApp/CDCInstanceManagers
# "CDCInstanceManagers": [
# {
#     "CDCAdminState": "Enable",
#     "DiscoverySvcAdminState": "Enable",
#     "InstanceIdentifier": "1",
#     "Interfaces": [
#         "ens192.222"
#     ],
#     "IpAddresses": [
#         "12.1.1.222"
#     ],
#     "@odata.id": "/redfish/v1/SFSSApp/CDCInstanceManagers('1')",
#     "@odata.type": "#CDCInstanceManagers.CDCInstanceManagers",
#     "@odata.context": "/redfish/v1/SFSSApp/$metadata#CDCInstanceManagers/CDCInstanceManagers/$entity"
# },
# {
#     "CDCAdminState": "Enable",
#     "DiscoverySvcAdminState": "Enable",
#     "InstanceIdentifier": "3",
#     "Interfaces": [
#         "ens160"
#     ],
#     "IpAddresses": [
#         "100.104.26.76"
#     ],
#     "@odata.id": "/redfish/v1/SFSSApp/CDCInstanceManagers('3')",
#     "@odata.type": "#CDCInstanceManagers.CDCInstanceManagers",
#     "@odata.context": "/redfish/v1/SFSSApp/$metadata#CDCInstanceManagers/CDCInstanceManagers/$entity"
# },
# {
#     "CDCAdminState": "Enable",
#     "DiscoverySvcAdminState": "Disable",
#     "InstanceIdentifier": "2",
#     "Interfaces": [
#         "ens192.223"
#     ],
#     "IpAddresses": [
#         "12.1.1.223"
#     ],
#     "@odata.id": "/redfish/v1/SFSSApp/CDCInstanceManagers('2')",
#     "@odata.type": "#CDCInstanceManagers.CDCInstanceManagers",
#     "@odata.context": "/redfish/v1/SFSSApp/$metadata#CDCInstanceManagers/CDCInstanceManagers/$entity"
# }
# ]
- name: Create CDC instances
  dellemc.sfss.cdc_instances:
  config:
  - admin_state: true
    discovery_svc_admin_state: true
    instance_id: 1
    interfaces:
    - name: ens192.222
  state: deleted
#
# After state:
# -------------
#
# redfish/v1/SFSSApp/CDCInstanceManagers
# "CDCInstanceManagers": [
# {
#     "CDCAdminState": "Enable",
#     "DiscoverySvcAdminState": "Enable",
#     "InstanceIdentifier": "3",
#     "Interfaces": [
#         "ens160"
#     ],
#     "IpAddresses": [
#         "100.104.26.76"
#     ],
#     "@odata.id": "/redfish/v1/SFSSApp/CDCInstanceManagers('3')",
#     "@odata.type": "#CDCInstanceManagers.CDCInstanceManagers",
#     "@odata.context": "/redfish/v1/SFSSApp/$metadata#CDCInstanceManagers/CDCInstanceManagers/$entity"
# },
# {
#     "CDCAdminState": "Enable",
#     "DiscoverySvcAdminState": "Disable",
#     "InstanceIdentifier": "2",
#     "Interfaces": [
#         "ens192.223"
#     ],
#     "IpAddresses": [
#         "12.1.1.223"
#     ],
#     "@odata.id": "/redfish/v1/SFSSApp/CDCInstanceManagers('2')",
#     "@odata.type": "#CDCInstanceManagers.CDCInstanceManagers",
#     "@odata.context": "/redfish/v1/SFSSApp/$metadata#CDCInstanceManagers/CDCInstanceManagers/$entity"
# }
# ]
# Using deleted
#
#
# Before state:
# -------------
#
#redfish/v1/SFSSApp/CDCInstanceManagers
# "CDCInstanceManagers": [
# {
#     "CDCAdminState": "Enable",
#     "DiscoverySvcAdminState": "Enable",
#     "InstanceIdentifier": "1",
#     "Interfaces": [
#         "ens192.222"
#     ],
#     "IpAddresses": [
#         "12.1.1.222"
#     ],
#     "@odata.id": "/redfish/v1/SFSSApp/CDCInstanceManagers('1')",
#     "@odata.type": "#CDCInstanceManagers.CDCInstanceManagers",
#     "@odata.context": "/redfish/v1/SFSSApp/$metadata#CDCInstanceManagers/CDCInstanceManagers/$entity"
# },
# {
#     "CDCAdminState": "Enable",
#     "DiscoverySvcAdminState": "Enable",
#     "InstanceIdentifier": "3",
#     "Interfaces": [
#         "ens160"
#     ],
#     "IpAddresses": [
#         "100.104.26.76"
#     ],
#     "@odata.id": "/redfish/v1/SFSSApp/CDCInstanceManagers('3')",
#     "@odata.type": "#CDCInstanceManagers.CDCInstanceManagers",
#     "@odata.context": "/redfish/v1/SFSSApp/$metadata#CDCInstanceManagers/CDCInstanceManagers/$entity"
# },
# {
#     "CDCAdminState": "Enable",
#     "DiscoverySvcAdminState": "Disable",
#     "InstanceIdentifier": "2",
#     "Interfaces": [
#         "ens192.223"
#     ],
#     "IpAddresses": [
#         "12.1.1.223"
#     ],
#     "@odata.id": "/redfish/v1/SFSSApp/CDCInstanceManagers('2')",
#     "@odata.type": "#CDCInstanceManagers.CDCInstanceManagers",
#     "@odata.context": "/redfish/v1/SFSSApp/$metadata#CDCInstanceManagers/CDCInstanceManagers/$entity"
# }
# ]
- name: Create CDC instances
  dellemc.sfss.cdc_instances:
    config: []
    state: deleted
#
# After state:
# -------------
#
#redfish/v1/SFSSApp/CDCInstanceManagers
# {
# "CDCInstanceManagers@odata.count": 0,
# "@odata.id": "/redfish/v1/SFSSApp/CDCInstanceManagers?$expand=CDCInstanceManagers",
# "@odata.context": "/redfish/v1/SFSSApp/$metadata#CDCInstanceManagers",
# "@odata.type": "#CDCInstanceManagersCollection.CDCInstanceManagersCollection"
# }
#
#
# Using merged
#
#
# Before state:
# -------------
#
#redfish/v1/SFSSApp/CDCInstanceManagers
# "CDCInstanceManagers": [
# {
#     "CDCAdminState": "Enable",
#     "DiscoverySvcAdminState": "Enable",
#     "InstanceIdentifier": "3",
#     "Interfaces": [
#         "ens160"
#     ],
#     "IpAddresses": [
#         "100.104.26.76"
#     ],
#     "@odata.id": "/redfish/v1/SFSSApp/CDCInstanceManagers('3')",
#     "@odata.type": "#CDCInstanceManagers.CDCInstanceManagers",
#     "@odata.context": "/redfish/v1/SFSSApp/$metadata#CDCInstanceManagers/CDCInstanceManagers/$entity"
# },
# {
#     "CDCAdminState": "Enable",
#     "DiscoverySvcAdminState": "Disable",
#     "InstanceIdentifier": "2",
#     "Interfaces": [
#         "ens192.223"
#     ],
#     "IpAddresses": [
#         "12.1.1.223"
#     ],
#     "@odata.id": "/redfish/v1/SFSSApp/CDCInstanceManagers('2')",
#     "@odata.type": "#CDCInstanceManagers.CDCInstanceManagers",
#     "@odata.context": "/redfish/v1/SFSSApp/$metadata#CDCInstanceManagers/CDCInstanceManagers/$entity"
# }
# ]
- name: Create CDC instances
  dellemc.sfss.cdc_instances:
  config:
  - admin_state: true
    discovery_svc_admin_state: true
    instance_id: 1
    interfaces:
    - name: ens192.222
#
# After state:
# -------------
#
#redfish/v1/SFSSApp/CDCInstanceManagers
# "CDCInstanceManagers": [
# {
#     "CDCAdminState": "Enable",
#     "DiscoverySvcAdminState": "Enable",
#     "InstanceIdentifier": "1",
#     "Interfaces": [
#         "ens192.222"
#     ],
#     "IpAddresses": [
#         "12.1.1.222"
#     ],
#     "@odata.id": "/redfish/v1/SFSSApp/CDCInstanceManagers('1')",
#     "@odata.type": "#CDCInstanceManagers.CDCInstanceManagers",
#     "@odata.context": "/redfish/v1/SFSSApp/$metadata#CDCInstanceManagers/CDCInstanceManagers/$entity"
# },
# {
#     "CDCAdminState": "Enable",
#     "DiscoverySvcAdminState": "Enable",
#     "InstanceIdentifier": "3",
#     "Interfaces": [
#         "ens160"
#     ],
#     "IpAddresses": [
#         "100.104.26.76"
#     ],
#     "@odata.id": "/redfish/v1/SFSSApp/CDCInstanceManagers('3')",
#     "@odata.type": "#CDCInstanceManagers.CDCInstanceManagers",
#     "@odata.context": "/redfish/v1/SFSSApp/$metadata#CDCInstanceManagers/CDCInstanceManagers/$entity"
# },
# {
#     "CDCAdminState": "Enable",
#     "DiscoverySvcAdminState": "Disable",
#     "InstanceIdentifier": "2",
#     "Interfaces": [
#         "ens192.223"
#     ],
#     "IpAddresses": [
#         "12.1.1.223"
#     ],
#     "@odata.id": "/redfish/v1/SFSSApp/CDCInstanceManagers('2')",
#     "@odata.type": "#CDCInstanceManagers.CDCInstanceManagers",
#     "@odata.context": "/redfish/v1/SFSSApp/$metadata#CDCInstanceManagers/CDCInstanceManagers/$entity"
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
from ansible_collections.dellemc.sfss.plugins.module_utils.network.sfss.argspec.cdc_instances.cdc_instances import Cdc_instancesArgs
from ansible_collections.dellemc.sfss.plugins.module_utils.network.sfss.config.cdc_instances.cdc_instances import Cdc_instances


def main():
    """
    Main entry point for module execution

    :returns: the result form module invocation
    """
    module = AnsibleModule(argument_spec=Cdc_instancesArgs.argument_spec,
                           supports_check_mode=True)

    result = Cdc_instances(module).execute_module()
    module.exit_json(**result)


if __name__ == '__main__':
    main()