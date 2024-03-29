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
The module file for sfss_security_authentication
"""

from __future__ import absolute_import, division, print_function
__metaclass__ = type


DOCUMENTATION = """
---
module: sfss_security_authentication
version_added: 1.0.0
notes:
- Idempotent is supported.
- Supports C(check_mode).
short_description: Manage remote RADIUS and TACACS servers
description:
  - This module is used to manage remote RADIUS and TACACS servers and to define the authentication sequence.
author: Namrata Chatterjee (@nchatterjee)

options:
  config:
    description: A list of authentication servers.
    type: list
    elements: dict
    suboptions:
      authentication_sequence:
        type: list
        elements: str
        description: The authentication sequence list.
        required: True
      authentication_servers:
        description: Details of the authentication servers.
        type: list
        elements: dict
        suboptions:
          server_ip:
            description:
            - Server IP address.
            type: str
          password:
            description:
            - Server password.
            type: str
          authentication_type:
            description:
            - Authentication type.
            type: str
            required: True
            choices:
            - tacacs
            - radius
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
# Before state:
# -------------
#
# redfish/v1/SFSSApp/RadiusServers
# "RadiusServers": [
# {
#     "ServerIp": "3.3.3.3",
#     "ServerPass": "6c8hua7A3Sc5ZS6aoviDPFbOt04XgOIrTPnY2F5Or0pt1jGSF6DQTisPQFQRsxuo",
#     "@odata.id": "/redfish/v1/SFSSApp/RadiusServers('3.3.3.3')",
#     "@odata.type": "#RadiusServers.RadiusServers",
#     "@odata.context": "/redfish/v1/SFSSApp/$metadata#RadiusServers/RadiusServers/$entity"
# },
# {
#     "ServerIp": "1.1.1.1",
#     "ServerPass": "+h7vBfukV+dybhSrCC1dG5bamPlNBEZqW2iBIXCLaHf2jlEd44ToqI5y63vCwFbR",
#     "@odata.id": "/redfish/v1/SFSSApp/RadiusServers('1.1.1.1')",
#     "@odata.type": "#RadiusServers.RadiusServers",
#     "@odata.context": "/redfish/v1/SFSSApp/$metadata#RadiusServers/RadiusServers/$entity"
# },
# {
#     "ServerIp": "2.3.4.5",
#     "ServerPass": "+05QvIgOaO5zsQ6kY4o6/SL3xBk4Wif81ZpONVPqUSiPIl86qrvqkQPwmlNnRdu1",
#     "@odata.id": "/redfish/v1/SFSSApp/RadiusServers('2.3.4.5')",
#     "@odata.type": "#RadiusServers.RadiusServers",
#     "@odata.context": "/redfish/v1/SFSSApp/$metadata#RadiusServers/RadiusServers/$entity"
# }
# ]
#
- name: security auth create
  dellemc.sfss.security_authentication:
    config:
      - authentication_sequence: ["local"]
        authentication_servers:
        - authentication_type: "radius"
          server_ip: "1.1.1.1"
          password: "xxxx"
    state: deleted
#
# After state:
# ------------
# redfish/v1/SFSSApp/RadiusServers
# "RadiusServers": [
# {
#   "ServerIp": "3.3.3.3",
#   "ServerPass": "6c8hua7A3Sc5ZS6aoviDPFbOt04XgOIrTPnY2F5Or0pt1jGSF6DQTisPQFQRsxuo",
#   "@odata.id": "/redfish/v1/SFSSApp/RadiusServers('3.3.3.3')",
#   "@odata.type": "#RadiusServers.RadiusServers",
#   "@odata.context": "/redfish/v1/SFSSApp/$metadata#RadiusServers/RadiusServers/$entity"
# },
# {
#   "ServerIp": "2.3.4.5",
#   "ServerPass": "+05QvIgOaO5zsQ6kY4o6/SL3xBk4Wif81ZpONVPqUSiPIl86qrvqkQPwmlNnRdu1",
#   "@odata.id": "/redfish/v1/SFSSApp/RadiusServers('2.3.4.5')",
#   "@odata.type": "#RadiusServers.RadiusServers",
#   "@odata.context": "/redfish/v1/SFSSApp/$metadata#RadiusServers/RadiusServers/$entity"
# }
# ]

