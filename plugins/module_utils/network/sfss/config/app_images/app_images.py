#
# -*- coding: utf-8 -*-
# Copyright 2021 Dell Inc. or its subsidiaries. All Rights Reserved
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
"""
The sfss_app_images class
It is in this file where the current configuration (as dict)
is compared to the provided configuration (as dict) and the command set
necessary to bring the current configuration to it's desired end-state is
created
"""
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type
from ansible_collections.dellemc.sfss.plugins.module_utils.network.sfss.config.base.sfss_config_base import (
    StfsConfigBase,
)
from ansible_collections.dellemc.sfss.plugins.module_utils.network.sfss.utils.debug import debug
from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.utils import (
    to_list,
)
from ansible_collections.dellemc.sfss.plugins.module_utils.network.sfss.facts.facts import Facts
from ansible_collections.dellemc.sfss.plugins.module_utils.network.sfss.constants.urls import (
    APP_IMAGES_BASE_URL,
    APP_IMAGES_UPDATE_URL,
)
from ansible_collections.dellemc.sfss.plugins.module_utils.network.sfss.constants.tranformers import (
    zone_group_id,
)


class App_images(StfsConfigBase):
    """
    The sfss_app_images class
    """

    gather_subset = [
        '!all',
        '!min',
    ]

    gather_network_resources = [
        'app_images',
    ]

    def __init__(self, module):
        super(App_images, self).__init__(module)
        self.resource_name = "app_images"
        self.test_keys = [{'config': {'version': '', 'image_id': '', 'fileserver_host': '', 'fileserver_username': '',
                                      'fileserver_password': '', 'image_file': '', 'transport_type': ''}}]

    def resource_id(self, app_image):
        return app_image.get('image_id')

    def build_delete_all_requests(self, commands):
        ret_requests = []
        ret_commands = []
        if commands:
            for app_image in commands:
                if "1.1.0" in app_image.get('image_id'):
                    continue
                ret_requests.append(self.build_delete_request(app_image))
                ret_commands.append(app_image)

        return ret_commands, ret_requests

    def build_delete_requests(self, commands, want, have, diff):
        debug("build_delete_requests", want)
        ret_requests = []
        ret_commands = []
        if want:
            for app_image in want:
                matched_have = self.matches(app_image, have)
                if matched_have:
                    ret_requests.append(self.build_delete_request(app_image))
                    ret_commands.append(app_image)

        return ret_commands, ret_requests

    def build_create_request(self, have, app_image):
        matched = False
        for have_image in have:
            if (have_image['image_file'] is not None):
                debug("have image_file ", have_image['image_file'])
                debug("app image_file ", app_image['image_file'])
                if (app_image['image_file'] in have_image['image_file'] and app_image['transport_type'] == have_image['transport_type']):
                    debug("matched have", have_image)
                    matched = True
                    break
        if matched:
            return []
        else:
            url = APP_IMAGES_BASE_URL
            method = "POST"
            return self.build_request(url, method, app_image)

    def build_update_requests(self, have, matched_have, app_image):
        want_host = app_image.get('fileserver_host')
        want_username = app_image.get('fileserver_username')
        want_image = app_image.get('image_file')
        want_transport_type = app_image.get('transport_type')
        have_host = matched_have.get('fileserver_host')
        have_username = matched_have.get('fileserver_username')
        have_image = matched_have.get('image_file')
        have_transport_type = matched_have.get('transport_type')
        if (app_image.get('update_password') or want_host != have_host
                or want_username != have_username or want_image != have_image
                or want_transport_type != have_transport_type):
            image_id = app_image.get('image_id')
            url = APP_IMAGES_UPDATE_URL.format(image_id=image_id)
            method = "PUT"
            return self.build_request(url, method, app_image)
        else:
            return []

    def build_request(self, url, method, app_image):
        # version = app_image.get('version')
        fileserver_host = app_image.get('fileserver_host')
        fileserver_username = app_image.get('fileserver_username')
        fileserver_password = app_image.get('fileserver_password')
        image_file = app_image.get('image_file')
        transport_type = app_image.get('transport_type').upper()
        # APP_IMAGE_SERVER_LOCATION = "{fileserver_host}:{image_file}"
        if (transport_type == 'HTTP'):
            APP_IMAGE_SERVER_LOCATION = "http://" + "{fileserver_host}{image_file}"
        elif (transport_type == 'HTTPS'):
            APP_IMAGE_SERVER_LOCATION = "https://" + "{fileserver_host}{image_file}"
        else:
            APP_IMAGE_SERVER_LOCATION = "{fileserver_host}:{image_file}"

        image_server_location = APP_IMAGE_SERVER_LOCATION.format(fileserver_host=fileserver_host, image_file=image_file)

        payload = {"ImageServerUserName": fileserver_username,
                   "ImageServerPassword": fileserver_password,
                   "ImageServerLocation": image_server_location,
                   "TransportType": transport_type}

        request = {
            "method": method,
            "path": url,
            "data": payload,
        }
        debug("app image request", request)
        return [request]

    def build_delete_request(self, app_image):
        image_id = app_image.get('image_id')
        url = APP_IMAGES_UPDATE_URL.format(image_id=image_id)
        method = "DELETE"

        request = {
            "method": method,
            "path": url,
        }
        debug("Zone_group_ delete request", request)
        return request
