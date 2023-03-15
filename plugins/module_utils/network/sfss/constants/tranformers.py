from __future__ import (absolute_import, division, print_function)
__metaclass__ = type
from ansible_collections.dellemc.sfss.plugins.module_utils.network.sfss.utils.debug import debug


def get_orginate_nqn_by_instance(orginate_nqns, instance_id):
    ret = ""
    debug("get_orginate_nqn_by_instance instance_id", instance_id)
    debug("get_orginate_nqn_by_instance orginate_nqns", orginate_nqns)
    for orginate_nqn in orginate_nqns:
        if str(orginate_nqn.get("instance_id")) == str(instance_id):
            ret = orginate_nqn.get("orginate_nqn")
            debug("get_orginate_nqn_by_instance matched", ret)
            break

    return ret


def zone_group_id(zone_group_name, orginate_nqn_id, config_type='config'):
    group_format_str = "{config_type}:{zone_group_name}:{orginate_nqn_id}"
    ret = group_format_str.format(config_type=config_type, zone_group_name=zone_group_name,
                                  orginate_nqn_id=orginate_nqn_id)

    return ret


def zone_id(zone_group_id, zone_name):
    ret = "{zone_group_id}:{zone_name}".format(zone_group_id=zone_group_id, zone_name=zone_name)
    return ret


def zone_member_id(zone_id, member_id):
    ret = "{zone_id}:{member_id}".format(zone_id=zone_id, member_id=member_id)

    return ret


def transform_end_point_name_type(type):
    ret = 'NQN'
    if "fqn" in type.lower():
        return 'FullQualifiedName'

    return ret


def retransform_end_point_name_type(type):
    ret = 'fqn'
    if "nqn" in type.lower():
        return 'nqn'

    return ret


def transform_end_point_type(role):
    ret = None
    if role == 'host':
        ret = 'Host'
    elif role == 'subsystem':
        ret = 'Subsystem'
    elif role == 'ddc':
        ret = 'DDC'

    return ret


def transform_cdc_state(state):
    if state == "Enable":
        return True
    else:
        return False


def retransform_cdc_state(state):
    ret = "Disable"
    if state:
        return "Enable"

    return ret


def retransform_zone_member_type(type):
    ret = 'fqn'
    type_str = type.lower()
    if "nqn" in type_str:
        ret = 'nqn'
    elif 'zonealias' in type_str:
        ret = 'zone_alias'

    return ret


def transform_zone_member_type(type):
    ret = 'NQN'
    type_str = type.lower()
    if "fqn" in type_str:
        ret = 'FullQualifiedName'
    elif 'zone_alias' in type_str:
        ret = 'ZoneAlias'

    return ret


def transform_zone_group_active_state(type):
    ret = 'DeActivate'
    if type:
        ret = 'Activate'

    return ret


def retransform_zone_group_active_state(type):
    ret = True
    if "DeActivate" in type:
        ret = False

    return ret


def get_endpoint_id(nqn_id, ip, ip_type, transport_service_id="", port_id=0, transport_type='TCP'):
    if transport_service_id != "":
        transport_service_id = int(transport_service_id)
    ip_type_id = 'V4'
    if ip_type == "ipv6":
        ip = "<{ip}>".format(ip=ip)
        ip_type_id = 'V6'
    # <NQN>@<ip>:<V4/V6>:<TRANSPORT_SERVICE_ID>:0:<PORT_ID>:<TCP>
    ret = "{nqn_id}@{ip}:{ip_type_id}:{transport_service_id}:0:{port_id}:{transport_type}"
    return ret.format(nqn_id=nqn_id, ip=ip, ip_type_id=ip_type_id, port_id=port_id,
                      transport_service_id=transport_service_id, transport_type=transport_type)
