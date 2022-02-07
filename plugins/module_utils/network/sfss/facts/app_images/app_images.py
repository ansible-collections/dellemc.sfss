#
# -*- coding: utf-8 -*-
# Copyright 2021 Dell Inc. or its subsidiaries. All Rights Reserved
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
"""
The sfss app_images fact class
It is in this file the configuration is collected from the device
for a given resource, parsed, and the facts tree is populated
based on the configuration.
"""
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type
from ansible_collections.dellemc.sfss.plugins.module_utils.network.sfss.argspec.app_images.app_images import App_imagesArgs
from ansible_collections.dellemc.sfss.plugins.module_utils.network.sfss.utils.debug import debug
from ansible_collections.dellemc.sfss.plugins.module_utils.network.sfss.constants.urls import (
    APP_IMAGES_GET_URL,
)
from ansible_collections.dellemc.sfss.plugins.module_utils.network.sfss.facts.base.sfss_facts_base import (
    StfsFactsBase,
)
from ansible_collections.dellemc.sfss.plugins.module_utils.network.sfss.utils.utils import (
    send_requests,
    get_instances,
)

GET = "get"


class App_imagesFacts(StfsFactsBase):
    """ The sfss app_images fact class
    """

    def __init__(self, module):
        self.argument_spec = App_imagesArgs.argument_spec
        self.resource_name = "app_images"
        super(App_imagesFacts, self).__init__(module)

    def get_all_data(self):
        ret = self.get_resource_data()
        debug("get_all_data", ret)
        return ret

    def get_resource_data(self):
        path = APP_IMAGES_GET_URL
        requests = [{"path": path, "method": GET}]
        responses = send_requests(self, requests)

        debug("Images get", responses)
        app_images = []
        if responses and responses[0][1].get('SFSSImages'):
            for app_image in responses[0][1]['SFSSImages']:
                app_images.append(self.transform_config(app_image))

        return app_images

    def transform_config(self, data):
        app_image = {}
        version = data.get('Version')
        image_file_loc = data.get('ImageServerLocation', "")
        image_file = fileserver_host = None
        if ':' in image_file_loc:
            image_file = image_file_loc.split(":")[1]
            fileserver_host = image_file_loc.split(":")[0]

        version = data.get('Version')
        fileserver_username = data.get('ImageServerUserName')
        fileserver_password = data.get('ImageServerPassword')
        transport_type_val = data.get('TransportType')
        transport_type = transport_type_val.lower() if transport_type_val else None
        status = data.get('Status')
        status_message = data.get('StatusMessage')

        app_image.update({
            "fileserver_host": fileserver_host,
            "fileserver_username": fileserver_username,
            "fileserver_password": fileserver_password,
            "image_file": image_file,
            "transport_type": transport_type,
            "status": status,
            "version": version,
            "status_message": status_message
        })
        return app_image
