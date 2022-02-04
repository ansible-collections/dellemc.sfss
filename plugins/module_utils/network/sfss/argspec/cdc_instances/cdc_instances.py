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
The arg spec for the sfss_cdc_instances module
"""
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type


class Cdc_instancesArgs(object):  # pylint: disable=R0903
    """The arg spec for the sfss_cdc_instances module
    """

    def __init__(self, **kwargs):
        pass

    argument_spec = {'config': {'elements': 'dict',
                                'options': {'admin_state': {'type': 'bool', 'required': True},
                                            'discovery_svc_admin_state': {'type': 'bool', 'required': True},
                                            'instance_id': {'required': True, 'type': 'int'},
                                            'interfaces': {'elements': 'dict',
                                                           'options': {'name': {'required': True,
                                                                                'type': 'str'}},
                                                           'type': 'list'}},
                                'type': 'list'},
                     'state': {'choices': ['merged', 'deleted'],
                               'default': 'merged',
                               'type': 'str'}}  # pylint: disable=C0301
