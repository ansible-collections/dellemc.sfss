#
# -*- coding: utf-8 -*-
# Copyright 2021 Dell Inc. or its subsidiaries. All Rights Reserved
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
"""
The sfss_security_authentication class
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
    AUTHENTICATION_SEQUENCE_URL,
    SERVER_DELETE_URL,
    SERVER_CREATE_URL,
)
from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.utils import (
    to_list,
)


class Security_authentication(StfsConfigBase):
    """
    The sfss_security_authentication class
    """

    gather_subset = [
        '!all',
        '!min',
    ]

    gather_network_resources = [
        'security_authentication',
    ]

    def __init__(self, module):
        super(Security_authentication, self).__init__(module)
        self.resource_name = 'security_authentication'
        self.test_keys = [{'config': {'authentication_sequence': '', 'authentication_servers': '', 'authentication_type': '', 'password': '', 'server_ip': ''}}]

    def build_delete_all_requests(self, commands):
        debug("build_delete_all_requests", commands)
        # debug("build_delete_all_requests", commands)
        ret_requests = []
        ret_commands = []
        if commands:
            for security_auth in commands:
                ret_requests.extend(self.build_delete_request_url(security_auth.get('authentication_servers')))
                ret_commands.append(security_auth)

        return ret_commands, ret_requests

    def transform_server_name(self, name):
        if name == 'tacacs':
            return 'TacacsServers'
        else:
            return 'RadiusServers'

    def build_delete_request_url(self, authentication_servers):
        method = "DELETE"
        requests = []
        for server in authentication_servers:
            server_name = self.transform_server_name(server.get('authentication_type'))
            ip = server.get("server_ip")
            url = SERVER_DELETE_URL.format(server_name=server_name, ip=ip)
            request = {
                "method": method,
                "path": url,
            }
            requests.append(request)
        debug("build_delete_request_url", requests)
        return requests

    def build_delete_requests(self, commands, want, have, diff):
        ret_req = []
        ret_command = []
        servers = want[0].get('authentication_servers')
        if servers:
            for server in servers:
                match = self.server_match(server, have[0].get('authentication_servers'))
                if match:
                    ret_req.extend(self.build_delete_request_url([server]))
                    ret_command.append(server)
        return ret_command, ret_req

    def server_match(self, want, have_servers):
        match = False
        auth_type = want.get('authentication_type')
        ip = want.get('server_ip')
        if have_servers:
            for have in have_servers:
                if auth_type == have.get('authentication_type') and ip == have.get('server_ip'):
                    match = True
                    return match
        return match

    def build_update_requests(self, have, matched_have, command):
        requests = []
        ret_command = {}
        have_servers = []
        have_auth_sequence = []
        if have and have[0]:
            have_servers = have[0].get('authentication_servers')
            have_auth_sequence = have[0].get('authentication_sequence')

        want_auth_sequence = command.get('authentication_sequence', [])
        auth_seq_match = self.compare_auth_sequence(have_auth_sequence, want_auth_sequence)

        if not auth_seq_match:
            ret_command.update({"authentication_sequence": want_auth_sequence})
            requests.append(self.build_auth_sequence_request(command))

        want_auth_servers = command.get('authentication_servers')

        auth_server_command = []
        if want_auth_servers:
            for want_auth_server in want_auth_servers:
                match = self.server_match(want_auth_server, have_servers)
                if not match:
                    auth_server_command.append(want_auth_server)
                    requests.append(self.build_server_create_request_url(want_auth_server))

        if auth_server_command:
            ret_command.update({"authentication_servers": auth_server_command})

        return requests

    def compare_auth_sequence(self, have_auth_sequence, want_auth_sequence):
        have_auth_sequence_str = ",".join(have_auth_sequence)
        want_auth_sequence_str = ",".join(want_auth_sequence)
        debug("have_auth_sequence_str", have_auth_sequence_str)
        debug("want_auth_sequence_str", want_auth_sequence_str)
        match = False
        if have_auth_sequence_str == want_auth_sequence_str:
            match = True

        return match

    def build_auth_sequence_request(self, command):
        method = "POST"
        url = AUTHENTICATION_SEQUENCE_URL
        payload = {
            "AuthenticationSequence": command.get('authentication_sequence')
        }
        request = {
            "method": method,
            "path": url,
            "data": payload,
        }

        return request

    def build_server_create_request_url(self, authentication_server):
        method = "POST"
        auth_type = self.transform_server_name(authentication_server.get('authentication_type'))
        url = SERVER_CREATE_URL.format(auth_type=auth_type)
        payload = {
            "ServerIp": authentication_server.get('server_ip'),
            "ServerPass": authentication_server.get('password')
        }

        request = {
            "method": method,
            "path": url,
            "data": payload,
        }
        return request

    # always goes to update
    def resource_id(self, instance):
        return True
