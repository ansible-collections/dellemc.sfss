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
The arg spec for the sfss_endpoints module
"""
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type


class EndpointsArgs(object):  # pylint: disable=R0903
    """The arg spec for the sfss_endpoints module
    """

    def __init__(self, **kwargs):
        pass

    argument_spec = {'config': {'elements': 'dict',
                                'options': {'ddc_activate': {'type': 'bool'},
                                            'instance_id': {'required': True, 'type': 'int'},
                                            'nqn_id': {'type': 'str'},
                                            'port_id': {'type': 'int', 'default': 0, },
                                            'transport_address': {'required': True, 'type': 'str'},
                                            'transport_address_family': {'choices': ['ipv4', 'ipv6'],
                                                                         'required': True,
                                                                         'type': 'str'},
                                            'transport_type': {'choices': ['tcp', 'udp'],
                                                               'default': 'tcp',
                                                               'type': 'str'},
                                            'transport_service_id': {'type': 'str'},
                                            'type': {'choices': ['host', 'subsystem', 'ddc'],
                                                     'required': True,
                                                     'type': 'str'}},
                                'type': 'list'},
                     'state': {'choices': ['merged', 'deleted'],
                               'default': 'merged',
                               'type': 'str'}}  # pylint: disable=C0301
