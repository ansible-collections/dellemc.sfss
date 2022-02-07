#
# -*- coding: utf-8 -*-
# Copyright 2021 Dell Inc. or its subsidiaries. All Rights Reserved
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
"""
The sfss_global_policies class
It is in this file where the current configuration (as dict)
is compared to the provided configuration (as dict) and the command set
necessary to bring the current configuration to it's desired end-state is
created
"""
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type
from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.cfg.base import (
    ConfigBase,
)
from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.utils import (
    to_list,
)
from ansible_collections.dellemc.sfss.plugins.module_utils.network.sfss.facts.facts import Facts
from ansible_collections.dellemc.sfss.plugins.module_utils.network.sfss.config.base.sfss_config_base import (
    StfsConfigBase,
)
from ansible_collections.dellemc.sfss.plugins.module_utils.network.sfss.utils.debug import debug
from ansible_collections.dellemc.sfss.plugins.module_utils.network.sfss.constants.urls import (
    GLOBAL_POLICIES_URL,
    CDC_INSTANCE_MANAGER_URL,
)
from ansible_collections.dellemc.sfss.plugins.module_utils.network.sfss.constants.tranformers import (
    retransform_cdc_state,
)
from ansible_collections.dellemc.sfss.plugins.module_utils.network.sfss.utils.utils import (
    send_requests,
    get_instances
)
from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.utils import (
    to_list,
)


class Global_policies(StfsConfigBase):
    """
    The sfss_global_policies class
    """

    gather_subset = [
        '!all',
        '!min',
    ]

    gather_network_resources = [
        'global_policies',
    ]

    def __init__(self, module):
        super(Global_policies, self).__init__(module)
        self.resource_name = 'global_policies'
        self.test_keys = [{'config': {'instance_id': '', 'zoning_policy': '', 'NameServerEntityPurgeTOV': ''}}]

    def build_delete_all_requests(self, commands):
        return [], []

    def build_delete_requests(self, commands, want, have, diff):
        return [], []

    def build_create_request(self, have, want):
        requests = []
        instance_ids = []
        ids = get_instances(self)
        for instance_id in ids:
            instance_ids.append(instance_id['id'])
        if want['instance_id'] in instance_ids:
            want_zoning_policy = want.get('zoning_policy')
            want_duration = want.get('NameServerEntityPurgeTOV')

            if want_duration is None:
                want_duration = '24Hr'

            url = GLOBAL_POLICIES_URL.format(instance_id=want['instance_id'])
            method = "POST"
            payload = {
                'ZoningPolicy': retransform_cdc_state(want_zoning_policy),
                'NameServerEntityPurgeTOV': want_duration,
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
        want_zoning_policy = want.get('zoning_policy')
        want_duration = want.get('NameServerEntityPurgeTOV')
        matched_have_zoning_policy = matched_have.get('zoning_policy')
        matched_have_duration = matched_have.get('NameServerEntityPurgeTOV')

        debug("Build update: want_zoning policy", want_zoning_policy)
        debug("Build update: want_duration", want_duration)

        if want_duration is None:
            want_duration = matched_have_duration
        if want_zoning_policy is None:
            want_zoning_policy = matched_have_zoning_policy

        if want_zoning_policy != matched_have_zoning_policy or want_duration != matched_have_duration:
            url = GLOBAL_POLICIES_URL.format(instance_id=want['instance_id'])
            method = "POST"
            payload = {
                'ZoningPolicy': retransform_cdc_state(want_zoning_policy),
                'NameServerEntityPurgeTOV': want_duration,
            }
            request = {
                "method": method,
                "path": url,
                "data": payload,
            }
            requests.append(request)
        return requests

    def resource_id(self, global_policy):
        return global_policy["instance_id"]
