#
# -*- coding: utf-8 -*-
# Copyright 2021 Dell Inc. or its subsidiaries. All Rights Reserved
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
"""
The sfss cdc_instances fact class
It is in this file the configuration is collected from the device
for a given resource, parsed, and the facts tree is populated
based on the configuration.
"""
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type
from ansible_collections.dellemc.sfss.plugins.module_utils.network.sfss.argspec.cdc_instances.cdc_instances import Cdc_instancesArgs
from ansible_collections.dellemc.sfss.plugins.module_utils.network.sfss.facts.base.sfss_facts_base import (
    StfsFactsBase,
)
from ansible_collections.dellemc.sfss.plugins.module_utils.network.sfss.constants.urls import (
    CDC_SPECIFIC_INSTANCE_URL,
)
from ansible_collections.dellemc.sfss.plugins.module_utils.network.sfss.constants.tranformers import (
    transform_cdc_state,
)
from ansible_collections.dellemc.sfss.plugins.module_utils.network.sfss.utils.utils import (
    send_requests,
)
GET = "get"


class Cdc_instancesFacts(StfsFactsBase):
    """ The sfss cdc_instances fact class
    """

    def __init__(self, module):
        self.argument_spec = Cdc_instancesArgs.argument_spec
        self.resource_name = "cdc_instances"
        super(Cdc_instancesFacts, self).__init__(module)

    def get_resource_data(self, instance_id):
        path = CDC_SPECIFIC_INSTANCE_URL.format(instance_id=instance_id)
        requests = [{"path": path, "method": GET}]
        responses = send_requests(self, requests)

        cdc_instances = []
        for response in responses:
            if response:
                cdc_instances.append(self.transform_config(response[1], instance_id))
        return cdc_instances

    def transform_config(self, data, instance_id):
        cdc_instances = {}
        interfaces = data.get('Interfaces')
        admin_state = data.get('CDCAdminState')
        discovery_svc_admin_state = data.get('DiscoveryStateAdminState')
        interface_names = []
        for interface in interfaces:
            interface_names.append({"name": interface})
        cdc_instances.update({
            "instance_id": instance_id,
            "interfaces": interface_names,
            "admin_state": transform_cdc_state(admin_state),
            "discovery_svc_admin_state": transform_cdc_state(discovery_svc_admin_state)
        })
        return cdc_instances
