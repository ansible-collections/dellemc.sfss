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
The module file for sfss_app_images
"""

from __future__ import absolute_import, division, print_function
__metaclass__ = type

DOCUMENTATION = """
---
module: sfss_app_images
version_added: 1.0.0
notes:
- Idempotent is supported.
- Supports C(check_mode).
short_description: Manage SFSS APP images
description:
  - This module is used to manage SFSS application images. Use this module to download images from the image file server using HTTP, HTTPS, FTP, or SCP.
author: Mohamed Javeed (@javeedf)
options:
  config:
    description: This module is used to manage SFSS application images.
    type: list
    elements: dict
    suboptions:
      version:
        description:
          - Image version.
        type: str
      image_id:
        description:
          - Unique Id assigned to image on creation.
        type: str
      status:
        description:
          - Status of the download process.
        type: str
      fileserver_username:
        description:
          - Username to access the image file server.
        type: str
      fileserver_password:
        description:
          - Password to access the image file server.
        type: str
      fileserver_host:
        description:
          - IP address of the image file server.
        type: str
      image_file:
        description:
          - Path location of the image file.
        type: str
      status_message:
        description:
          - Status message.
        type: str
      update_password:
        description:
          - Choice to update the password.
        type: bool
        default: False
      transport_type:
        description:
          - Transport type.
        type: str
        required: True
        choices:
        - scp
        - sftp
        - http
        - https
        - None
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
#redfish/v1/SFSSApp/SFSSImages?$expand=SFSSImages
# "SFSSImages":[
# {
#   "ImageServerLocation": "100.94.72.166:/home/dell/temp_images/sfss-1.2.0.deb",
#   "StatusMessage": "Download Started",
#   "ImageServerPassword": "force10",
#   "Status": "InProgress",
#   "TransportType": "SCP",
#   "ImageServerUserName": "dell",
#   "Version": "1.2.0",
#   "@odata.id": "/redfish/v1/SFSSApp/SFSSImages('1.2.0')",
#   "@odata.type": "#SFSSImages.SFSSImages",
#   "@odata.context": "/redfish/v1/SFSSApp/$metadata#SFSSImages/SFSSImages/$entity"
# },
# {
#     "StatusMessage": "Added during initializing",
#     "Status": "Success",
#     "Version": "1.0.0",
#     "@odata.id": "/redfish/v1/SFSSApp/SFSSImages('1.0.0')",
#     "@odata.type": "#SFSSImages.SFSSImages",
#     "@odata.context": "/redfish/v1/SFSSApp/$metadata#SFSSImages/SFSSImages/$entity"
# }
# ]
- name: Stfs App image create
  dellemc.sfss.app_images:
    config:
    - fileserver_host: 100.94.72.166
      fileserver_password: force10
      fileserver_username: dell
      image_file: /home/dell/temp_images1/sfss-1.2.0.deb
      transport_type: scp
      version: 1.2.0
    state: deleted
#
# After state:
# -------------
#
#redfish/v1/SFSSApp/SFSSImages?$expand=SFSSImages
# "SFSSImages": [
# {
#   "StatusMessage": "Added during initializing",
#   "Status": "Success",
#   "Version": "1.0.0",
#   "@odata.id": "/redfish/v1/SFSSApp/SFSSImages('1.0.0')",
#   "@odata.type": "#SFSSImages.SFSSImages",
#   "@odata.context": "/redfish/v1/SFSSApp/$metadata#SFSSImages/SFSSImages/$entity"
# }
# ]
#
# Using deleted
#
# Before state:
# -------------
#
#redfish/v1/SFSSApp/SFSSImages?$expand=SFSSImages
# "SFSSImages": [
# {
#   "ImageServerLocation": "100.94.72.166:/home/dell/temp_images/sfss-1.2.0.deb",
#   "StatusMessage": "Download Started",
#   "ImageServerPassword": "force10",
#   "Status": "InProgress",
#   "TransportType": "SCP",
#   "ImageServerUserName": "dell",
#   "Version": "1.2.0",
#   "@odata.id": "/redfish/v1/SFSSApp/SFSSImages('1.2.0')",
#   "@odata.type": "#SFSSImages.SFSSImages",
#   "@odata.context": "/redfish/v1/SFSSApp/$metadata#SFSSImages/SFSSImages/$entity"
# },
# {
#   "StatusMessage": "Added during initializing",
#   "Status": "Success",
#   "Version": "1.0.0",
#   "@odata.id": "/redfish/v1/SFSSApp/SFSSImages('1.0.0')",
#   "@odata.type": "#SFSSImages.SFSSImages",
#   "@odata.context": "/redfish/v1/SFSSApp/$metadata#SFSSImages/SFSSImages/$entity"
# }
# ]
- name: Stfs App image create
  dellemc.sfss.app_images:
    config: []
    state: deleted
