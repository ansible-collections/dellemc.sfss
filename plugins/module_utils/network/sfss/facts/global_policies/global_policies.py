#
# -*- coding: utf-8 -*-
# Copyright 2021 Dell Inc. or its subsidiaries. All Rights Reserved
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
"""
The sfss global_policies fact class
It is in this file the configuration is collected from the device
for a given resource, parsed, and the facts tree is populated
based on the configuration.
"""
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type
import re
from copy import deepcopy

from ansible_collections.ansible.netcommon.plugins.module_utils.network.common import (
    utils,
)
from ansible_collections.dellemc.sfss.plugins.module_utils.network.sfss.argspec.global_policies.global_policies import Global_policiesArgs
from ansible_collections.dellemc.sfss.plugins.module_utils.network.sfss.facts.base.sfss_facts_base import (
    StfsFactsBase,
)
from ansible_collections.dellemc.sfss.plugins.module_utils.network.sfss.utils.debug import debug
from ansible_collections.dellemc.sfss.plugins.module_utils.network.sfss.utils.utils import (
    send_requests,
    get_instances,
)
from ansible_collections.dellemc.sfss.plugins.module_utils.network.sfss.constants.tranformers import (
    transform_cdc_state,
)
from ansible_collections.dellemc.sfss.plugins.module_utils.network.sfss.constants.urls import (
    GLOBAL_POLICIES_URL,
)
from ansible.module_utils.connection import ConnectionError
GET = "get"


class Global_policiesFacts(StfsFactsBase):
    """ The sfss global_policies fact class
    """
    def __init__(self, module):
        self.argument_spec = Global_policiesArgs.argument_spec
        self.resource_name = "global_policies"
        super(Global_policiesFacts, self).__init__(module)

    def get_resource_data(self, instance_id):
        requests = [{"path": GLOBAL_POLICIES_URL.format(instance_id=instance_id),
                     "method": GET}]
        responses = send_requests(self, requests)
        global_policies = []
        for response in responses:
            if response:
                global_policies.append(self.transform_config(response[1], instance_id))
        return global_policies

    def transform_config(self, data, instance_id):
        global_policy = {}
        zoning_policy = data.get('ZoningPolicy')
        NameServerEntityPurgeTOV = data.get('NameServerEntityPurgeTOV')
        global_policy.update({
            "instance_id": instance_id,
            "zoning_policy": transform_cdc_state(zoning_policy),
            "NameServerEntityPurgeTOV": NameServerEntityPurgeTOV
        })
        return global_policy
