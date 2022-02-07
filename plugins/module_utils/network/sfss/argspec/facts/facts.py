#
# -*- coding: utf-8 -*-
# Copyright 2021 Dell Inc. or its subsidiaries. All Rights Reserved
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
"""
The arg spec for the sfss facts module.
"""

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type


class FactsArgs(object):  # pylint: disable=R0903
    """ The arg spec for the sfss facts module
    """

    def __init__(self, **kwargs):
        pass

    choices = [
        'all',
        'endpoints',
        'zone_groups',
        'zones',
        'zone_alias',
        'cdc_instances',
        'security_authentication',
        'app_images',
        'interface_ip_mgmt',
        'app_image_upgrade',
        'global_policies',
        'backup_restore',
    ]

    argument_spec = {
        'gather_subset': dict(default=['!config'], type='list', elements='str'),
        'gather_network_resources': dict(choices=choices,
                                         type='list', elements='str'),
    }
