#
# -*- coding: utf-8 -*-
# Copyright 2021 Dell Inc. or its subsidiaries. All Rights Reserved
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
"""
The sfss app_image_upgrade fact class
It is in this file the configuration is collected from the device
for a given resource, parsed, and the facts tree is populated
based on the configuration.
"""
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type
from ansible_collections.dellemc.sfss.plugins.module_utils.network.sfss.utils.debug import debug
from ansible_collections.ansible.netcommon.plugins.module_utils.network.common import (
    utils,
)
from ansible_collections.dellemc.sfss.plugins.module_utils.network.sfss.sfss import (
    to_request,
    edit_config
)
from ansible_collections.dellemc.sfss.plugins.module_utils.network.sfss.facts.base.sfss_facts_base import (
    StfsFactsBase,
)
from ansible_collections.dellemc.sfss.plugins.module_utils.network.sfss.argspec.app_image_upgrade.app_image_upgrade import App_image_upgradeArgs
from ansible_collections.dellemc.sfss.plugins.module_utils.network.sfss.constants.urls import (
    SFSS_APP_GET,
)

GET = "get"


class App_image_upgradeFacts(StfsFactsBase):
    """ The sfss app_image_upgrade fact class
    """

    def __init__(self, module):
        self.argument_spec = App_image_upgradeArgs.argument_spec
        self.resource_name = "app_image_upgrade"
        super(App_image_upgradeFacts, self).__init__(module)

    def get_all_data(self):
        ret = self.get_app_image_version()
        debug("App ret", ret)
        return ret

    def populate_facts(self, connection, ansible_facts, data=None):
        """ Populate the facts for mclag
        :param connection: the device connection
        :param ansible_facts: Facts dictionary
        :param data: previously collected conf
        :rtype: dictionary
        :returns: facts
        """
        objs = None
        if not data:
            data = self.get_all_data()
        if data:
            objs = self.render_config(self.generated_spec, data)
        facts = {}
        if objs:
            params = utils.validate_config(self.argument_spec, {'config': objs})
            facts[self.resource_name] = params['config']

        ansible_facts['ansible_network_resources'].update(facts)
        return ansible_facts

    def get_app_image_version(self):
        path = SFSS_APP_GET
        requests = [{"path": path, "method": GET}]
        responses = []

        try:
            responses = edit_config(self._module, to_request(self._module, requests))
        except ConnectionError as exc:
            self._module.fail_json(msg=str(exc), code=exc.code)

        debug("App get", responses[0][1])
        app_images = []
        ret = {}
        if responses and responses[0][1].get('Version'):
            current_version = responses[0][1].get('Version')
            debug("App current_version", responses[0][1].get('Version'))
            ret = {
                "image_version": current_version
            }
            import json
            json_data = json.dumps(ret)
            debug("json_data", json_data)
        return ret
