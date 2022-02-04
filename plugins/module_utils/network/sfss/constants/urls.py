SFSS_BASE = "redfish/v1/SFSS/"
SFSS_APP_GET = "redfish/v1/SFSSApp"
SFSS_APP_BASE = SFSS_APP_GET + "/"

CDC_BASE_URL = SFSS_APP_BASE + "CDCInstanceManagers"
CDC_INSTANCE_MANAGER_URL = CDC_BASE_URL + "?$expand=CDCInstanceManagers"
CDC_SPECIFIC_INSTANCE_URL = CDC_BASE_URL + "({instance_id})"

# Security authentication URLs
AUTHENTICATION_SEQUENCE_URL = SFSS_APP_BASE + "AuthenticationSequence"
TACACSSERVERS_URL = SFSS_APP_BASE + "TacacsServers"
RADIUS_SERVERS_URL = SFSS_APP_BASE + "RadiusServers"
SERVER_DELETE_URL = SFSS_APP_BASE + "{server_name}('{ip}')"
SERVER_CREATE_URL = SFSS_APP_BASE + "{auth_type}"

# CDC Instances
CDC_INSTANCES_URL = SFSS_BASE + "{instance_id}/CDCInstance?$source=config"

# Global Policies URLs
GLOBAL_POLICIES_URL = SFSS_BASE + "{instance_id}/GlobalPolicies"

# Backup and Restore URLs
BACKUP_URL = SFSS_APP_GET + "/Backups?$expand=Backups"
BACKUP_CREATE_URL = SFSS_APP_GET + "/Backups"
RESTORE_URL = SFSS_APP_GET + "/Restores?$expand=Restores"
RESTORE_CREATE_URL = SFSS_APP_GET + "/Restores"

# Endpoint URLs
EP_SPECIFIC_URL = SFSS_BASE + "{instance_id}/{endpoint_type_str}('{endpoint_id}')"
EP_BASE_URL = SFSS_BASE + "{instance_id}/{endpoint_type_str}"
EP_EXPNAD_URL = EP_BASE_URL + "?$expand={endpoint_type_str}"
EP_CREATE_URL = EP_BASE_URL + "?$source=config"
# Zone alias FACTS modules URLs
ZONE_ALIAS_URL = SFSS_BASE + "{instance_id}/ZoneDBs('config')/{zonealias_str}?$source=config&$expand={zonealias_str}"
ZONE_ALIAS_MEMBERS_URL1 = (SFSS_BASE
                           + "{instance_id}/ZoneDBs('config')/{zonealias_str}('config:{name}')/ZoneAliasMembers?$source=config&$expand=ZoneAliasMembers")
# Zone alias Config module URLS
ZA_CONFIG_URL = SFSS_BASE + "{instance_id}/ZoneDBs('config')/{zonealias_str}"
ZA_MEMBER_CONFIG_URL = SFSS_BASE + "{instance_id}/ZoneDBs('config')/{zonealias_str}('config:{zone_alias_name}')/ZoneAliasMembers"
ZA_MEMBER_SPECIFIC_GET_URL = ZA_MEMBER_CONFIG_URL + "('{member_id}')" + "?$source=config"
ZA_DELETE_URL = SFSS_BASE + "{instance_id}/ZoneDBs('config')/ZoneAlias('config:{zone_alias_name}')"
ZA_MEMBER_SPECIFIC_URL = SFSS_BASE + "{instance_id}/ZoneDBs('config')/ZoneAlias('config:{zone_alias_name}')/ZoneAliasMembers('config:{zone_alias_name}:{id}')"
ZA_ALL_MEMBER_DELETE_URL = SFSS_BASE + "{instance_id}/ZoneDBs('config')/ZoneAlias('config:{zone_alias_name}')/ZoneAliasMembers('{member_id}')"
# Zone FACTS modules URLs
ZONE_BASE_URL = SFSS_BASE + "{instance_id}/ZoneDBs('{config_type}')"
ZONE_GROUP_ALL_URL = ZONE_BASE_URL + "/ZoneGroups?$source=config&$expand=ZoneGroups"
ZONES_ALL_URL = ZONE_BASE_URL + "/ZoneGroups('{zone_group_id}')/Zones?$source=config&$expand=Zones"
ZONE_MEMBER_ALL_URL = ZONE_BASE_URL + "/ZoneGroups('{zone_group_id}')/Zones('{zone_id}')/ZoneMembers?$source=config&$expand=ZoneMembers"
# Zone Config module URLs
ZONE_GRP_CREATE_URL = ZONE_BASE_URL + "/ZoneGroups"
ZONE_GRP_UPDATE_URL = ZONE_GRP_CREATE_URL + "('{zone_group_id}')"

ZONE_CREATE_URL = ZONE_GRP_CREATE_URL + "('{zone_group_id}')/Zones"
ZONE_MEMBER_CREATE_URL = ZONE_CREATE_URL + "('{zone_id}')/ZoneMembers?$source=config"
ZONE_MEMBER_UPDATE_URL = ZONE_CREATE_URL + "('{zone_id}')/ZoneMembers('{zone_member_id}')?$source=config"
ZONE_DELETE_URL = ZONE_CREATE_URL + "('{zone_id}')?$source=config"
# APP_IMAGES
APP_IMAGES_BASE_URL = SFSS_APP_BASE + "SFSSImages"
APP_IMAGES_GET_URL = APP_IMAGES_BASE_URL + "?$expand=SFSSImages"
APP_IMAGES_SPECIFIC_GET_URL = APP_IMAGES_GET_URL + "({instance_id})"
APP_IMAGES_UPDATE_URL = APP_IMAGES_BASE_URL + "({version})"

# Interface IP management
INF_IP_MGMT_BASE_URL = SFSS_APP_BASE + "IpAddressManagements"
INF_IP_MGMT_URL = INF_IP_MGMT_BASE_URL + "?$expand=IpAddressManagements"
INF_IP_MGMT_UPDATE_URL = SFSS_APP_BASE + "IpAddressManagements('{interface_name}')"
