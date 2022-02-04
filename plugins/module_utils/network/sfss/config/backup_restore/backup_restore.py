#
# -*- coding: utf-8 -*-
# Copyright 2021 Dell Inc. or its subsidiaries. All Rights Reserved
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
"""
The sfss_backup_restore class
It is in this file where the current configuration (as dict)
is compared to the provided configuration (as dict) and the command set
necessary to bring the current configuration to it's desired end-state is
created
"""
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type
from ansible_collections.dellemc.sfss.plugins.module_utils.network.sfss.facts.facts import Facts
from ansible_collections.dellemc.sfss.plugins.module_utils.network.sfss.config.base.sfss_config_base import (
    StfsConfigBase,
)
from ansible_collections.dellemc.sfss.plugins.module_utils.network.sfss.utils.debug import debug
from ansible_collections.dellemc.sfss.plugins.module_utils.network.sfss.constants.urls import (
    BACKUP_CREATE_URL,
    RESTORE_CREATE_URL
)


class Backup_restore(StfsConfigBase):
    """
    The sfss_backup_restore class
    """

    gather_subset = [
        '!all',
        '!min',
    ]

    gather_network_resources = [
        'backup_restore',
    ]

    def __init__(self, module):
        super(Backup_restore, self).__init__(module)
        self.resource_name = 'backup_restore'
        self.test_keys = []

    def build_delete_all_requests(self, commands):
        return [], []

    def build_delete_requests(self, commands, want, have, diff):
        return [], []

    def build_create_request(self, have, want):
        requests = []
        location = want.get('imageserver_location')
        password = want.get('imageserver_password')
        user_name = want.get('imageserver_username')
        transport_type = want.get('transport_type')
        operation_type = want.get('operation_type')
        if operation_type == 'backup':
            url = BACKUP_CREATE_URL
        elif operation_type == 'restore':
            url = RESTORE_CREATE_URL
        method = "POST"
        payload = {
            'ImageServerLocation': location,
            'ImageServerPassword': password,
            'ImageServerUserName': user_name,
            'TransportType': transport_type
        }
        request = {
            "method": method,
            "path": url,
            "data": payload,
        }
        requests.append(request)
        return requests

    def build_update_requests(self, have, matched_have, want):
        requests = []
        location = want.get('imageserver_location')
        password = want.get('imageserver_password')
        user_name = want.get('imageserver_username')
        transport_type = want.get('transport_type')
        operation_type = want.get('operation_type')
        if operation_type == 'backup':
            url = BACKUP_CREATE_URL
        elif operation_type == 'restore':
            url = RESTORE_CREATE_URL
        method = "POST"
        payload = {
            'ImageServerLocation': location,
            'ImageServerPassword': password,
            'ImageServerUserName': user_name,
            'TransportType': transport_type
        }
        request = {
            "method": method,
            "path": url,
            "data": payload,
        }
        requests.append(request)
        return requests

    def resource_id(self, global_policy):
        return True
