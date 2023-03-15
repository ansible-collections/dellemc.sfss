#
# -*- coding: utf-8 -*-
# Copyright 2021 Dell Inc. or its subsidiaries. All Rights Reserved
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
"""
The sfss security_authentication fact class
It is in this file the configuration is collected from the device
for a given resource, parsed, and the facts tree is populated
based on the configuration.
"""
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible_collections.dellemc.sfss.plugins.module_utils.network.sfss.argspec.security_authentication.security_authentication import (
    Security_authenticationArgs,
)
from ansible_collections.dellemc.sfss.plugins.module_utils.network.sfss.sfss import (
    to_request,
    edit_config
)
from ansible_collections.dellemc.sfss.plugins.module_utils.network.sfss.facts.base.sfss_facts_base import (
    StfsFactsBase,
)
from ansible_collections.dellemc.sfss.plugins.module_utils.network.sfss.constants.urls import (
    AUTHENTICATION_SEQUENCE_URL,
    TACACSSERVERS_URL,
    RADIUS_SERVERS_URL
)
from ansible.module_utils.connection import ConnectionError
GET = "get"


class Security_authenticationFacts(StfsFactsBase):
    """ The sfss security_authentication fact class
    """
    def __init__(self, module):
        self.argument_spec = Security_authenticationArgs.argument_spec
        self.resource_name = "security_authentication"
        super(Security_authenticationFacts, self).__init__(module)

    def get_all_data(self):
        data = self.get_resource_data()
        return [data]

    def get_resource_data(self):
        path = AUTHENTICATION_SEQUENCE_URL
        requests = [{"path": path, "method": GET}]
        responses = []

        try:
            responses = edit_config(self._module, to_request(self._module, requests))
        except ConnectionError as exc:
            self._module.fail_json(msg=str(exc), code=exc.code)

        security_auth = {}
        for response in responses:
            if response:
                security_auth.update(self.transform_config(response[1]))
        return security_auth

    def transform_config(self, data):
        security_auth = {}
        authentication_sequence = data.get('AuthenticationSequence')
        authentication_servers = self.get_authentication_servers()
        security_auth.update({
            'authentication_sequence': authentication_sequence,
            'authentication_servers': authentication_servers
        })
        return security_auth

    def get_authentication_servers(self):
        paths = [TACACSSERVERS_URL, RADIUS_SERVERS_URL]
        server_names = ['TacacsServers', 'RadiusServers']
        auth_types = ['tacacs', 'radius']
        auth_servers = []

        for i in range(len(paths)):
            requests = [{"path": paths[i], "method": GET}]
            responses = []

            try:
                responses = edit_config(self._module, to_request(self._module, requests))
            except ConnectionError as exc:
                self._module.fail_json(msg=str(exc), code=exc.code)

            for response in responses:
                if response:
                    servers = response[1].get(server_names[i])
                    if servers:
                        for server in servers:
                            server_path = server.get('@odata.id')
                            server_requests = [{"path": server_path, "method": GET}]
                            server_responses = []
                            try:
                                server_responses = edit_config(self._module, to_request(self._module, server_requests))
                            except ConnectionError as exc:
                                self._module.fail_json(msg=str(exc), code=exc.code)
                            for server_response in server_responses:
                                if server_response:
                                    auth_servers.append(
                                        {
                                            'server_ip': server_response[1].get('ServerIp'),
                                            'password': server_response[1].get('ServerPass'),
                                            'authentication_type': auth_types[i]
                                        }
                                    )
        return auth_servers
