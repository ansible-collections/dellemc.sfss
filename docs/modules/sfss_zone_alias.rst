.. _sfss_zone_alias_module:


sfss_zone_alias -- Manage aliases for SFSS zones
================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

This module is used to manage aliases for SFSS zones and zone members. This module is used to define a friendly name for the zone.






Parameters
----------

  config (optional, list, None)
    A list of SFSS zone aliases.


    instance_id (True, int, None)
      Instance ID.


    name (True, str, None)
      Name of the zone alias.


    members (optional, dict, None)
      Name of the zone members.


      data (optional, list, None)
        Member information.


        id (True, str, None)
          Endpoint ID, for endpoints such as hosts, subsystems, or direct discovery controllers (DDCs).


        type (optional, str, nqn)
          Endpoint ID type NQN or FQN.


        role (True, str, None)
          Endpoint role Host, subsystem, or DDC.





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
    #redfish/v1/SFSS/1/ZoneDBs('config')/ZoneAlias?$source=config&$expand=ZoneAlias
    # "ZoneAlias": [
    # {
    #   "NumberZoneMembers": "2",
    #   "ZoneAliasMembers": [
    #       "config:zone_alais3:nqn.2014-08.org.nvmexpress:uuid:host:TCP:Ipv4:1.1.1.1:3002",
    #       "config:zone_alais3:nqn1.2014-08.org.nvmexpress:uuid:host:TCP:Ipv4:4.3.1.1:3002"
    #   ],
    #   "ZoneAliasName": "zone_alais3",
    #   "ZoneAliasId": "config:zone_alais3",
    #   "@odata.id": "/redfish/v1/SFSS/1/ZoneDBs('config')/ZoneAlias('config:zone_alais3')",
    #   "@odata.type": "#ZoneAlias.ZoneAlias",
    #   "@odata.context": "/redfish/v1/SFSS/1/ZoneDBs('config')/$metadata#ZoneAlias/ZoneAlias/$entity"
    # },
    # {
    #   "NumberZoneMembers": "3",
    #   "ZoneAliasMembers": [
    #       "config:zone_alais1:nqn.2014-08.org.nvmexpress:uuid:host:TCP:Ipv4:1.1.1.1:3002",
    #       "config:zone_alais1:nqn1.2014-08.org.nvmexpress:uuid:host:TCP:Ipv4:4.3.1.1:3002",
    #       "config:zone_alais1:nqn3.2014-08.org.nvmexpress:uuid:host:TCP:Ipv4:1.1.1.1:3002"
    #   ],
    #   "ZoneAliasName": "zone_alais1",
    #   "ZoneAliasId": "config:zone_alais1",
    #   "@odata.id": "/redfish/v1/SFSS/1/ZoneDBs('config')/ZoneAlias('config:zone_alais1')",
    #   "@odata.type": "#ZoneAlias.ZoneAlias",
    #   "@odata.context": "/redfish/v1/SFSS/1/ZoneDBs('config')/$metadata#ZoneAlias/ZoneAlias/$entity"
    # },
    # {
    #   "ZoneAliasId": "config:zone_alais4",
    #   "ZoneAliasName": "zone_alais4",
    #   "NumberZoneMembers": "0",
    #   "@odata.id": "/redfish/v1/SFSS/1/ZoneDBs('config')/ZoneAlias('config:zone_alais4')",
    #   "@odata.type": "#ZoneAlias.ZoneAlias",
    #   "@odata.context": "/redfish/v1/SFSS/1/ZoneDBs('config')/$metadata#ZoneAlias/ZoneAlias/$entity"
    # },
    # {
    #   "NumberZoneMembers": "2",
    #   "ZoneAliasMembers": [
    #       "config:zone_alais2:nqn1.2014-08.org.nvmexpress:uuid:host:TCP:Ipv4:4.3.1.1:3002",
    #       "config:zone_alais2:nqn2.2014-08.org.nvmexpress:uuid:host:TCP:Ipv4:1.1.1.1:3002"
    #   ],
    #   "ZoneAliasName": "zone_alais2",
    #   "ZoneAliasId": "config:zone_alais2",
    #   "@odata.id": "/redfish/v1/SFSS/1/ZoneDBs('config')/ZoneAlias('config:zone_alais2')",
    #   "@odata.type": "#ZoneAlias.ZoneAlias",
    #   "@odata.context": "/redfish/v1/SFSS/1/ZoneDBs('config')/$metadata#ZoneAlias/ZoneAlias/$entity"
    # }
    # ]
    #redfish/v1/SFSS/1/ZoneDBs('config')/ZoneAlias('config:zone_alais3')/ZoneAliasMembers?$source=config&$expand=ZoneAliasMembers
    # "ZoneMembers": [
    # {
    #   "Role": "Host",
    #   "ZoneMemberType": "FullQualifiedName",
    #   "ZoneAliasMemberId": "config:zone_alais3:nqn1.2014-08.org.nvmexpress:uuid:host:TCP:Ipv4:4.3.1.1:3002",
    #   "@odata.id": "/redfish/v1/SFSS/1/ZoneDBs('config')/ZoneAlias('config:zone_alais3')
    # /ZoneAliasMembers('config:zone_alais3:nqn1.2014-08.org.nvmexpress:uuid:host:TCP:Ipv4:4.3.1.1:3002')",
    #   "@odata.type": "#ZoneAliasMembers.ZoneAliasMembers",
    #   "@odata.context": "/redfish/v1/SFSS/1/ZoneDBs('config')/ZoneAlias('config:zone_alais3')/$metadata#ZoneAliasMembers/ZoneAliasMembers/$entity"
    # },
    # {
    #   "Role": "Subsystem",
    #   "ZoneMemberType": "NQN",
    #   "ZoneAliasMemberId": "config:zone_alais3:nqn.2014-08.org.nvmexpress:uuid:host:TCP:Ipv4:1.1.1.1:3002",
    #   "@odata.id": "/redfish/v1/SFSS/1/ZoneDBs('config')/ZoneAlias('config:zone_alais3')
    # /ZoneAliasMembers('config:zone_alais3:nqn.2014-08.org.nvmexpress:uuid:host:TCP:Ipv4:1.1.1.1:3002')",
    #   "@odata.type": "#ZoneAliasMembers.ZoneAliasMembers",
    #   "@odata.context": "/redfish/v1/SFSS/1/ZoneDBs('config')/ZoneAlias('config:zone_alais3')/$metadata#ZoneAliasMembers/ZoneAliasMembers/$entity"
    # }
    # ]

    - name: Stfs zones alias create
      dellemc.sfss.zone_alias:
        config:
        - name: zone_alais3
          instance_id: 1
          members:
            data:
              - id: "nqn.2014-08.org.nvmexpress:uuid:host:TCP:Ipv4:1.1.1.1:3002"
                type: 'nqn'
                role: 'subsystem'
        state: deleted

    #
    # After state:
    # -------------
    #
    #redfish/v1/SFSS/1/ZoneDBs('config')/ZoneAlias('config:zone_alais3')/ZoneAliasMembers?$source=config&$expand=ZoneAliasMembers
    # "ZoneMembers": [
    # {
    #   "Role": "Host",
    #   "ZoneMemberType": "FullQualifiedName",
    #   "ZoneAliasMemberId": "config:zone_alais3:nqn1.2014-08.org.nvmexpress:uuid:host:TCP:Ipv4:4.3.1.1:3002",
    #   "@odata.id": "/redfish/v1/SFSS/1/ZoneDBs('config')/ZoneAlias('config:zone_alais3')
    # /ZoneAliasMembers('config:zone_alais3:nqn1.2014-08.org.nvmexpress:uuid:host:TCP:Ipv4:4.3.1.1:3002')",
    #   "@odata.type": "#ZoneAliasMembers.ZoneAliasMembers",
    #   "@odata.context": "/redfish/v1/SFSS/1/ZoneDBs('config')/ZoneAlias('config:zone_alais3')/$metadata#ZoneAliasMembers/ZoneAliasMembers/$entity"
    # }
    # ]
    # Using deleted
    #
    # Before state:
    # -------------
    #
    #redfish/v1/SFSS/1/ZoneDBs('config')/ZoneAlias?$source=config&$expand=ZoneAlias
    # "ZoneAlias": [
    # {
    #   "NumberZoneMembers": "2",
    #   "ZoneAliasMembers": [
    #       "config:zone_alais3:nqn.2014-08.org.nvmexpress:uuid:host:TCP:Ipv4:1.1.1.1:3002",
    #       "config:zone_alais3:nqn1.2014-08.org.nvmexpress:uuid:host:TCP:Ipv4:4.3.1.1:3002"
    #   ],
    #   "ZoneAliasName": "zone_alais3",
    #   "ZoneAliasId": "config:zone_alais3",
    #   "@odata.id": "/redfish/v1/SFSS/1/ZoneDBs('config')/ZoneAlias('config:zone_alais3')",
    #   "@odata.type": "#ZoneAlias.ZoneAlias",
    #   "@odata.context": "/redfish/v1/SFSS/1/ZoneDBs('config')/$metadata#ZoneAlias/ZoneAlias/$entity"
    # },
    # {
    #   "NumberZoneMembers": "3",
    #   "ZoneAliasMembers": [
    #       "config:zone_alais1:nqn.2014-08.org.nvmexpress:uuid:host:TCP:Ipv4:1.1.1.1:3002",
    #       "config:zone_alais1:nqn1.2014-08.org.nvmexpress:uuid:host:TCP:Ipv4:4.3.1.1:3002",
    #       "config:zone_alais1:nqn3.2014-08.org.nvmexpress:uuid:host:TCP:Ipv4:1.1.1.1:3002"
    #   ],
    #   "ZoneAliasName": "zone_alais1",
    #   "ZoneAliasId": "config:zone_alais1",
    #   "@odata.id": "/redfish/v1/SFSS/1/ZoneDBs('config')/ZoneAlias('config:zone_alais1')",
    #   "@odata.type": "#ZoneAlias.ZoneAlias",
    #   "@odata.context": "/redfish/v1/SFSS/1/ZoneDBs('config')/$metadata#ZoneAlias/ZoneAlias/$entity"
    # },
    # {
    #   "ZoneAliasId": "config:zone_alais4",
    #   "ZoneAliasName": "zone_alais4",
    #   "NumberZoneMembers": "0",
    #   "@odata.id": "/redfish/v1/SFSS/1/ZoneDBs('config')/ZoneAlias('config:zone_alais4')",
    #   "@odata.type": "#ZoneAlias.ZoneAlias",
    #   "@odata.context": "/redfish/v1/SFSS/1/ZoneDBs('config')/$metadata#ZoneAlias/ZoneAlias/$entity"
    # },
    # {
    #   "NumberZoneMembers": "2",
    #   "ZoneAliasMembers": [
    #       "config:zone_alais2:nqn1.2014-08.org.nvmexpress:uuid:host:TCP:Ipv4:4.3.1.1:3002",
    #       "config:zone_alais2:nqn2.2014-08.org.nvmexpress:uuid:host:TCP:Ipv4:1.1.1.1:3002"
    #   ],
    #   "ZoneAliasName": "zone_alais2",
    #   "ZoneAliasId": "config:zone_alais2",
    #   "@odata.id": "/redfish/v1/SFSS/1/ZoneDBs('config')/ZoneAlias('config:zone_alais2')",
    #   "@odata.type": "#ZoneAlias.ZoneAlias",
    #   "@odata.context": "/redfish/v1/SFSS/1/ZoneDBs('config')/$metadata#ZoneAlias/ZoneAlias/$entity"
    # }
    # ]
    - name: Stfs zones alias create
      dellemc.sfss.zone_alias:
        config: []
        state: deleted

    #
    # After state:
    # -------------
    #
    #redfish/v1/SFSS/1/ZoneDBs('config')/ZoneAlias?$source=config&$expand=ZoneAlias
    # {
    #   "ZoneAlias@odata.count": 0,
    #   "@odata.id": "/redfish/v1/SFSS/1/ZoneDBs('config')/ZoneAlias?$source=config&$expand=ZoneAlias",
    #   "@odata.context": "/redfish/v1/SFSS/1/ZoneDBs('config')/$metadata#ZoneAlias",
    #   "@odata.type": "#ZoneAliasCollection.ZoneAliasCollection"
    # }

    # Using merged
    #
    # Before state:
    # -------------
    #
    #redfish/v1/SFSS/1/ZoneDBs('config')/ZoneAlias('config:zone_alais3')/ZoneAliasMembers?$source=config&$expand=ZoneAliasMembers
    # "ZoneMembers": [
    # {
    #   "Role": "Host",
    #   "ZoneMemberType": "FullQualifiedName",
    #   "ZoneAliasMemberId": "config:zone_alais3:nqn1.2014-08.org.nvmexpress:uuid:host:TCP:Ipv4:4.3.1.1:3002",
    #   "@odata.id": "/redfish/v1/SFSS/1/ZoneDBs('config')/ZoneAlias('config:zone_alais3')
    # /ZoneAliasMembers('config:zone_alais3:nqn1.2014-08.org.nvmexpress:uuid:host:TCP:Ipv4:4.3.1.1:3002')",
    #   "@odata.type": "#ZoneAliasMembers.ZoneAliasMembers",
    #   "@odata.context": "/redfish/v1/SFSS/1/ZoneDBs('config')/ZoneAlias('config:zone_alais3')/$metadata#ZoneAliasMembers/ZoneAliasMembers/$entity"
    # }
    # ]

    - name: Stfs zones alias create
      dellemc.sfss.zone_alias:
        config:
        - name: zone_alais3
          instance_id: 1
          members:
            data:
              - id: "nqn.2014-08.org.nvmexpress:uuid:host:TCP:Ipv4:1.1.1.1:3002"
                type: 'nqn'
                role: 'subsystem'


    #
    # After state:
    # ------------
    #redfish/v1/SFSS/1/ZoneDBs('config')/ZoneAlias('config:zone_alais3')/ZoneAliasMembers?$source=config&$expand=ZoneAliasMembers

    # "ZoneMembers": [
    # {
    #   "Role": "Host",
    #   "ZoneMemberType": "FullQualifiedName",
    #   "ZoneAliasMemberId": "config:zone_alais3:nqn1.2014-08.org.nvmexpress:uuid:host:TCP:Ipv4:4.3.1.1:3002",
    #   "@odata.id": "/redfish/v1/SFSS/1/ZoneDBs('config')/ZoneAlias('config:zone_alais3')
    # /ZoneAliasMembers('config:zone_alais3:nqn1.2014-08.org.nvmexpress:uuid:host:TCP:Ipv4:4.3.1.1:3002')",
    #   "@odata.type": "#ZoneAliasMembers.ZoneAliasMembers",
    #   "@odata.context": "/redfish/v1/SFSS/1/ZoneDBs('config')/ZoneAlias('config:zone_alais3')/$metadata#ZoneAliasMembers/ZoneAliasMembers/$entity"
    # },
    # {
    #   "Role": "Subsystem",
    #   "ZoneMemberType": "NQN",
    #   "ZoneAliasMemberId": "config:zone_alais3:nqn.2014-08.org.nvmexpress:uuid:host:TCP:Ipv4:1.1.1.1:3002",
    #   "@odata.id": "/redfish/v1/SFSS/1/ZoneDBs('config')/ZoneAlias('config:zone_alais3')
    # /ZoneAliasMembers('config:zone_alais3:nqn.2014-08.org.nvmexpress:uuid:host:TCP:Ipv4:1.1.1.1:3002')",
    #   "@odata.type": "#ZoneAliasMembers.ZoneAliasMembers",
    #   "@odata.context": "/redfish/v1/SFSS/1/ZoneDBs('config')/ZoneAlias('config:zone_alais3')/$metadata#ZoneAliasMembers/ZoneAliasMembers/$entity"
    # }
    # ]

    # Using merged
    #
    # Before state:
    # -------------
    #
    #redfish/v1/SFSS/1/ZoneDBs('config')/ZoneAlias('config:zone_alais3')/ZoneAliasMembers?$source=config&$expand=ZoneAliasMembers
    # "ZoneMembers": [
    # {
    #   "Role": "Host",
    #   "ZoneMemberType": "FullQualifiedName",
    #   "ZoneAliasMemberId": "config:zone_alais3:nqn1.2014-08.org.nvmexpress:uuid:host:TCP:Ipv4:4.3.1.1:3002",
    #   "@odata.id": "/redfish/v1/SFSS/1/ZoneDBs('config')/ZoneAlias('config:zone_alais3')
    # /ZoneAliasMembers('config:zone_alais3:nqn1.2014-08.org.nvmexpress:uuid:host:TCP:Ipv4:4.3.1.1:3002')",
    #   "@odata.type": "#ZoneAliasMembers.ZoneAliasMembers",
    #   "@odata.context": "/redfish/v1/SFSS/1/ZoneDBs('config')/ZoneAlias('config:zone_alais3')/$metadata#ZoneAliasMembers/ZoneAliasMembers/$entity"
    # },
    # {
    #   "Role": "Subsystem",
    #   "ZoneMemberType": "NQN",
    #   "ZoneAliasMemberId": "config:zone_alais3:nqn.2014-08.org.nvmexpress:uuid:host:TCP:Ipv4:1.1.1.1:3002",
    #   "@odata.id": "/redfish/v1/SFSS/1/ZoneDBs('config')/ZoneAlias('config:zone_alais3')
    # /ZoneAliasMembers('config:zone_alais3:nqn.2014-08.org.nvmexpress:uuid:host:TCP:Ipv4:1.1.1.1:3002')",
    #   "@odata.type": "#ZoneAliasMembers.ZoneAliasMembers",
    #   "@odata.context": "/redfish/v1/SFSS/1/ZoneDBs('config')/ZoneAlias('config:zone_alais3')/$metadata#ZoneAliasMembers/ZoneAliasMembers/$entity"
    # }
    # ]
    - name: Stfs zones alias create
      dellemc.sfss.zone_alias:
        config:
        - name: Ansible123
          instance_id: 1
          members:
            data:
              - id: "nqn.2014-08.org.nvmexpress:uuid:host:TCP:Ipv4:1.1.1.1:3002"
                type: 'nqn'
                role: 'host'

    #
    # After state:
    # ------------
    #redfish/v1/SFSS/1/ZoneDBs('config')/ZoneAlias('config:zone_alais3')/ZoneAliasMembers?$source=config&$expand=ZoneAliasMembers

    # "ZoneMembers": [
    # {
    #   "Role": "Host",
    #   "ZoneMemberType": "FullQualifiedName",
    #   "ZoneAliasMemberId": "config:zone_alais3:nqn1.2014-08.org.nvmexpress:uuid:host:TCP:Ipv4:4.3.1.1:3002",
    #   "@odata.id": "/redfish/v1/SFSS/1/ZoneDBs('config')/ZoneAlias('config:zone_alais3')
    # /ZoneAliasMembers('config:zone_alais3:nqn1.2014-08.org.nvmexpress:uuid:host:TCP:Ipv4:4.3.1.1:3002')",
    #   "@odata.type": "#ZoneAliasMembers.ZoneAliasMembers",
    #   "@odata.context": "/redfish/v1/SFSS/1/ZoneDBs('config')/ZoneAlias('config:zone_alais3')/$metadata#ZoneAliasMembers/ZoneAliasMembers/$entity"
    # },
    # {
    #   "Role": "Host",
    #   "ZoneMemberType": "NQN",
    #   "ZoneAliasMemberId": "config:zone_alais3:nqn.2014-08.org.nvmexpress:uuid:host:TCP:Ipv4:1.1.1.1:3002",
    #   "@odata.id": "/redfish/v1/SFSS/1/ZoneDBs('config')/ZoneAlias('config:zone_alais3')
    # /ZoneAliasMembers('config:zone_alais3:nqn.2014-08.org.nvmexpress:uuid:host:TCP:Ipv4:1.1.1.1:3002')",
    #   "@odata.type": "#ZoneAliasMembers.ZoneAliasMembers",
    #   "@odata.context": "/redfish/v1/SFSS/1/ZoneDBs('config')/ZoneAlias('config:zone_alais3')/$metadata#ZoneAliasMembers/ZoneAliasMembers/$entity"
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

