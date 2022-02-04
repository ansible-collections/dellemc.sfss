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
The arg spec for the sfss_backup_restore module
"""
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type


class Backup_restoreArgs(object):  # pylint: disable=R0903
    """The arg spec for the sfss_backup_restore module
    """

    def __init__(self, **kwargs):
        pass

    argument_spec = {'config': {'elements': 'dict',
                                'options': {'imageserver_location': {'required': True,
                                                                     'type': 'str'},
                                            'imageserver_password': {'required': True,
                                                                     'type': 'str', 'no_log': True},
                                            'imageserver_username': {'required': True,
                                                                     'type': 'str'},
                                            'transport_type': {'choices': ['SCP',
                                                                           'HTTP',
                                                                           'HTTPS',
                                                                           'SFTP'],
                                                               'default': 'SCP',
                                                               'type': 'str'},
                                            'operation_type': {'choices': ['backup', 'restore'],
                                                               'required': True,
                                                               'type': 'str'}},
                                'type': 'list'},
                     'state': {'choices': ['merged'],
                               'default': 'merged',
                               'type': 'str'}}  # pylint: disable=C0301
