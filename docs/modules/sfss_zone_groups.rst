.. _sfss_zone_groups_module:


sfss_zone_groups -- Manage SFSS zone groups
===========================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

This module is used to manage SFSS zone groups.






Parameters
----------

  config (optional, list, None)
    A list of zone groups.


    name (True, str, None)
      Name of the zone group.


    instance_id (True, int, None)
      Instance ID.


    activate_status (optional, bool, None)
      Activate the zone group.


    activation_state (optional, str, None)
      Activation status of the zone group.



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

    
    # Using deleted
    #
    # Before state:
    # -------------
    #
    # redfish/v1/SFSS/1/ZoneDBs('config')/ZoneGroups?$source=config&$expand=ZoneGroups
    # "ZoneGroups": [
    # {
    #   "Type": "Manual",
    #   "ZoneDBType": "config",
    #   "ZoneGroupId": "config:play.zone_group1:nqn.1988-11.com.dell:SFSS:1:20210803224020e8",
    #   "ActivateStatus": "DeActivate",
    #   "zoneGroupName": "play.zone_group1",
    #   "OriginatorNQN": "nqn.1988-11.com.dell:SFSS:1:20210803224020e8",
    #   "ActivationState": "NotActive",
    #   "@odata.id": "/redfish/v1/SFSS/1/ZoneDBs('config')/ZoneGroups('config:play.zone_group1:nqn.1988-11.com.dell:SFSS:1:20210803224020e8')",
    #   "@odata.type": "#ZoneGroups.ZoneGroups",
    #   "@odata.context": "/redfish/v1/SFSS/1/ZoneDBs('config')/$metadata#ZoneGroups/ZoneGroups/$entity"
    # },
    # {
    #   "Type": "Manual",
    #   "ZoneDBType": "config",
    #   "ZoneGroupId": "config:reg.zone_group1:nqn.1988-11.com.dell:SFSS:1:20210803224020e8",
    #   "ActivateStatus": "Activate",
    #   "NumberZones": 1,
    #   "zoneGroupName": "reg.zone_group1",
    #   "OriginatorNQN": "nqn.1988-11.com.dell:SFSS:1:20210803224020e8",
    #   "Zones": "config:reg.zone_group1:nqn.1988-11.com.dell:SFSS:1:20210803224020e8:reg.zone1",
    #   "ActivationState": "ReActivationNeeded",
    #   "@odata.id": "/redfish/v1/SFSS/1/ZoneDBs('config')/ZoneGroups('config:reg.zone_group1:nqn.1988-11.com.dell:SFSS:1:20210803224020e8')",
    #   "@odata.type": "#ZoneGroups.ZoneGroups",
    #   "@odata.context": "/redfish/v1/SFSS/1/ZoneDBs('config')/$metadata#ZoneGroups/ZoneGroups/$entity"
    # },
    # {
    #   "Type": "Manual",
    #   "ZoneDBType": "config",
    #   "ZoneGroupId": "config:reg.zone_group2:nqn.1988-11.com.dell:SFSS:1:20210803224020e8",
    #   "ActivateStatus": "Activate",
    #   "NumberZones": 2,
    #   "zoneGroupName": "reg.zone_group2",
    #   "OriginatorNQN": "nqn.1988-11.com.dell:SFSS:1:20210803224020e8",
    #   "Zones": "config:reg.zone_group2:nqn.1988-11.com.dell:SFSS:1:20210803224020e8:reg.zone2|
    # config:reg.zone_group2:nqn.1988-11.com.dell:SFSS:1:20210803224020e8:reg.zone3",
    #   "ActivationState": "ReActivationNeeded",
    #   "@odata.id": "/redfish/v1/SFSS/1/ZoneDBs('config')/ZoneGroups('config:reg.zone_group2:nqn.1988-11.com.dell:SFSS:1:20210803224020e8')",
    #   "@odata.type": "#ZoneGroups.ZoneGroups",
    #   "@odata.context": "/redfish/v1/SFSS/1/ZoneDBs('config')/$metadata#ZoneGroups/ZoneGroups/$entity"
    # },
    # {
    #   "Type": "Manual",
    #   "ZoneDBType": "config",
    #   "ZoneGroupId": "config:ansible.zone_grp1:nqn.1988-11.com.dell:SFSS:1:20210803224020e8",
    #   "ActivateStatus": "Activate",
    #   "zoneGroupName": "ansible.zone_grp1",
    #   "OriginatorNQN": "nqn.1988-11.com.dell:SFSS:1:20210803224020e8",
    #   "ActivationState": "Active",
    #   "@odata.id": "/redfish/v1/SFSS/1/ZoneDBs('config')/ZoneGroups('config:ansible.zone_grp1:nqn.1988-11.com.dell:SFSS:1:20210803224020e8')",
    #   "@odata.type": "#ZoneGroups.ZoneGroups",
    #   "@odata.context": "/redfish/v1/SFSS/1/ZoneDBs('config')/$metadata#ZoneGroups/ZoneGroups/$entity"
    # }
    # ]
    - name: Stfs zones create
      dellemc.sfss.zone_groups:
        config:
          - name: ansible.zone_grp1
            instance_id: 1
            activate_status: true
        state: deleted
    #
    # After state:
    # -------------
    #
    # redfish/v1/SFSS/1/ZoneDBs('config')/ZoneGroups?$source=config&$expand=ZoneGroups
    # "ZoneGroups": [
    # {
    #   "Type": "Manual",
    #   "ZoneDBType": "config",
    #   "ZoneGroupId": "config:play.zone_group1:nqn.1988-11.com.dell:SFSS:1:20210803224020e8",
    #   "ActivateStatus": "DeActivate",
    #   "zoneGroupName": "play.zone_group1",
    #   "OriginatorNQN": "nqn.1988-11.com.dell:SFSS:1:20210803224020e8",
    #   "ActivationState": "NotActive",
    #   "@odata.id": "/redfish/v1/SFSS/1/ZoneDBs('config')/ZoneGroups('config:play.zone_group1:nqn.1988-11.com.dell:SFSS:1:20210803224020e8')",
    #   "@odata.type": "#ZoneGroups.ZoneGroups",
    #   "@odata.context": "/redfish/v1/SFSS/1/ZoneDBs('config')/$metadata#ZoneGroups/ZoneGroups/$entity"
    # },
    # {
    #   "Type": "Manual",
    #   "ZoneDBType": "config",
    #   "ZoneGroupId": "config:reg.zone_group1:nqn.1988-11.com.dell:SFSS:1:20210803224020e8",
    #   "ActivateStatus": "Activate",
    #   "NumberZones": 1,
    #   "zoneGroupName": "reg.zone_group1",
    #   "OriginatorNQN": "nqn.1988-11.com.dell:SFSS:1:20210803224020e8",
    #   "Zones": "config:reg.zone_group1:nqn.1988-11.com.dell:SFSS:1:20210803224020e8:reg.zone1",
    #   "ActivationState": "ReActivationNeeded",
    #   "@odata.id": "/redfish/v1/SFSS/1/ZoneDBs('config')/ZoneGroups('config:reg.zone_group1:nqn.1988-11.com.dell:SFSS:1:20210803224020e8')",
    #   "@odata.type": "#ZoneGroups.ZoneGroups",
    #   "@odata.context": "/redfish/v1/SFSS/1/ZoneDBs('config')/$metadata#ZoneGroups/ZoneGroups/$entity"
    # },
    # {
    #   "Type": "Manual",
    #   "ZoneDBType": "config",
    #   "ZoneGroupId": "config:reg.zone_group2:nqn.1988-11.com.dell:SFSS:1:20210803224020e8",
    #   "ActivateStatus": "Activate",
    #   "NumberZones": 2,
    #   "zoneGroupName": "reg.zone_group2",
    #   "OriginatorNQN": "nqn.1988-11.com.dell:SFSS:1:20210803224020e8",
    #   "Zones": "config:reg.zone_group2:nqn.1988-11.com.dell:SFSS:1:20210803224020e8:reg.zone2|
    # config:reg.zone_group2:nqn.1988-11.com.dell:SFSS:1:20210803224020e8:reg.zone3",
    #   "ActivationState": "ReActivationNeeded",
    #   "@odata.id": "/redfish/v1/SFSS/1/ZoneDBs('config')/ZoneGroups('config:reg.zone_group2:nqn.1988-11.com.dell:SFSS:1:20210803224020e8')",
    #   "@odata.type": "#ZoneGroups.ZoneGroups",
    #   "@odata.context": "/redfish/v1/SFSS/1/ZoneDBs('config')/$metadata#ZoneGroups/ZoneGroups/$entity"
    # }
    # ]
    #
    # Using deleted
    #
    # Before state:
    # -------------
    #
    # redfish/v1/SFSS/1/ZoneDBs('config')/ZoneGroups?$source=config&$expand=ZoneGroups
    #
    # "ZoneGroups": [
    # {
    #   "Type": "Manual",
    #   "ZoneDBType": "config",
    #   "ZoneGroupId": "config:play.zone_group1:nqn.1988-11.com.dell:SFSS:1:20210803224020e8",
    #   "ActivateStatus": "DeActivate",
    #   "zoneGroupName": "play.zone_group1",
    #   "OriginatorNQN": "nqn.1988-11.com.dell:SFSS:1:20210803224020e8",
    #   "ActivationState": "NotActive",
    #   "@odata.id": "/redfish/v1/SFSS/1/ZoneDBs('config')/ZoneGroups('config:play.zone_group1:nqn.1988-11.com.dell:SFSS:1:20210803224020e8')",
    #   "@odata.type": "#ZoneGroups.ZoneGroups",
    #   "@odata.context": "/redfish/v1/SFSS/1/ZoneDBs('config')/$metadata#ZoneGroups/ZoneGroups/$entity"
    # },
    # {
    #   "Type": "Manual",
    #   "ZoneDBType": "config",
    #   "ZoneGroupId": "config:reg.zone_group1:nqn.1988-11.com.dell:SFSS:1:20210803224020e8",
    #   "ActivateStatus": "Activate",
    #   "NumberZones": 1,
    #   "zoneGroupName": "reg.zone_group1",
    #   "OriginatorNQN": "nqn.1988-11.com.dell:SFSS:1:20210803224020e8",
    #   "Zones": "config:reg.zone_group1:nqn.1988-11.com.dell:SFSS:1:20210803224020e8:reg.zone1",
    #   "ActivationState": "ReActivationNeeded",
    #   "@odata.id": "/redfish/v1/SFSS/1/ZoneDBs('config')/ZoneGroups('config:reg.zone_group1:nqn.1988-11.com.dell:SFSS:1:20210803224020e8')",
    #   "@odata.type": "#ZoneGroups.ZoneGroups",
    #   "@odata.context": "/redfish/v1/SFSS/1/ZoneDBs('config')/$metadata#ZoneGroups/ZoneGroups/$entity"
    # },
    # {
    #   "Type": "Manual",
    #   "ZoneDBType": "config",
    #   "ZoneGroupId": "config:reg.zone_group2:nqn.1988-11.com.dell:SFSS:1:20210803224020e8",
    #   "ActivateStatus": "Activate",
    #   "NumberZones": 2,
    #   "zoneGroupName": "reg.zone_group2",
    #   "OriginatorNQN": "nqn.1988-11.com.dell:SFSS:1:20210803224020e8",
    #   "Zones": "config:reg.zone_group2:nqn.1988-11.com.dell:SFSS:1:20210803224020e8:reg.zone2|
    # config:reg.zone_group2:nqn.1988-11.com.dell:SFSS:1:20210803224020e8:reg.zone3",
    #   "ActivationState": "ReActivationNeeded",
    #   "@odata.id": "/redfish/v1/SFSS/1/ZoneDBs('config')/ZoneGroups('config:reg.zone_group2:nqn.1988-11.com.dell:SFSS:1:20210803224020e8')",
    #   "@odata.type": "#ZoneGroups.ZoneGroups",
    #   "@odata.context": "/redfish/v1/SFSS/1/ZoneDBs('config')/$metadata#ZoneGroups/ZoneGroups/$entity"
    # }
    # ]
    - name: Stfs zones create
      dellemc.sfss.zone_groups:
        config: []
        state: deleted
    #
    #
    # After state:
    # -------------
    # redfish/v1/SFSS/1/ZoneDBs('config')/ZoneGroups?$source=config&$expand=ZoneGroups
    # {
    #   "ZoneGroups@odata.count": 0,
    #   "@odata.id": "/redfish/v1/SFSS/1/ZoneDBs('config')/ZoneGroups?$source=config&$expand=ZoneGroups",
    #   "@odata.context": "/redfish/v1/SFSS/1/ZoneDBs('config')/$metadata#ZoneGroups",
    #   "@odata.type": "#ZoneGroupsCollection.ZoneGroupsCollection"
    # }
    #
    # Using merged
    #
    # Before state:
    # -------------
    #
    # redfish/v1/SFSS/1/ZoneDBs('config')/ZoneGroups?$source=config&$expand=ZoneGroups
    # "ZoneGroups": [
    # {
    #   "Type": "Manual",
    #   "ZoneDBType": "config",
    #   "ZoneGroupId": "config:play.zone_group1:nqn.1988-11.com.dell:SFSS:1:20210803224020e8",
    #   "ActivateStatus": "DeActivate",
    #   "zoneGroupName": "play.zone_group1",
    #   "OriginatorNQN": "nqn.1988-11.com.dell:SFSS:1:20210803224020e8",
    #   "ActivationState": "NotActive",
    #   "@odata.id": "/redfish/v1/SFSS/1/ZoneDBs('config')/ZoneGroups('config:play.zone_group1:nqn.1988-11.com.dell:SFSS:1:20210803224020e8')",
    #   "@odata.type": "#ZoneGroups.ZoneGroups",
    #   "@odata.context": "/redfish/v1/SFSS/1/ZoneDBs('config')/$metadata#ZoneGroups/ZoneGroups/$entity"
    # },
    # {
    #   "Type": "Manual",
    #   "ZoneDBType": "config",
    #   "ZoneGroupId": "config:reg.zone_group1:nqn.1988-11.com.dell:SFSS:1:20210803224020e8",
    #   "ActivateStatus": "Activate",
    #   "NumberZones": 1,
    #   "zoneGroupName": "reg.zone_group1",
    #   "OriginatorNQN": "nqn.1988-11.com.dell:SFSS:1:20210803224020e8",
    #   "Zones": "config:reg.zone_group1:nqn.1988-11.com.dell:SFSS:1:20210803224020e8:reg.zone1",
    #   "ActivationState": "ReActivationNeeded",
    #   "@odata.id": "/redfish/v1/SFSS/1/ZoneDBs('config')/ZoneGroups('config:reg.zone_group1:nqn.1988-11.com.dell:SFSS:1:20210803224020e8')",
    #   "@odata.type": "#ZoneGroups.ZoneGroups",
    #   "@odata.context": "/redfish/v1/SFSS/1/ZoneDBs('config')/$metadata#ZoneGroups/ZoneGroups/$entity"
    # },
    # {
    #   "Type": "Manual",
    #   "ZoneDBType": "config",
    #   "ZoneGroupId": "config:reg.zone_group2:nqn.1988-11.com.dell:SFSS:1:20210803224020e8",
    #   "ActivateStatus": "Activate",
    #   "NumberZones": 2,
    #   "zoneGroupName": "reg.zone_group2",
    #   "OriginatorNQN": "nqn.1988-11.com.dell:SFSS:1:20210803224020e8",
    #   "Zones": "config:reg.zone_group2:nqn.1988-11.com.dell:SFSS:1:20210803224020e8:reg.zone2|
    # config:reg.zone_group2:nqn.1988-11.com.dell:SFSS:1:20210803224020e8:reg.zone3",
    #   "ActivationState": "ReActivationNeeded",
    #   "@odata.id": "/redfish/v1/SFSS/1/ZoneDBs('config')/ZoneGroups('config:reg.zone_group2:nqn.1988-11.com.dell:SFSS:1:20210803224020e8')",
    #   "@odata.type": "#ZoneGroups.ZoneGroups",
    #   "@odata.context": "/redfish/v1/SFSS/1/ZoneDBs('config')/$metadata#ZoneGroups/ZoneGroups/$entity"
    # }
    # ]
    - name: Stfs zones create
      dellemc.sfss.zone_groups:
        config:
          - name: ansible.zone_grp1
            instance_id: 1
            activate_status: true
    #
    # After state:
    # -------------
    #
    # redfish/v1/SFSS/1/ZoneDBs('config')/ZoneGroups?$source=config&$expand=ZoneGroups
    # "ZoneGroups": [
    # {
    #   "Type": "Manual",
    #   "ZoneDBType": "config",
    #   "ZoneGroupId": "config:play.zone_group1:nqn.1988-11.com.dell:SFSS:1:20210803224020e8",
    #   "ActivateStatus": "DeActivate",
    #   "zoneGroupName": "play.zone_group1",
    #   "OriginatorNQN": "nqn.1988-11.com.dell:SFSS:1:20210803224020e8",
    #   "ActivationState": "NotActive",
    #   "@odata.id": "/redfish/v1/SFSS/1/ZoneDBs('config')/ZoneGroups('config:play.zone_group1:nqn.1988-11.com.dell:SFSS:1:20210803224020e8')",
    #   "@odata.type": "#ZoneGroups.ZoneGroups",
    #   "@odata.context": "/redfish/v1/SFSS/1/ZoneDBs('config')/$metadata#ZoneGroups/ZoneGroups/$entity"
    # },
    # {
    #   "Type": "Manual",
    #   "ZoneDBType": "config",
    #   "ZoneGroupId": "config:reg.zone_group1:nqn.1988-11.com.dell:SFSS:1:20210803224020e8",
    #   "ActivateStatus": "Activate",
    #   "NumberZones": 1,
    #   "zoneGroupName": "reg.zone_group1",
    #   "OriginatorNQN": "nqn.1988-11.com.dell:SFSS:1:20210803224020e8",
    #   "Zones": "config:reg.zone_group1:nqn.1988-11.com.dell:SFSS:1:20210803224020e8:reg.zone1",
    #   "ActivationState": "ReActivationNeeded",
    #   "@odata.id": "/redfish/v1/SFSS/1/ZoneDBs('config')/ZoneGroups('config:reg.zone_group1:nqn.1988-11.com.dell:SFSS:1:20210803224020e8')",
    #   "@odata.type": "#ZoneGroups.ZoneGroups",
    #   "@odata.context": "/redfish/v1/SFSS/1/ZoneDBs('config')/$metadata#ZoneGroups/ZoneGroups/$entity"
    # },
    # {
    #   "Type": "Manual",
    #   "ZoneDBType": "config",
    #   "ZoneGroupId": "config:reg.zone_group2:nqn.1988-11.com.dell:SFSS:1:20210803224020e8",
    #   "ActivateStatus": "Activate",
    #   "NumberZones": 2,
    #   "zoneGroupName": "reg.zone_group2",
    #   "OriginatorNQN": "nqn.1988-11.com.dell:SFSS:1:20210803224020e8",
    #   "Zones": "config:reg.zone_group2:nqn.1988-11.com.dell:SFSS:1:20210803224020e8:reg.zone2|
    # config:reg.zone_group2:nqn.1988-11.com.dell:SFSS:1:20210803224020e8:reg.zone3",
    #   "ActivationState": "ReActivationNeeded",
    #   "@odata.id": "/redfish/v1/SFSS/1/ZoneDBs('config')/ZoneGroups('config:reg.zone_group2:nqn.1988-11.com.dell:SFSS:1:20210803224020e8')",
    #   "@odata.type": "#ZoneGroups.ZoneGroups",
    #   "@odata.context": "/redfish/v1/SFSS/1/ZoneDBs('config')/$metadata#ZoneGroups/ZoneGroups/$entity"
    # },
    # {
    #   "Type": "Manual",
    #   "ZoneDBType": "config",
    #   "ZoneGroupId": "config:ansible.zone_grp1:nqn.1988-11.com.dell:SFSS:1:20210803224020e8",
    #   "ActivateStatus": "DeActivate",
    #   "NumberZones": 0,
    #   "zoneGroupName": "ansible.zone_grp1",
    #   "OriginatorNQN": "nqn.1988-11.com.dell:SFSS:1:20210803224020e8",
    #   "ActivationState": "ReActivationNeeded",
    #   "@odata.id": "/redfish/v1/SFSS/1/ZoneDBs('config')/ZoneGroups('config:ansible.zone_grp1:nqn.1988-11.com.dell:SFSS:1:20210803224020e8')",
    #   "@odata.type": "#ZoneGroups.ZoneGroups",
    #   "@odata.context": "/redfish/v1/SFSS/1/ZoneDBs('config')/$metadata#ZoneGroups/ZoneGroups/$entity"
    # }
    # ]



Return Values
-------------

before (always, list, The configuration returned will always be in the same format
 of the parameters above.
)
  The configuration prior to the model invocation.


after (when changed, list, The configuration returned will always be in the same format
 of the parameters above.
)
  The resulting configuration model invocation.


commands (always, list, ['command 1', 'command 2', 'command 3'])
  The set of commands pushed to the remote device.





Status
------





Authors
~~~~~~~

- Mohamed Javeed (@javeedf)

