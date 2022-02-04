#
# -*- coding: utf-8 -*-
# Copyright 2021 Dell Inc. or its subsidiaries. All Rights Reserved
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
"""
The facts class for sfss
this file validates each subset of facts and selectively
calls the appropriate facts gathering function
"""
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type
from ansible_collections.dellemc.sfss.plugins.module_utils.network.sfss.argspec.facts.facts import FactsArgs
from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.facts.facts import (
    FactsBase,
)
from ansible_collections.dellemc.sfss.plugins.module_utils.network.sfss.facts.endpoints.endpoints import EndpointsFacts
from ansible_collections.dellemc.sfss.plugins.module_utils.network.sfss.facts.zones.zones import ZonesFacts
from ansible_collections.dellemc.sfss.plugins.module_utils.network.sfss.facts.zone_alias.zone_alias import Zone_aliasFacts
from ansible_collections.dellemc.sfss.plugins.module_utils.network.sfss.facts.cdc_instances.cdc_instances import Cdc_instancesFacts
from ansible_collections.dellemc.sfss.plugins.module_utils.network.sfss.facts.security_authentication.security_authentication import (
    Security_authenticationFacts,
)
from ansible_collections.dellemc.sfss.plugins.module_utils.network.sfss.facts.app_images.app_images import App_imagesFacts
from ansible_collections.dellemc.sfss.plugins.module_utils.network.sfss.facts.interface_ip_mgmt.interface_ip_mgmt import Interface_ip_mgmtFacts
from ansible_collections.dellemc.sfss.plugins.module_utils.network.sfss.facts.app_image_upgrade.app_image_upgrade import App_image_upgradeFacts
from ansible_collections.dellemc.sfss.plugins.module_utils.network.sfss.facts.zone_groups.zone_groups import Zone_groupsFacts
from ansible_collections.dellemc.sfss.plugins.module_utils.network.sfss.facts.global_policies.global_policies import Global_policiesFacts
from ansible_collections.dellemc.sfss.plugins.module_utils.network.sfss.facts.backup_restore.backup_restore import Backup_restoreFacts


FACT_LEGACY_SUBSETS = {}
FACT_RESOURCE_SUBSETS = dict(
    endpoints=EndpointsFacts,
    zones=ZonesFacts,
    zone_groups=Zone_groupsFacts,
    zone_alias=Zone_aliasFacts,
    cdc_instances=Cdc_instancesFacts,
    security_authentication=Security_authenticationFacts,
    app_images=App_imagesFacts,
    interface_ip_mgmt=Interface_ip_mgmtFacts,
    app_image_upgrade=App_image_upgradeFacts,
    global_policies=Global_policiesFacts,
    backup_restore=Backup_restoreFacts,
)


class Facts(FactsBase):
    """ The fact class for sfss
    """

    VALID_LEGACY_GATHER_SUBSETS = frozenset(FACT_LEGACY_SUBSETS.keys())
    VALID_RESOURCE_SUBSETS = frozenset(FACT_RESOURCE_SUBSETS.keys())

    def __init__(self, module):
        super(Facts, self).__init__(module)

    def get_facts(self, legacy_facts_type=None, resource_facts_type=None, data=None):
        """ Collect the facts for sfss

        :param legacy_facts_type: List of legacy facts types
        :param resource_facts_type: List of resource fact types
        :param data: previously collected conf
        :rtype: dict
        :return: the facts gathered
        """

        netres_choices = FactsArgs.argument_spec['gather_network_resources'].get('choices', [])
        if self.VALID_RESOURCE_SUBSETS:
            self.get_network_resources_facts(FACT_RESOURCE_SUBSETS, resource_facts_type, data)

        if self.VALID_LEGACY_GATHER_SUBSETS:
            self.get_network_legacy_facts(FACT_LEGACY_SUBSETS, legacy_facts_type)
        return self.ansible_facts, self._warnings