# Using deleted
#
# Before state:
# -------------
#
# redfish/v1/SFSSApp/RadiusServers
# "RadiusServers": [
# {
#   "ServerIp": "10.1.1.1",
#   "ServerPass": "2+YGyhuqn5Kn3TWYbwZu+yWtLBhM97+pAsMG+L/Sd1qTJdSwBq7i0PM1RNW6pmtb",
#   "@odata.id": "/redfish/v1/SFSSApp/RadiusServers('10.1.1.1')",
#   "@odata.type": "#RadiusServers.RadiusServers",
#   "@odata.context": "/redfish/v1/SFSSApp/$metadata#RadiusServers/RadiusServers/$entity"
# },
# {
#   "ServerIp": "21.1.1.1",
#   "ServerPass": "+RgniIfG21lRvtWqTZEAZKm3ParQWdtFYf+g6YUWavhVpPfUxPcEoO+ntE43A6yq",
#   "@odata.id": "/redfish/v1/SFSSApp/RadiusServers('21.1.1.1')",
#   "@odata.type": "#RadiusServers.RadiusServers",
#   "@odata.context": "/redfish/v1/SFSSApp/$metadata#RadiusServers/RadiusServers/$entity"
# },
# {
#   "ServerIp": "2.3.4.5",
#   "ServerPass": "+05QvIgOaO5zsQ6kY4o6/SL3xBk4Wif81ZpONVPqUSiPIl86qrvqkQPwmlNnRdu1",
#   "@odata.id": "/redfish/v1/SFSSApp/RadiusServers('2.3.4.5')",
#   "@odata.type": "#RadiusServers.RadiusServers",
#   "@odata.context": "/redfish/v1/SFSSApp/$metadata#RadiusServers/RadiusServers/$entity"
# },
# {
#   "ServerIp": "1.1.1.1",
#   "ServerPass": "vDYv9ApwdJFVeoFvu8BfL1FuA44ivP1+yfgP9f4wRSln6/9c+XRC1WMPaHE6wsFD",
#   "@odata.id": "/redfish/v1/SFSSApp/RadiusServers('1.1.1.1')",
#   "@odata.type": "#RadiusServers.RadiusServers",
#   "@odata.context": "/redfish/v1/SFSSApp/$metadata#RadiusServers/RadiusServers/$entity"
# },
# {
#   "ServerIp": "3.3.3.3",
#   "ServerPass": "6c8hua7A3Sc5ZS6aoviDPFbOt04XgOIrTPnY2F5Or0pt1jGSF6DQTisPQFQRsxuo",
#   "@odata.id": "/redfish/v1/SFSSApp/RadiusServers('3.3.3.3')",
#   "@odata.type": "#RadiusServers.RadiusServers",
#   "@odata.context": "/redfish/v1/SFSSApp/$metadata#RadiusServers/RadiusServers/$entity"
# }
# ]

#redfish/v1/SFSSApp/TacacsServers
# "TacacsServers": [
# {
#   "ServerIp": "2.2.2.2",
#   "ServerPass": "MkNgvF14iIDJXGxfAnDABawtiFQ6/rLrahcr1d2KaQNt9i4NVAOQxwieDYYYl6y+",
#   "@odata.id": "/redfish/v1/SFSSApp/TacacsServers('2.2.2.2')",
#   "@odata.type": "#TacacsServers.TacacsServers",
#   "@odata.context": "/redfish/v1/SFSSApp/$metadata#TacacsServers/TacacsServers/$entity"
# },
# {
#   "ServerIp": "60.8.8.8",
#   "ServerPass": "iBQbXHDIVRkfeYA2NWQj3b/yvUFmWnerNttUxQQK2XNByc/CqXQSne+Wyjh9qck1",
#   "@odata.id": "/redfish/v1/SFSSApp/TacacsServers('60.8.8.8')",
#   "@odata.type": "#TacacsServers.TacacsServers",
#   "@odata.context": "/redfish/v1/SFSSApp/$metadata#TacacsServers/TacacsServers/$entity"
# },
# {
#   "ServerIp": "11.1.1.1",
#   "ServerPass": "DRRUDxiwdzYNLH+2DyxoR7qR07RYUfVZcwSWGdeHPo/8b8Ykr6YjJ7DhpOpMaV09",
#   "@odata.id": "/redfish/v1/SFSSApp/TacacsServers('11.1.1.1')",
#   "@odata.type": "#TacacsServers.TacacsServers",
#   "@odata.context": "/redfish/v1/SFSSApp/$metadata#TacacsServers/TacacsServers/$entity"
# }
# ]
- name: security auth create
  dellemc.sfss.security_authentication:
    config: []
    state: deleted
