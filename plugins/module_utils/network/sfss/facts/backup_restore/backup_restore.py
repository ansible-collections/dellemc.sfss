#
# -*- coding: utf-8 -*-
# Copyright 2021 Dell Inc. or its subsidiaries. All Rights Reserved
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
"""
The sfss backup_restore fact class
It is in this file the configuration is collected from the device
for a given resource, parsed, and the facts tree is populated
based on the configuration.
"""
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type
import re
from copy import deepcopy
from ansible_collections.dellemc.sfss.plugins.module_utils.network.sfss.argspec.backup_restore.backup_restore import Backup_restoreArgs
from ansible_collections.dellemc.sfss.plugins.module_utils.network.sfss.facts.base.sfss_facts_base import (
    StfsFactsBase,
)
from ansible_collections.dellemc.sfss.plugins.module_utils.network.sfss.utils.debug import debug
from ansible_collections.dellemc.sfss.plugins.module_utils.network.sfss.utils.utils import (
    send_requests,
    get_instances,
)
from ansible_collections.dellemc.sfss.plugins.module_utils.network.sfss.constants.urls import (
    BACKUP_URL,
    RESTORE_URL
)
from ansible.module_utils.connection import ConnectionError

GET = "get"


class Backup_restoreFacts(StfsFactsBase):
    """ The sfss backup fact class
    """

    def __init__(self, module):
        self.argument_spec = Backup_restoreArgs.argument_spec
        self.resource_name = "backup_restore"
        super(Backup_restoreFacts, self).__init__(module)

    def get_all_data(self):
        instances = get_instances(self)
        data = self.get_resource_data()
        return data

    def get_resource_data(self):
        requests = [
            {"path": BACKUP_URL, "method": GET},
            {"path": RESTORE_URL, "method": GET}]

        responses = send_requests(self, requests)
        ret = []
        for response in responses:
            if response and response[1].get('Backups'):
                for backup in response[1].get('Backups'):
                    backups = self.transform_config(backup, 'backup')
                    ret.append(backups)
            elif response and response[1].get('Restores'):
                for restore in response[1].get('Restores'):
                    restores = self.transform_config(restore, 'restore')
                    ret.append(restores)
        return ret

    def transform_config(self, data, operation_type):
        location = data.get('ImageServerLocation')
        password = data.get('ImageServerPassword')
        user_name = data.get('ImageServerUserName')
        transport_type = data.get('TransportType')
        backup = {
            'imageserver_location': location,
            'imageserver_password': password,
            'imageserver_username': user_name,
            'transport_type': transport_type,
            'operation_type': operation_type
        }
        return backup
