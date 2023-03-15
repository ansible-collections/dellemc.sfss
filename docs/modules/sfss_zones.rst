.. _sfss_zones_module:


sfss_zones -- Manage the SFSS zone and zone member attributes
=============================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

This module is used to manage the SFSS zone and zone member attributes.






Parameters
----------

  config (optional, list, None)
    A list of SFSS zones.


    instance_id (True, int, None)
      Instance ID.


    name (True, str, None)
      Name of the zone.


    group_name (True, str, None)
      Name of the zone group.


    members (optional, dict, None)
      List of members associated with the zone.


      data (optional, list, None)
        List of members associated with the zone.


        id (True, str, None)
          ID of SFSS endpoints such as hosts, subsystems, or direct discovery controllers (DDCs).


        id_type (optional, str, nqn)
          Endpoint ID type NQN, FQN, or zone alias.


        role (optional, str, None)
          Endpoint role.





  state (optional, str, merged)
    The state the configuration should be left in.





Notes
-----

.. note::
   - Idempotent is supported.
   - Supports ``check_mode``.




Examples
--------

.. code-block:: yaml+jinja

    
    # Using merged
    #
    # Before state:
    # -------------
    #
    #redfish/v1/SFSS/1/ZoneDBs('config')/ZoneGroups?$source=config&$expand=ZoneGroups
    # "ZoneGroups": [
    # {
    #   "NumberZones": 1,
    #   "Type": "Manual",
    #   "ActivateStatus": "Activate",
    #   "zoneGroupName": "zg1",
    #   "OriginatorNQN": "nqn.1988-11.com.dell:SFSS:1:20210624220526e8",
    #   "ZoneDBType": "config",
    #   "Zones": "config:zg1:nqn.1988-11.com.dell:SFSS:1:20210624220526e8:z1",
    #   "ZoneGroupId": "config:zg1:nqn.1988-11.com.dell:SFSS:1:20210624220526e8",
    #   "ActivationState": "NotActive",
    #   "@odata.id": "/redfish/v1/SFSS/1/ZoneDBs('config')/ZoneGroups('config:zg1:nqn.1988-11.com.dell:SFSS:1:20210624220526e8')",
    #   "@odata.type": "#ZoneGroups.ZoneGroups",
    #   "@odata.context": "/redfish/v1/SFSS/1/ZoneDBs('config')/$metadata#ZoneGroups/ZoneGroups/$entity"
    # },
    # {
    #   "ActivationState": "NotActive",
    #   "OriginatorNQN": "nqn.1988-11.com.dell:SFSS:1:20210624220526e8",
    #   "ZoneDBType": "config",
    #   "ActivateStatus": "Activate",
    #   "Type": "Manual",
    #   "ZoneGroupId": "config:reg.zone_group1:nqn.1988-11.com.dell:SFSS:1:20210624220526e8",
    #   "zoneGroupName": "reg.zone_group1",
    #   "@odata.id": "/redfish/v1/SFSS/1/ZoneDBs('config')/ZoneGroups('config:reg.zone_group1:nqn.1988-11.com.dell:SFSS:1:20210624220526e8')",
    #   "@odata.type": "#ZoneGroups.ZoneGroups",
    #   "@odata.context": "/redfish/v1/SFSS/1/ZoneDBs('config')/$metadata#ZoneGroups/ZoneGroups/$entity"
    # },
    # {
    #   "ActivationState": "NotActive",
    #   "OriginatorNQN": "nqn.1988-11.com.dell:SFSS:1:20210624220526e8",
    #   "ZoneDBType": "config",
    #   "ActivateStatus": "Activate",
    #   "Type": "Manual",
    #   "ZoneGroupId": "config:test-zg1:nqn.1988-11.com.dell:SFSS:1:20210624220526e8",
    #   "zoneGroupName": "test-zg1",
    #   "NumberZones": 1,
    #   "Zones": "config:test-zg1:nqn.1988-11.com.dell:SFSS:1:20210624220526e8:zone-test1",
    #   "@odata.id": "/redfish/v1/SFSS/1/ZoneDBs('config')/ZoneGroups('config:test-zg1:nqn.1988-11.com.dell:SFSS:1:20210624220526e8')",
    #   "@odata.type": "#ZoneGroups.ZoneGroups",
    #   "@odata.context": "/redfish/v1/SFSS/1/ZoneDBs('config')/$metadata#ZoneGroups/ZoneGroups/$entity"
    # },
    # {
    #   "ActivationState": "NotActive",
    #   "OriginatorNQN": "nqn.1988-11.com.dell:SFSS:1:20210624220526e8",
    #   "ZoneDBType": "config",
    #   "ActivateStatus": "Activate",
    #   "Type": "Manual",
    #   "ZoneGroupId": "config:play.zone_group1:nqn.1988-11.com.dell:SFSS:1:20210624220526e8",
    #   "zoneGroupName": "play.zone_group1",
    #   "@odata.id": "/redfish/v1/SFSS/1/ZoneDBs('config')/ZoneGroups('config:play.zone_group1:nqn.1988-11.com.dell:SFSS:1:20210624220526e8')",
    #   "@odata.type": "#ZoneGroups.ZoneGroups",
    #   "@odata.context": "/redfish/v1/SFSS/1/ZoneDBs('config')/$metadata#ZoneGroups/ZoneGroups/$entity"
    # }
    # ]
    - name: Stfs zones create
      dellemc.sfss.zones:
        config:
          - name: Ansible_Zone
            instance_id: 1
            group_name: Zone_group_11
            members:
              data:
                - id: nqn.2014-08.org.nvmexpress:uuid:host
                  id_type: nqn
                  role: host
    # After state:
    # -------------
    #
    #redfish/v1/SFSS/1/ZoneDBs('config')/ZoneGroups?$source=config&$expand=ZoneGroups
    # "ZoneGroups": [
    # {
    #   "NumberZones": 1,
    #   "Type": "Manual",
    #   "ActivateStatus": "Activate",
    #   "zoneGroupName": "zg1",
    #   "OriginatorNQN": "nqn.1988-11.com.dell:SFSS:1:20210624220526e8",
    #   "ZoneDBType": "config",
    #   "Zones": "config:zg1:nqn.1988-11.com.dell:SFSS:1:20210624220526e8:z1",
    #   "ZoneGroupId": "config:zg1:nqn.1988-11.com.dell:SFSS:1:20210624220526e8",
    #   "ActivationState": "NotActive",
    #   "@odata.id": "/redfish/v1/SFSS/1/ZoneDBs('config')/ZoneGroups('config:zg1:nqn.1988-11.com.dell:SFSS:1:20210624220526e8')",
    #   "@odata.type": "#ZoneGroups.ZoneGroups",
    #   "@odata.context": "/redfish/v1/SFSS/1/ZoneDBs('config')/$metadata#ZoneGroups/ZoneGroups/$entity"
    # },
    # {
    #   "ActivationState": "NotActive",
    #   "OriginatorNQN": "nqn.1988-11.com.dell:SFSS:1:20210624220526e8",
    #   "ZoneDBType": "config",
    #   "ActivateStatus": "Activate",
    #   "Type": "Manual",
    #   "ZoneGroupId": "config:reg.zone_group1:nqn.1988-11.com.dell:SFSS:1:20210624220526e8",
    #   "zoneGroupName": "reg.zone_group1",
    #   "@odata.id": "/redfish/v1/SFSS/1/ZoneDBs('config')/ZoneGroups('config:reg.zone_group1:nqn.1988-11.com.dell:SFSS:1:20210624220526e8')",
    #   "@odata.type": "#ZoneGroups.ZoneGroups",
    #   "@odata.context": "/redfish/v1/SFSS/1/ZoneDBs('config')/$metadata#ZoneGroups/ZoneGroups/$entity"
    # },
    # {
    #   "ActivationState": "NotActive",
    #   "OriginatorNQN": "nqn.1988-11.com.dell:SFSS:1:20210624220526e8",
    #   "ZoneDBType": "config",
    #   "ActivateStatus": "Activate",
    #   "Type": "Manual",
    #   "ZoneGroupId": "config:test-zg1:nqn.1988-11.com.dell:SFSS:1:20210624220526e8",
    #   "zoneGroupName": "test-zg1",
    #   "NumberZones": 1,
    #   "Zones": "config:test-zg1:nqn.1988-11.com.dell:SFSS:1:20210624220526e8:zone-test1",
    #   "@odata.id": "/redfish/v1/SFSS/1/ZoneDBs('config')/ZoneGroups('config:test-zg1:nqn.1988-11.com.dell:SFSS:1:20210624220526e8')",
    #   "@odata.type": "#ZoneGroups.ZoneGroups",
    #   "@odata.context": "/redfish/v1/SFSS/1/ZoneDBs('config')/$metadata#ZoneGroups/ZoneGroups/$entity"
    # },
    # {
    #   "ActivationState": "NotActive",
    #   "OriginatorNQN": "nqn.1988-11.com.dell:SFSS:1:20210624220526e8",
    #   "ZoneDBType": "config",
    #   "ActivateStatus": "Activate",
    #   "Type": "Manual",
    #   "ZoneGroupId": "config:play.zone_group1:nqn.1988-11.com.dell:SFSS:1:20210624220526e8",
    #   "zoneGroupName": "play.zone_group1",
    #   "@odata.id": "/redfish/v1/SFSS/1/ZoneDBs('config')/ZoneGroups('config:play.zone_group1:nqn.1988-11.com.dell:SFSS:1:20210624220526e8')",
    #   "@odata.type": "#ZoneGroups.ZoneGroups",
    #   "@odata.context": "/redfish/v1/SFSS/1/ZoneDBs('config')/$metadata#ZoneGroups/ZoneGroups/$entity"
    # },
    # {
    #   "ActivationState": "NotActive",
    #   "OriginatorNQN": "nqn.1988-11.com.dell:SFSS:1:20210624220526e8",
    #   "Type": "Manual",
    #   "ZoneGroupId": "config:Zone_group_11:nqn.1988-11.com.dell:SFSS:1:20210624220526e8",
    #   "ZoneDBType": "config",
    #   "ActivateStatus": "Activate",
    #   "zoneGroupName": "Zone_group_11",
    #   "NumberZones": 2,
    #   "Zones": "config:Zone_group_11:nqn.1988-11.com.dell:SFSS:1:20210624220526e8:Ansible_Zone|
    #             config:Zone_group_11:nqn.1988-11.com.dell:SFSS:1:20210624220526e8:",
    #   "@odata.id": "/redfish/v1/SFSS/1/ZoneDBs('config')/ZoneGroups('config:Zone_group_11:nqn.1988-11.com.dell:SFSS:1:20210624220526e8')",
    #   "@odata.type": "#ZoneGroups.ZoneGroups",
    #   "@odata.context": "/redfish/v1/SFSS/1/ZoneDBs('config')/$metadata#ZoneGroups/ZoneGroups/$entity"
    # }
    # ]
    #redfish/v1/SFSS/1/ZoneDBs('config')/ZoneGroups('config:Zone_group_11:nqn.1988-11.com.dell:SFSS:1:20210624220526e8')/Zones?$source=config
    # "Zones": [
    # {
    #   "@odata.id": "/redfish/v1/SFSS/1/ZoneDBs('config')/ZoneGroups('config:Zone_group_11:nqn.1988-11.com.dell:SFSS:1:20210624220526e8')
    #                 /Zones('config:Zone_group_11:nqn.1988-11.com.dell:SFSS:1:20210624220526e8:Ansible_Zone')"
    # }
    # ]
    #redfish/v1/SFSS/1/ZoneDBs('config')/ZoneGroups('config:Zone_group_11:nqn.1988-11.com.dell:SFSS:1:20210624220526e8')/Zones('config:Zone_group_11:nqn.1988-11.com.dell:SFSS:1:20210624220526e8:Ansible_Zone')/ZoneMembers?$source=config
    # "ZoneMembers": [
    # {
    #   "ZoneMemberId": "config:Zone_group_11:nqn.1988-11.com.dell:SFSS:1:20210624220526e8:Ansible_Zone:nqn.2014-08.org.nvmexpress:uuid:host",
    #   "Role": "Host",
    #   "ZoneMemberType": "NQN",
    #   "@odata.id": "/redfish/v1/SFSS/1/ZoneDBs('config')/ZoneGroups('config:Zone_group_11:nqn.1988-11.com.dell:SFSS:1:20210624220526e8')
    # /Zones('config:Zone_group_11:nqn.1988-11.com.dell:SFSS:1:20210624220526e8:Ansible_Zone')
    # /ZoneMembers('config:Zone_group_11:nqn.1988-11.com.dell:SFSS:1:20210624220526e8:Ansible_Zone:nqn.2014-08.org.nvmexpress:uuid:host')",
    #   "@odata.type": "#ZoneMembers.ZoneMembers",
    #   "@odata.context": "/redfish/v1/SFSS/1/ZoneDBs('config')/ZoneGroups('config:Zone_group_11:nqn.1988-11.com.dell:SFSS:1:20210624220526e8')
    # /Zones('config:Zone_group_11:nqn.1988-11.com.dell:SFSS:1:20210624220526e8:Ansible_Zone')/$metadata#ZoneMembers/ZoneMembers/$entity"
    # }
    # ]
    # Using deleted
    #
    # Before state:
    # -------------
    #
    #redfish/v1/SFSS/1/ZoneDBs('config')/ZoneGroups('config:Zone_group_11:nqn.1988-11.com.dell:SFSS:1:20210624220526e8')/Zones('config:Zone_group_11:nqn.1988-11.com.dell:SFSS:1:20210624220526e8:Ansible_Zone')/ZoneMembers?$source=config
    # "ZoneMembers": [
    # {
    #   "ZoneMemberId": "config:Zone_group_11:nqn.1988-11.com.dell:SFSS:1:20210624220526e8:Ansible_Zone:nqn.2014-08.org.nvmexpress:uuid:host",
    #   "Role": "Host",
    #   "ZoneMemberType": "NQN",
    #   "@odata.id": "/redfish/v1/SFSS/1/ZoneDBs('config')/ZoneGroups('config:Zone_group_11:nqn.1988-11.com.dell:SFSS:1:20210624220526e8')
    # /Zones('config:Zone_group_11:nqn.1988-11.com.dell:SFSS:1:20210624220526e8:Ansible_Zone')
    # /ZoneMembers('config:Zone_group_11:nqn.1988-11.com.dell:SFSS:1:20210624220526e8:Ansible_Zone:nqn.2014-08.org.nvmexpress:uuid:host')",
    #   "@odata.type": "#ZoneMembers.ZoneMembers",
    #   "@odata.context": "/redfish/v1/SFSS/1/ZoneDBs('config')/ZoneGroups('config:Zone_group_11:nqn.1988-11.com.dell:SFSS:1:20210624220526e8')
    # /Zones('config:Zone_group_11:nqn.1988-11.com.dell:SFSS:1:20210624220526e8:Ansible_Zone')/$metadata#ZoneMembers/ZoneMembers/$entity"
    # }
    # ]
    - name: Stfs zones create
      dellemc.sfss.zones:
        config:
          - name: Ansible_Zone
            instance_id: 1
            group_name: Zone_group_11
            members:
              data:
                - id: nqn.2014-08.org.nvmexpress:uuid:host
                  id_type: nqn
                  role: host
        state: deleted

    #
    # After state:
    # -------------
    #
    #redfish/v1/SFSS/1/ZoneDBs('config')/ZoneGroups('config:Zone_group_11:nqn.1988-11.com.dell:SFSS:1:20210624220526e8')/Zones('config:Zone_group_11:nqn.1988-11.com.dell:SFSS:1:20210624220526e8:Ansible_Zone')/ZoneMembers?$source=config&$expand=ZoneMembers
    # {
    #   "ZoneMembers@odata.count": 0,
    #   "@odata.id": "/redfish/v1/SFSS/1/ZoneDBs('config')/ZoneGroups('config:Zone_group_11:nqn.1988-11.com.dell:SFSS:1:20210624220526e8')
    #   /Zones('config:Zone_group_11:nqn.1988-11.com.dell:SFSS:1:20210624220526e8:Ansible_Zone')/ZoneMembers?$source=config&$expand=ZoneMembers",
    #   "@odata.context": "/redfish/v1/SFSS/1/ZoneDBs('config')/ZoneGroups('config:Zone_group_11:nqn.1988-11.com.dell:SFSS:1:20210624220526e8')
    #   /Zones('config:Zone_group_11:nqn.1988-11.com.dell:SFSS:1:20210624220526e8:Ansible_Zone')/$metadata#ZoneMembers",
    #   "@odata.type": "#ZoneMembersCollection.ZoneMembersCollection"
    # }

    # Using deleted
    #
    # Before state:
    # -------------
    #
    #redfish/v1/SFSS/1/ZoneDBs('config')/ZoneGroups?$source=config&$expand=ZoneGroups
    # "ZoneGroups": [
    # {
    #   "NumberZones": 1,
    #   "Type": "Manual",
    #   "ActivateStatus": "Activate",
    #   "zoneGroupName": "zg1",
    #   "OriginatorNQN": "nqn.1988-11.com.dell:SFSS:1:20210624220526e8",
    #   "ZoneDBType": "config",
    #   "Zones": "config:zg1:nqn.1988-11.com.dell:SFSS:1:20210624220526e8:z1",
    #   "ZoneGroupId": "config:zg1:nqn.1988-11.com.dell:SFSS:1:20210624220526e8",
    #   "ActivationState": "NotActive",
    #   "@odata.id": "/redfish/v1/SFSS/1/ZoneDBs('config')/ZoneGroups('config:zg1:nqn.1988-11.com.dell:SFSS:1:20210624220526e8')",
    #   "@odata.type": "#ZoneGroups.ZoneGroups",
    #   "@odata.context": "/redfish/v1/SFSS/1/ZoneDBs('config')/$metadata#ZoneGroups/ZoneGroups/$entity"
    # },
    # {
    #   "ActivationState": "NotActive",
    #   "OriginatorNQN": "nqn.1988-11.com.dell:SFSS:1:20210624220526e8",
    #   "ZoneDBType": "config",
    #   "ActivateStatus": "Activate",
    #   "Type": "Manual",
    #   "ZoneGroupId": "config:reg.zone_group1:nqn.1988-11.com.dell:SFSS:1:20210624220526e8",
    #   "zoneGroupName": "reg.zone_group1",
    #   "@odata.id": "/redfish/v1/SFSS/1/ZoneDBs('config')/ZoneGroups('config:reg.zone_group1:nqn.1988-11.com.dell:SFSS:1:20210624220526e8')",
    #   "@odata.type": "#ZoneGroups.ZoneGroups",
    #   "@odata.context": "/redfish/v1/SFSS/1/ZoneDBs('config')/$metadata#ZoneGroups/ZoneGroups/$entity"
    # },
    # {
    #   "ActivationState": "NotActive",
    #   "OriginatorNQN": "nqn.1988-11.com.dell:SFSS:1:20210624220526e8",
    #   "ZoneDBType": "config",
    #   "ActivateStatus": "Activate",
    #   "Type": "Manual",
    #   "ZoneGroupId": "config:test-zg1:nqn.1988-11.com.dell:SFSS:1:20210624220526e8",
    #   "zoneGroupName": "test-zg1",
    #   "NumberZones": 1,
    #   "Zones": "config:test-zg1:nqn.1988-11.com.dell:SFSS:1:20210624220526e8:zone-test1",
    #   "@odata.id": "/redfish/v1/SFSS/1/ZoneDBs('config')/ZoneGroups('config:test-zg1:nqn.1988-11.com.dell:SFSS:1:20210624220526e8')",
    #   "@odata.type": "#ZoneGroups.ZoneGroups",
    #   "@odata.context": "/redfish/v1/SFSS/1/ZoneDBs('config')/$metadata#ZoneGroups/ZoneGroups/$entity"
    # },
    # {
    #   "ActivationState": "NotActive",
    #   "OriginatorNQN": "nqn.1988-11.com.dell:SFSS:1:20210624220526e8",
    #   "ZoneDBType": "config",
    #   "ActivateStatus": "Activate",
    #   "Type": "Manual",
    #   "ZoneGroupId": "config:play.zone_group1:nqn.1988-11.com.dell:SFSS:1:20210624220526e8",
    #   "zoneGroupName": "play.zone_group1",
    #   "@odata.id": "/redfish/v1/SFSS/1/ZoneDBs('config')/ZoneGroups('config:play.zone_group1:nqn.1988-11.com.dell:SFSS:1:20210624220526e8')",
    #   "@odata.type": "#ZoneGroups.ZoneGroups",
    #   "@odata.context": "/redfish/v1/SFSS/1/ZoneDBs('config')/$metadata#ZoneGroups/ZoneGroups/$entity"
    # }
    # ]
    - name: Stfs zones create
      dellemc.sfss.zones:
        config: []
        state: deleted
    #
    # After state:
    # -------------
    #
    #redfish/v1/SFSS/1/ZoneDBs('config')/ZoneGroups?$source=config&$expand=ZoneGroups
    # {
    #   "ZoneGroups@odata.count": 0,
    #   "@odata.id": "/redfish/v1/SFSS/1/ZoneDBs('config')/ZoneGroups?$source=config&$expand=ZoneGroups",
    #   "@odata.context": "/redfish/v1/SFSS/1/ZoneDBs('config')/$metadata#ZoneGroups",
    #   "@odata.type": "#ZoneGroupsCollection.ZoneGroupsCollection"
    # }



Return Values
-------------

before (always, list, ['ZoneName: ansible_zone1', 'numberZoneMembers: 0', 'zoneId: config:AutoZonegroupnew:nqn.1988-11.com.dell:SFSS:1:20230314033523e8:ansible_zone1'])
  The configuration prior to the model invocation.


after (when changed, list, ['ZoneName: ansible_zone1', 'numberZoneMembers: 0', 'zoneId: config:AutoZonegroupnew:nqn.1988-11.com.dell:SFSS:1:20230314033523e8:ansible_zone1'])
  The resulting configuration model invocation.


commands (always, list, ['command 1', 'command 2', 'command 3'])
  The set of commands pushed to the remote device.





Status
------





Authors
~~~~~~~

- Mohamed Javeed (@javeedf)