#
# After state:
# ------------
#redfish/v1/SFSSApp/RadiusServers
# {
#   "RadiusServers@odata.count": 0,
#   "@odata.id": "/redfish/v1/SFSSApp/RadiusServers?$expand=RadiusServers",
#   "@odata.context": "/redfish/v1/SFSSApp/$metadata#RadiusServers",
#   "@odata.type": "#RadiusServersCollection.RadiusServersCollection"
# }
#redfish/v1/SFSSApp/TacacsServers
# {
#   "TacacsServers@odata.count": 0,
#   "@odata.id": "/redfish/v1/SFSSApp/TacacsServers?$expand=TacacsServers",
#   "@odata.context": "/redfish/v1/SFSSApp/$metadata#TacacsServers",
#   "@odata.type": "#TacacsServersCollection.TacacsServersCollection"
# }
# Using merged
#
# Before state:
# -------------
#
# redfish/v1/SFSSApp/RadiusServers
# "RadiusServers": [
# {
#   "ServerIp": "3.3.3.3",
#   "ServerPass": "6c8hua7A3Sc5ZS6aoviDPFbOt04XgOIrTPnY2F5Or0pt1jGSF6DQTisPQFQRsxuo",
#   "@odata.id": "/redfish/v1/SFSSApp/RadiusServers('3.3.3.3')",
#   "@odata.type": "#RadiusServers.RadiusServers",
#   "@odata.context": "/redfish/v1/SFSSApp/$metadata#RadiusServers/RadiusServers/$entity"
# },
# {
#   "ServerIp": "2.3.4.5",
#   "ServerPass": "+05QvIgOaO5zsQ6kY4o6/SL3xBk4Wif81ZpONVPqUSiPIl86qrvqkQPwmlNnRdu1",
#   "@odata.id": "/redfish/v1/SFSSApp/RadiusServers('2.3.4.5')",
#   "@odata.type": "#RadiusServers.RadiusServers",
#   "@odata.context": "/redfish/v1/SFSSApp/$metadata#RadiusServers/RadiusServers/$entity"
# }
# ]
#
- name: security auth create
  dellemc.sfss.security_authentication:
    config:
      - authentication_sequence: ["local"]
        authentication_servers:
        - authentication_type: "radius"
          server_ip: "1.1.1.1"
          password: "xxxx"
#
# After state:
# ------------
# redfish/v1/SFSSApp/RadiusServers
# "RadiusServers": [
# {
#   "ServerIp": "3.3.3.3",
#   "ServerPass": "6c8hua7A3Sc5ZS6aoviDPFbOt04XgOIrTPnY2F5Or0pt1jGSF6DQTisPQFQRsxuo",
#   "@odata.id": "/redfish/v1/SFSSApp/RadiusServers('3.3.3.3')",
#   "@odata.type": "#RadiusServers.RadiusServers",
#   "@odata.context": "/redfish/v1/SFSSApp/$metadata#RadiusServers/RadiusServers/$entity"
# },
# {
#   "ServerIp": "1.1.1.1",
#   "ServerPass": "vDYv9ApwdJFVeoFvu8BfL1FuA44ivP1+yfgP9f4wRSln6/9c+XRC1WMPaHE6wsFD",
#   "@odata.id": "/redfish/v1/SFSSApp/RadiusServers('1.1.1.1')",
#   "@odata.type": "#RadiusServers.RadiusServers",
#   "@odata.context": "/redfish/v1/SFSSApp/$metadata#RadiusServers/RadiusServers/$entity"
# },
# {
#   "ServerIp": "2.3.4.5",
#   "ServerPass": "+05QvIgOaO5zsQ6kY4o6/SL3xBk4Wif81ZpONVPqUSiPIl86qrvqkQPwmlNnRdu1",
#   "@odata.id": "/redfish/v1/SFSSApp/RadiusServers('2.3.4.5')",
#   "@odata.type": "#RadiusServers.RadiusServers",
#   "@odata.context": "/redfish/v1/SFSSApp/$metadata#RadiusServers/RadiusServers/$entity"
# }
# ]

"""
RETURN = """
before:
  description: The configuration prior to the model invocation.
  returned: always
  sample: ['ServerIp: 2.3.4.5', 'ServerPass: +05QvIgOaO5zsQ6kY4o6/SL3xBk4Wif81ZpONVPqUSiPIl86qrvqkQPwmlNnRdu1']
  type: list

after:
  description: The resulting configuration model invocation.
  returned: when changed
  sample: ['ServerIp: 2.3.4.5', 'ServerPass: +05QvIgOaO5zsQ6kY4o6/SL3xBk4Wif81ZpONVPqUSiPIl86qrvqkQPwmlNnRdu1']
  type: list

commands:
  description: The set of commands pushed to the remote device.
  returned: always
  type: list
  sample: ['command 1', 'command 2', 'command 3']
"""


from ansible.module_utils.basic import AnsibleModule
from ansible_collections.dellemc.sfss.plugins.module_utils.network.sfss.argspec.security_authentication.security_authentication import (
    Security_authenticationArgs
)
from ansible_collections.dellemc.sfss.plugins.module_utils.network.sfss.config.security_authentication.security_authentication import Security_authentication


def main():
    """
    Main entry point for module execution

    :returns: the result form module invocation
    """
    module = AnsibleModule(argument_spec=Security_authenticationArgs.argument_spec,
                           supports_check_mode=True)

    result = Security_authentication(module).execute_module()
    module.exit_json(**result)


if __name__ == '__main__':
    main()
