.. _sfss_cdc_instances_module:


sfss_cdc_instances -- Manage the SFSS CDC Instance Manager attributes
=====================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

This module is used to manage the SFSS CDC Instance Manager attributes.






Parameters
----------

  config (optional, list, None)
    A list of CDC instances.


    instance_id (True, int, None)
      The instance identifier.


    interfaces (optional, list, None)
      A list of interface members.


      name (True, str, None)
        Name of the interface.



    admin_state (True, bool, None)
      Administrative state of the interface, enable or disable.


    discovery_svc_admin_state (True, bool, None)
      Administrative state of the discovery service, enable or disable.



  state (optional, str, merged)
    The state the configuration should be left in





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
    #
    # Before state:
    # -------------
    #
    # redfish/v1/SFSSApp/CDCInstanceManagers
    # "CDCInstanceManagers": [
    # {
    #     "CDCAdminState": "Enable",
    #     "DiscoverySvcAdminState": "Enable",
    #     "InstanceIdentifier": "1",
    #     "Interfaces": [
    #         "ens192.222"
    #     ],
    #     "IpAddresses": [
    #         "12.1.1.222"
    #     ],
    #     "@odata.id": "/redfish/v1/SFSSApp/CDCInstanceManagers('1')",
    #     "@odata.type": "#CDCInstanceManagers.CDCInstanceManagers",
    #     "@odata.context": "/redfish/v1/SFSSApp/$metadata#CDCInstanceManagers/CDCInstanceManagers/$entity"
    # },
    # {
    #     "CDCAdminState": "Enable",
    #     "DiscoverySvcAdminState": "Enable",
    #     "InstanceIdentifier": "3",
    #     "Interfaces": [
    #         "ens160"
    #     ],
    #     "IpAddresses": [
    #         "100.104.26.76"
    #     ],
    #     "@odata.id": "/redfish/v1/SFSSApp/CDCInstanceManagers('3')",
    #     "@odata.type": "#CDCInstanceManagers.CDCInstanceManagers",
    #     "@odata.context": "/redfish/v1/SFSSApp/$metadata#CDCInstanceManagers/CDCInstanceManagers/$entity"
    # },
    # {
    #     "CDCAdminState": "Enable",
    #     "DiscoverySvcAdminState": "Disable",
    #     "InstanceIdentifier": "2",
    #     "Interfaces": [
    #         "ens192.223"
    #     ],
    #     "IpAddresses": [
    #         "12.1.1.223"
    #     ],
    #     "@odata.id": "/redfish/v1/SFSSApp/CDCInstanceManagers('2')",
    #     "@odata.type": "#CDCInstanceManagers.CDCInstanceManagers",
    #     "@odata.context": "/redfish/v1/SFSSApp/$metadata#CDCInstanceManagers/CDCInstanceManagers/$entity"
    # }
    # ]
    - name: Create CDC instances
      dellemc.sfss.cdc_instances:
      config:
      - admin_state: true
        discovery_svc_admin_state: true
        instance_id: 1
        interfaces:
        - name: ens192.222
      state: deleted
    #
    # After state:
    # -------------
    #
    # redfish/v1/SFSSApp/CDCInstanceManagers
    # "CDCInstanceManagers": [
    # {
    #     "CDCAdminState": "Enable",
    #     "DiscoverySvcAdminState": "Enable",
    #     "InstanceIdentifier": "3",
    #     "Interfaces": [
    #         "ens160"
    #     ],
    #     "IpAddresses": [
    #         "100.104.26.76"
    #     ],
    #     "@odata.id": "/redfish/v1/SFSSApp/CDCInstanceManagers('3')",
    #     "@odata.type": "#CDCInstanceManagers.CDCInstanceManagers",
    #     "@odata.context": "/redfish/v1/SFSSApp/$metadata#CDCInstanceManagers/CDCInstanceManagers/$entity"
    # },
    # {
    #     "CDCAdminState": "Enable",
    #     "DiscoverySvcAdminState": "Disable",
    #     "InstanceIdentifier": "2",
    #     "Interfaces": [
    #         "ens192.223"
    #     ],
    #     "IpAddresses": [
    #         "12.1.1.223"
    #     ],
    #     "@odata.id": "/redfish/v1/SFSSApp/CDCInstanceManagers('2')",
    #     "@odata.type": "#CDCInstanceManagers.CDCInstanceManagers",
    #     "@odata.context": "/redfish/v1/SFSSApp/$metadata#CDCInstanceManagers/CDCInstanceManagers/$entity"
    # }
    # ]
    # Using deleted
    #
    #
    # Before state:
    # -------------
    #
    #redfish/v1/SFSSApp/CDCInstanceManagers
    # "CDCInstanceManagers": [
    # {
    #     "CDCAdminState": "Enable",
    #     "DiscoverySvcAdminState": "Enable",
    #     "InstanceIdentifier": "1",
    #     "Interfaces": [
    #         "ens192.222"
    #     ],
    #     "IpAddresses": [
    #         "12.1.1.222"
    #     ],
    #     "@odata.id": "/redfish/v1/SFSSApp/CDCInstanceManagers('1')",
    #     "@odata.type": "#CDCInstanceManagers.CDCInstanceManagers",
    #     "@odata.context": "/redfish/v1/SFSSApp/$metadata#CDCInstanceManagers/CDCInstanceManagers/$entity"
    # },
    # {
    #     "CDCAdminState": "Enable",
    #     "DiscoverySvcAdminState": "Enable",
    #     "InstanceIdentifier": "3",
    #     "Interfaces": [
    #         "ens160"
    #     ],
    #     "IpAddresses": [
    #         "100.104.26.76"
    #     ],
    #     "@odata.id": "/redfish/v1/SFSSApp/CDCInstanceManagers('3')",
    #     "@odata.type": "#CDCInstanceManagers.CDCInstanceManagers",
    #     "@odata.context": "/redfish/v1/SFSSApp/$metadata#CDCInstanceManagers/CDCInstanceManagers/$entity"
    # },
    # {
    #     "CDCAdminState": "Enable",
    #     "DiscoverySvcAdminState": "Disable",
    #     "InstanceIdentifier": "2",
    #     "Interfaces": [
    #         "ens192.223"
    #     ],
    #     "IpAddresses": [
    #         "12.1.1.223"
    #     ],
    #     "@odata.id": "/redfish/v1/SFSSApp/CDCInstanceManagers('2')",
    #     "@odata.type": "#CDCInstanceManagers.CDCInstanceManagers",
    #     "@odata.context": "/redfish/v1/SFSSApp/$metadata#CDCInstanceManagers/CDCInstanceManagers/$entity"
    # }
    # ]
    - name: Create CDC instances
      dellemc.sfss.cdc_instances:
        config: []
        state: deleted
    #
    # After state:
    # -------------
    #
    #redfish/v1/SFSSApp/CDCInstanceManagers
    # {
    # "CDCInstanceManagers@odata.count": 0,
    # "@odata.id": "/redfish/v1/SFSSApp/CDCInstanceManagers?$expand=CDCInstanceManagers",
    # "@odata.context": "/redfish/v1/SFSSApp/$metadata#CDCInstanceManagers",
    # "@odata.type": "#CDCInstanceManagersCollection.CDCInstanceManagersCollection"
    # }
    #
    #
    # Using merged
    #
    #
    # Before state:
    # -------------
    #
    #redfish/v1/SFSSApp/CDCInstanceManagers
    # "CDCInstanceManagers": [
    # {
    #     "CDCAdminState": "Enable",
    #     "DiscoverySvcAdminState": "Enable",
    #     "InstanceIdentifier": "3",
    #     "Interfaces": [
    #         "ens160"
    #     ],
    #     "IpAddresses": [
    #         "100.104.26.76"
    #     ],
    #     "@odata.id": "/redfish/v1/SFSSApp/CDCInstanceManagers('3')",
    #     "@odata.type": "#CDCInstanceManagers.CDCInstanceManagers",
    #     "@odata.context": "/redfish/v1/SFSSApp/$metadata#CDCInstanceManagers/CDCInstanceManagers/$entity"
    # },
    # {
    #     "CDCAdminState": "Enable",
    #     "DiscoverySvcAdminState": "Disable",
    #     "InstanceIdentifier": "2",
    #     "Interfaces": [
    #         "ens192.223"
    #     ],
    #     "IpAddresses": [
    #         "12.1.1.223"
    #     ],
    #     "@odata.id": "/redfish/v1/SFSSApp/CDCInstanceManagers('2')",
    #     "@odata.type": "#CDCInstanceManagers.CDCInstanceManagers",
    #     "@odata.context": "/redfish/v1/SFSSApp/$metadata#CDCInstanceManagers/CDCInstanceManagers/$entity"
    # }
    # ]
    - name: Create CDC instances
      dellemc.sfss.cdc_instances:
      config:
      - admin_state: true
        discovery_svc_admin_state: true
        instance_id: 1
        interfaces:
        - name: ens192.222
    #
    # After state:
    # -------------
    #
    #redfish/v1/SFSSApp/CDCInstanceManagers
    # "CDCInstanceManagers": [
    # {
    #     "CDCAdminState": "Enable",
    #     "DiscoverySvcAdminState": "Enable",
    #     "InstanceIdentifier": "1",
    #     "Interfaces": [
    #         "ens192.222"
    #     ],
    #     "IpAddresses": [
    #         "12.1.1.222"
    #     ],
    #     "@odata.id": "/redfish/v1/SFSSApp/CDCInstanceManagers('1')",
    #     "@odata.type": "#CDCInstanceManagers.CDCInstanceManagers",
    #     "@odata.context": "/redfish/v1/SFSSApp/$metadata#CDCInstanceManagers/CDCInstanceManagers/$entity"
    # },
    # {
    #     "CDCAdminState": "Enable",
    #     "DiscoverySvcAdminState": "Enable",
    #     "InstanceIdentifier": "3",
    #     "Interfaces": [
    #         "ens160"
    #     ],
    #     "IpAddresses": [
    #         "100.104.26.76"
    #     ],
    #     "@odata.id": "/redfish/v1/SFSSApp/CDCInstanceManagers('3')",
    #     "@odata.type": "#CDCInstanceManagers.CDCInstanceManagers",
    #     "@odata.context": "/redfish/v1/SFSSApp/$metadata#CDCInstanceManagers/CDCInstanceManagers/$entity"
    # },
    # {
    #     "CDCAdminState": "Enable",
    #     "DiscoverySvcAdminState": "Disable",
    #     "InstanceIdentifier": "2",
    #     "Interfaces": [
    #         "ens192.223"
    #     ],
    #     "IpAddresses": [
    #         "12.1.1.223"
    #     ],
    #     "@odata.id": "/redfish/v1/SFSSApp/CDCInstanceManagers('2')",
    #     "@odata.type": "#CDCInstanceManagers.CDCInstanceManagers",
    #     "@odata.context": "/redfish/v1/SFSSApp/$metadata#CDCInstanceManagers/CDCInstanceManagers/$entity"
    # }
    # ]



Return Values
-------------

before (always, list, ['CDCAdminState: Enable', 'DiscoverySvcAdminState: Disable', 'InstanceIdentifier: 2'])
  The configuration prior to the model invocation.


after (when changed, list, ['CDCAdminState: Enable', 'DiscoverySvcAdminState: Disable', 'InstanceIdentifier: 2'])
  The resulting configuration model invocation.


commands (always, list, ['command 1', 'command 2', 'command 3'])
  The set of commands pushed to the remote device.





Status
------





Authors
~~~~~~~

- Namrata Chatterjee (@nchatterjee)