#
# After state:
# -------------
#
#redfish/v1/SFSSApp/SFSSImages?$expand=SFSSImages
# "SFSSImages": [
# {
#   "StatusMessage": "Added during initializing",
#   "Status": "Success",
#   "Version": "1.0.0",
#   "@odata.id": "/redfish/v1/SFSSApp/SFSSImages('1.0.0')",
#   "@odata.type": "#SFSSImages.SFSSImages",
#   "@odata.context": "/redfish/v1/SFSSApp/$metadata#SFSSImages/SFSSImages/$entity"
# }
# ]
# Using merged
#
# Before state:
# -------------
#
#redfish/v1/SFSSApp/SFSSImages?$expand=SFSSImages
# "SFSSImages": [
# {
#   "StatusMessage": "Added during initializing",
#   "Status": "Success",
#   "Version": "1.0.0",
#   "@odata.id": "/redfish/v1/SFSSApp/SFSSImages('1.0.0')",
#   "@odata.type": "#SFSSImages.SFSSImages",
#   "@odata.context": "/redfish/v1/SFSSApp/$metadata#SFSSImages/SFSSImages/$entity"
# }
# ]
- name: Stfs App image create
  dellemc.sfss.app_images:
    config:
    - fileserver_host: 100.94.72.166
      fileserver_password: force10
      fileserver_username: dell
      image_file: /home/dell/temp_images1/sfss-1.2.0.deb
      transport_type: scp
      version: 1.2.0

#
# After state:
# -------------
#
#redfish/v1/SFSSApp/SFSSImages?$expand=SFSSImages
# "SFSSImages": [
# {
#   "ImageServerLocation": "100.94.72.166:/home/dell/temp_images/sfss-1.2.0.deb",
#   "StatusMessage": "Download Started",
#   "ImageServerPassword": "force10",
#   "Status": "InProgress",
#   "TransportType": "SCP",
#   "ImageServerUserName": "dell",
#   "Version": "1.2.0",
#   "@odata.id": "/redfish/v1/SFSSApp/SFSSImages('1.2.0')",
#   "@odata.type": "#SFSSImages.SFSSImages",
#   "@odata.context": "/redfish/v1/SFSSApp/$metadata#SFSSImages/SFSSImages/$entity"
# },
# {
#   "StatusMessage": "Added during initializing",
#   "Status": "Success",
#   "Version": "1.0.0",
#   "@odata.id": "/redfish/v1/SFSSApp/SFSSImages('1.0.0')",
#   "@odata.type": "#SFSSImages.SFSSImages",
#   "@odata.context": "/redfish/v1/SFSSApp/$metadata#SFSSImages/SFSSImages/$entity"
# }
# ]


"""
RETURN = """
before:
  description: The configuration prior to the model invocation.
  returned: always
  sample: ['StatusMessage: Added during initializing', 'Status: Success', 'Version: 1.0.0']
  type: list

after:
  description: The resulting configuration model invocation.
  returned: when changed
  sample: ['StatusMessage: Added during initializing', 'Status: Success', 'Version: 1.0.0']
  type: list

commands:
  description: The set of commands pushed to the remote device.
  returned: always
  type: list
  sample: ['command 1', 'command 2', 'command 3']
"""


from ansible.module_utils.basic import AnsibleModule
from ansible_collections.dellemc.sfss.plugins.module_utils.network.sfss.argspec.app_images.app_images import App_imagesArgs
from ansible_collections.dellemc.sfss.plugins.module_utils.network.sfss.config.app_images.app_images import App_images


def main():
    """
    Main entry point for module execution

    :returns: the result form module invocation
    """
    module = AnsibleModule(argument_spec=App_imagesArgs.argument_spec,
                           supports_check_mode=True)

    result = App_images(module).execute_module()
    module.exit_json(**result)


if __name__ == '__main__':
    main()
