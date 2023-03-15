#
# -*- coding: utf-8 -*-
# Copyright 2021 Dell Inc. or its subsidiaries. All Rights Reserved
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
"""
The sfss_app_image_upgrade class
It is in this file where the current configuration (as dict)
is compared to the provided configuration (as dict) and the command set
necessary to bring the current configuration to it's desired end-state is
created
"""
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type
from ansible_collections.dellemc.sfss.plugins.module_utils.network.sfss.utils.debug import debug
from ansible_collections.dellemc.sfss.plugins.module_utils.network.sfss.config.base.sfss_config_base import (
    StfsConfigBase,
)
from ansible_collections.dellemc.sfss.plugins.module_utils.network.sfss.constants.urls import (
    SFSS_APP_GET,
)


class App_image_upgrade(StfsConfigBase):
    """
    The sfss_app_image_upgrade class
    """

    gather_subset = [
        '!all',
        '!min',
    ]

    gather_network_resources = [
        'app_image_upgrade',
    ]

    def __init__(self, module):
        super(App_image_upgrade, self).__init__(module)
        self.resource_name = "app_image_upgrade"
        self.test_keys = [{'config': {'image_version': '', 'current_state': ''}}]

    def resource_id(self, app_image):
        return app_image["image_version"]

    def build_create_request(self, have, app):
        url = SFSS_APP_GET
        method = "PUT"
        version = app.get('image_version')
        # To Do in case of Preventing Downgrade of Image
        # have_version = have.get('image_version')
        # version_splitted = version.split(".")
        # have_version_spliited = have_version.split(".")
        # ver_len = len(version_splitted)
        # if ver_len > len(have_version_spliited):
        #     ver_len = len(have_version_spliited)
        # if ver_len > 3:
        #     ver_len = 3
        # for i in range(ver_len):
        #     if int(version_splitted[i]) < int(have_version_spliited[i]):
        #         return []
        # If downgrade condition fails then upgrade the image

        payload = {"Version": version}
        request = {
            "method": method,
            "path": url,
            "data": payload,
        }
        debug("app image request", request)
        return [request]
