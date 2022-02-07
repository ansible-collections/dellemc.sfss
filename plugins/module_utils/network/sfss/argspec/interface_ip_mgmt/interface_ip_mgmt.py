#
# -*- coding: utf-8 -*-
# Copyright 2021 Dell Inc. or its subsidiaries. All Rights Reserved
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

#############################################
#                WARNING                    #
#############################################
#
# This file is auto generated by the resource
#   module builder playbook.
#
# Do not edit this file manually.
#
# Changes to this file will be over written
#   by the resource module builder.
#
# Changes should be made in the model used to
#   generate this file or in the resource module
#   builder template.
#
#############################################

"""
The arg spec for the sfss_interface_ip_mgmt module
"""
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type


class Interface_ip_mgmtArgs(object):  # pylint: disable=R0903
    """The arg spec for the sfss_interface_ip_mgmt module
    """

    def __init__(self, **kwargs):
        pass

    argument_spec = {'config': {'elements': 'dict',
                                'options': {'ipv4_address': {'type': 'str'},
                                            'ipv4_config_type': {'choices': ['manual', 'automatic'],
                                                                 'required': True,
                                                                 'type': 'str'},
                                            'ipv4_gateway': {'type': 'str'},
                                            'ipv4_netmask': {'type': 'int'},
                                            'ipv6_address': {'type': 'str'},
                                            'ipv6_config_type': {'choices': ['manual', 'automatic'],
                                                                 'required': True,
                                                                 'type': 'str'},
                                            'ipv6_gateway': {'type': 'str'},
                                            'ipv6_netmask': {'type': 'int'},
                                            'parent_interface': {'required': True, 'type': 'str'},
                                            'vlan_id': {'type': 'int'}},
                                'type': 'list'},
                     'state': {'choices': ['merged', 'deleted'],
                               'default': 'merged',
                               'type': 'str'}}  # pylint: disable=C0301