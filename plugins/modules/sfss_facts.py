#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright 2021 Dell Inc. or its subsidiaries. All Rights Reserved
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
"""
The module file for sfss_facts
"""

from __future__ import absolute_import, division, print_function
__metaclass__ = type

DOCUMENTATION = """
---
module: sfss_facts
version_added: 1.0.0
short_description: Get facts about SFSS devices
description:
  - Collects facts from network devices running the SFSS application.
    This module places the facts gathered in the fact tree keyed by the
    respective resource name.  The facts module will always collect a
    base set of facts from the device and can enable or disable
    collection of additional facts.
author: Mohamed Javeed (@javeedf)
options:
  gather_subset:
    description:
      - When supplied, this argument will restrict the facts collected
        to a given subset. Possible values for this argument include
        all, min, hardware, config, legacy, and interfaces. Can specify a
        list of values to include a larger subset. Values can also be used
        with an initial C(M(!)) to specify that a specific subset should
        not be collected.
    required: false
    default: '!config'
    type: list
    elements: str
  gather_network_resources:
    description:
      - When supplied, this argument will restrict the facts collected
        to a given subset. Possible values for this argument include
        all and the resources like interfaces, vlans etc.
        Can specify a list of values to include a larger subset. Values
        can also be used with an initial C(M(!)) to specify that a
        specific subset should not be collected.
    required: false
    type: list
    elements: str
    choices:
    - all
    - endpoints
    - zone_groups
    - zones
    - zone_alias
    - cdc_instances
    - security_authentication
    - app_images
    - interface_ip_mgmt
    - app_image_upgrade
    - global_policies
    - backup_restore
"""

EXAMPLES = """
# Gather all facts
- sfss_facts:
    gather_subset: all
    gather_network_resources: all

# Collect only the endpoints facts
- sfss_facts:
    gather_subset:
      -!all
      -!min
    gather_network_resources:
    - endpoints
    - zones
    - zone_alias
    - cdc_instances
    - security_authentication
    - app_images
    - interface_ip_mgmt
    - app_image_upgrade

# Do not collect endpoints facts
- sfss_facts:
    gather_network_resources:
    - "!endpoints"

# Collect endpoints and minimal default facts
- sfss_facts:
    gather_subset: min
    gather_network_resources: endpoints
"""

RETURN = """
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.dellemc.sfss.plugins.module_utils.network.sfss.argspec.facts.facts import FactsArgs
from ansible_collections.dellemc.sfss.plugins.module_utils.network.sfss.facts.facts import Facts


def main():
    """
    Main entry point for module execution

    :returns: ansible_facts
    """
    module = AnsibleModule(argument_spec=FactsArgs.argument_spec,
                           supports_check_mode=True)
    warnings = ['default value for `gather_subset` '
                'will be changed to `min` from `!config` v2.11 onwards']

    result = Facts(module).get_facts()

    ansible_facts, additional_warnings = result
    warnings.extend(additional_warnings)

    module.exit_json(ansible_facts=ansible_facts, warnings=warnings)


if __name__ == '__main__':
    main()
