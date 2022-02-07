from __future__ import (absolute_import, division, print_function)
__metaclass__ = type
import json

from ansible.module_utils._text import to_text
from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.utils import to_list, ComplexList
from ansible.module_utils.connection import Connection, ConnectionError
from ansible_collections.dellemc.sfss.plugins.module_utils.network.sfss.utils.debug import debug


def get_connection(module):
    if hasattr(module, "_sfss_connection"):
        return module._sfss_connection

    capabilities = get_capabilities(module)
    network_api = capabilities.get("network_api")
    if network_api in ["cliconf", "sfss_rest"]:
        module._sfss_connection = Connection(module._socket_path)
    else:
        module.fail_json(msg="Invalid connection type %s" % network_api)

    return module._sfss_connection


def get_capabilities(module):
    if hasattr(module, "_sfss_capabilities"):
        return module._sfss_capabilities
    try:
        capabilities = Connection(module._socket_path).get_capabilities()
    except ConnectionError as exc:
        module.fail_json(msg=to_text(exc, errors="surrogate_then_replace"))
    module._sfss_capabilities = json.loads(capabilities)
    return module._sfss_capabilities


def edit_config(module, commands, skip_code=None):
    connection = get_connection(module)
    try:
        return connection.edit_config(commands)
    except ConnectionError as exc:
        debug("Send requests edit_config: ")
        module.fail_json(msg=str(exc), code=exc.code)


def to_request(module, requests):
    transform = ComplexList(dict(path=dict(key=True), method={}, data=dict(type='dict')), module)
    return transform(to_list(requests))
