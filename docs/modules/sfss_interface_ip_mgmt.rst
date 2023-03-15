.. _sfss_interface_ip_mgmt_module:


sfss_interface_ip_mgmt -- Manage SFSS APP interfaces
====================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

This module is used to manage SFSS application interfaces. This module is used to create subinterfaces and assign IP address to the subinterfaces.






Parameters
----------

  config (optional, list, None)
    A list of interfaces.


    vlan_id (optional, int, None)
      VLAN ID for creating the subinterface.


    parent_interface (True, str, None)
      Parent interface name to create the subinterface based on the VLAN ID.


    ipv4_address (optional, str, None)
      IPv4 address of the subinterface.


    ipv4_netmask (optional, int, None)
      Subnet mask of the subinterface IPv4 address.


    ipv4_gateway (optional, str, None)
      IPv4 Gateway address of the subinterface.


    ipv4_config_type (True, str, None)
      Configuration type.


    ipv6_address (optional, str, None)
      IPv6 address of the subinterface.


    ipv6_netmask (optional, int, None)
      Subnet mask of the subinterface IPv6 address.


    ipv6_gateway (optional, str, None)
      IPv6 Gateway address of the subinterface.


    ipv6_config_type (True, str, None)
      Configuration type.


    name (optional, str, None)
      Name of the Interface.



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
    # redfish/v1/SFSSApp/IpAddressManagements?$expand=IpAddressManagements
    # "IpAddressManagements": [
    # {
    #   "Interface": "ens192.51",
    #   "Type": "VLAN",
    #   "IPV4Address": [
    #       "52.1.1.2"
    #   ],
    #   "IPV4Config": "MANUAL",
    #   "IPV4Gateway": "52.1.1.254",
    #   "IPV4PrefixLength": 16,
    #   "IPV6Address": [
    #       "fe52::1699:6f09:43dd:56c2"
    #   ],
    #   "IPV6Config": "MANUAL",
    #   "IPV6Gateway": "fe52::1699:6f09:43dd:ffff",
    #   "IPV6PrefixLength": 64,
    #   "ParentInterface": "ens192",
    #   "VlanId": 51,
    #   "@odata.id": "/redfish/v1/SFSSApp/IpAddressManagements('ens192.51')",
    #   "@odata.type": "#IpAddressManagements.IpAddressManagements",
    #   "@odata.context": "/redfish/v1/SFSSApp/$metadata#IpAddressManagements/IpAddressManagements/$entity"
    # },
    # {
    #   "Interface": "ens192.76",
    #   "Type": "VLAN",
    #   "IPV4Address": [
    #       "76.1.1.2"
    #   ],
    #   "IPV4Config": "MANUAL",
    #   "IPV4Gateway": "76.1.1.254",
    #   "IPV4PrefixLength": 16,
    #   "IPV6Address": [
    #       "fe76::1699:6f09:43dd:56c2"
    #   ],
    #   "IPV6Config": "MANUAL",
    #   "IPV6Gateway": "fe76::1699:6f09:43dd:ffff",
    #   "IPV6PrefixLength": 64,
    #   "ParentInterface": "ens192",
    #   "VlanId": 76,
    #   "@odata.id": "/redfish/v1/SFSSApp/IpAddressManagements('ens192.76')",
    #   "@odata.type": "#IpAddressManagements.IpAddressManagements",
    #   "@odata.context": "/redfish/v1/SFSSApp/$metadata#IpAddressManagements/IpAddressManagements/$entity"
    # },
    # {
    #   "Interface": "ens192.77",
    #   "Type": "VLAN",
    #   "IPV4Address": [
    #       "77.1.1.2"
    #   ],
    #   "IPV4Config": "MANUAL",
    #   "IPV4Gateway": "77.1.1.254",
    #   "IPV4PrefixLength": 16,
    #   "IPV6Address": [
    #       "fe77::1699:6f09:43dd:56c2"
    #   ],
    #   "IPV6Config": "MANUAL",
    #   "IPV6Gateway": "fe77::1699:6f09:43dd:ffff",
    #   "IPV6PrefixLength": 77,
    #   "ParentInterface": "ens192",
    #   "VlanId": 77,
    #   "@odata.id": "/redfish/v1/SFSSApp/IpAddressManagements('ens192.77')",
    #   "@odata.type": "#IpAddressManagements.IpAddressManagements",
    #   "@odata.context": "/redfish/v1/SFSSApp/$metadata#IpAddressManagements/IpAddressManagements/$entity"
    # },
    # {
    #   "Interface": "ens192.74",
    #   "Type": "VLAN",
    #   "IPV4Address": [
    #       "74.1.1.2"
    #   ],
    #   "IPV4Config": "MANUAL",
    #   "IPV4Gateway": "74.1.1.254",
    #   "IPV4PrefixLength": 16,
    #   "IPV6Address": [
    #       "fe74::1699:6f09:43dd:56c2"
    #   ],
    #   "IPV6Config": "MANUAL",
    #   "IPV6Gateway": "fe74::1699:6f09:43dd:ffff",
    #   "IPV6PrefixLength": 74,
    #   "ParentInterface": "ens192",
    #   "VlanId": 74,
    #   "@odata.id": "/redfish/v1/SFSSApp/IpAddressManagements('ens192.74')",
    #   "@odata.type": "#IpAddressManagements.IpAddressManagements",
    #   "@odata.context": "/redfish/v1/SFSSApp/$metadata#IpAddressManagements/IpAddressManagements/$entity"
    # },
    # {
    #   "Interface": "ens192.64",
    #   "Type": "VLAN",
    #   "IPV4Config": "AUTOMATIC",
    #   "IPV6Config": "AUTOMATIC",
    #   "ParentInterface": "ens192",
    #   "VlanId": 64,
    #   "@odata.id": "/redfish/v1/SFSSApp/IpAddressManagements('ens192.64')",
    #   "@odata.type": "#IpAddressManagements.IpAddressManagements",
    #   "@odata.context": "/redfish/v1/SFSSApp/$metadata#IpAddressManagements/IpAddressManagements/$entity"
    # },
    # {
    #   "Interface": "ens192",
    #   "Type": "ETHERNET",
    #   "IPV4Config": "AUTOMATIC",
    #   "IPV6Config": "AUTOMATIC",
    #   "@odata.id": "/redfish/v1/SFSSApp/IpAddressManagements('ens192')",
    #   "@odata.type": "#IpAddressManagements.IpAddressManagements",
    #   "@odata.context": "/redfish/v1/SFSSApp/$metadata#IpAddressManagements/IpAddressManagements/$entity"
    # },
    # {
    #   "Interface": "ens160",
    #   "Type": "ETHERNET",
    #   "IPV4Address": [
    #       "100.104.26.127"
    #   ],
    #   "IPV4Config": "MANUAL",
    #   "IPV4Gateway": "100.104.26.254",
    #   "IPV4PrefixLength": 24,
    #   "IPV6Config": "AUTOMATIC",
    #   "@odata.id": "/redfish/v1/SFSSApp/IpAddressManagements('ens160')",
    #   "@odata.type": "#IpAddressManagements.IpAddressManagements",
    #   "@odata.context": "/redfish/v1/SFSSApp/$metadata#IpAddressManagements/IpAddressManagements/$entity"
    # },
    # {
    #   "Interface": "ens192.75",
    #   "Type": "VLAN",
    #   "IPV4Address": [
    #       "75.1.1.2"
    #   ],
    #   "IPV4Config": "MANUAL",
    #   "IPV4Gateway": "75.1.1.254",
    #   "IPV4PrefixLength": 16,
    #   "IPV6Address": [
    #       "fe75::1699:6f09:43dd:56c2"
    #   ],
    #   "IPV6Config": "MANUAL",
    #   "IPV6Gateway": "fe75::1699:6f09:43dd:ffff",
    #   "IPV6PrefixLength": 75,
    #   "ParentInterface": "ens192",
    #   "VlanId": 75,
    #   "@odata.id": "/redfish/v1/SFSSApp/IpAddressManagements('ens192.75')",
    #   "@odata.type": "#IpAddressManagements.IpAddressManagements",
    #   "@odata.context": "/redfish/v1/SFSSApp/$metadata#IpAddressManagements/IpAddressManagements/$entity"
    # }
    # ]
    - name: Stfs interface ip management
      dellemc.sfss.interface_ip_mgmt:
        config:
        - ipv4_address: 52.1.1.2
          ipv4_config_type: manual
          ipv4_gateway: 52.1.1.254
          ipv4_netmask: 16
          ipv6_address: fe52::1699:6f09:43dd:56c2
          ipv6_config_type: manual
          ipv6_gateway: fe52::1699:6f09:43dd:ffff
          ipv6_netmask: 64
          parent_interface: ens192
          vlan_id: 51
        state: deleted
    #
    # After state:
    # -------------
    #
    # redfish/v1/SFSSApp/IpAddressManagements?$expand=IpAddressManagements
    # "IpAddressManagements": [
    # {
    #   "Interface": "ens192.76",
    #   "Type": "VLAN",
    #   "IPV4Address": [
    #       "76.1.1.2"
    #   ],
    #   "IPV4Config": "MANUAL",
    #   "IPV4Gateway": "76.1.1.254",
    #   "IPV4PrefixLength": 16,
    #   "IPV6Address": [
    #       "fe76::1699:6f09:43dd:56c2"
    #   ],
    #   "IPV6Config": "MANUAL",
    #   "IPV6Gateway": "fe76::1699:6f09:43dd:ffff",
    #   "IPV6PrefixLength": 64,
    #   "ParentInterface": "ens192",
    #   "VlanId": 76,
    #   "@odata.id": "/redfish/v1/SFSSApp/IpAddressManagements('ens192.76')",
    #   "@odata.type": "#IpAddressManagements.IpAddressManagements",
    #   "@odata.context": "/redfish/v1/SFSSApp/$metadata#IpAddressManagements/IpAddressManagements/$entity"
    # },
    # {
    #   "Interface": "ens192.77",
    #   "Type": "VLAN",
    #   "IPV4Address": [
    #       "77.1.1.2"
    #   ],
    #   "IPV4Config": "MANUAL",
    #   "IPV4Gateway": "77.1.1.254",
    #   "IPV4PrefixLength": 16,
    #   "IPV6Address": [
    #       "fe77::1699:6f09:43dd:56c2"
    #   ],
    #   "IPV6Config": "MANUAL",
    #   "IPV6Gateway": "fe77::1699:6f09:43dd:ffff",
    #   "IPV6PrefixLength": 77,
    #   "ParentInterface": "ens192",
    #   "VlanId": 77,
    #   "@odata.id": "/redfish/v1/SFSSApp/IpAddressManagements('ens192.77')",
    #   "@odata.type": "#IpAddressManagements.IpAddressManagements",
    #   "@odata.context": "/redfish/v1/SFSSApp/$metadata#IpAddressManagements/IpAddressManagements/$entity"
    # },
    # {
    #   "Interface": "ens192.74",
    #   "Type": "VLAN",
    #   "IPV4Address": [
    #       "74.1.1.2"
    #   ],
    #   "IPV4Config": "MANUAL",
    #   "IPV4Gateway": "74.1.1.254",
    #   "IPV4PrefixLength": 16,
    #   "IPV6Address": [
    #       "fe74::1699:6f09:43dd:56c2"
    #   ],
    #   "IPV6Config": "MANUAL",
    #   "IPV6Gateway": "fe74::1699:6f09:43dd:ffff",
    #   "IPV6PrefixLength": 74,
    #   "ParentInterface": "ens192",
    #   "VlanId": 74,
    #   "@odata.id": "/redfish/v1/SFSSApp/IpAddressManagements('ens192.74')",
    #   "@odata.type": "#IpAddressManagements.IpAddressManagements",
    #   "@odata.context": "/redfish/v1/SFSSApp/$metadata#IpAddressManagements/IpAddressManagements/$entity"
    # },
    # {
    #   "Interface": "ens192.64",
    #   "Type": "VLAN",
    #   "IPV4Config": "AUTOMATIC",
    #   "IPV6Config": "AUTOMATIC",
    #   "ParentInterface": "ens192",
    #   "VlanId": 64,
    #   "@odata.id": "/redfish/v1/SFSSApp/IpAddressManagements('ens192.64')",
    #   "@odata.type": "#IpAddressManagements.IpAddressManagements",
    #   "@odata.context": "/redfish/v1/SFSSApp/$metadata#IpAddressManagements/IpAddressManagements/$entity"
    # },
    # {
    #   "Interface": "ens192",
    #   "Type": "ETHERNET",
    #   "IPV4Config": "AUTOMATIC",
    #   "IPV6Config": "AUTOMATIC",
    #   "@odata.id": "/redfish/v1/SFSSApp/IpAddressManagements('ens192')",
    #   "@odata.type": "#IpAddressManagements.IpAddressManagements",
    #   "@odata.context": "/redfish/v1/SFSSApp/$metadata#IpAddressManagements/IpAddressManagements/$entity"
    # },
    # {
    #   "Interface": "ens160",
    #   "Type": "ETHERNET",
    #   "IPV4Address": [
    #       "100.104.26.127"
    #   ],
    #   "IPV4Config": "MANUAL",
    #   "IPV4Gateway": "100.104.26.254",
    #   "IPV4PrefixLength": 24,
    #   "IPV6Config": "AUTOMATIC",
    #   "@odata.id": "/redfish/v1/SFSSApp/IpAddressManagements('ens160')",
    #   "@odata.type": "#IpAddressManagements.IpAddressManagements",
    #   "@odata.context": "/redfish/v1/SFSSApp/$metadata#IpAddressManagements/IpAddressManagements/$entity"
    # },
    # {
    #   "Interface": "ens192.75",
    #   "Type": "VLAN",
    #   "IPV4Address": [
    #       "75.1.1.2"
    #   ],
    #   "IPV4Config": "MANUAL",
    #   "IPV4Gateway": "75.1.1.254",
    #   "IPV4PrefixLength": 16,
    #   "IPV6Address": [
    #       "fe75::1699:6f09:43dd:56c2"
    #   ],
    #   "IPV6Config": "MANUAL",
    #   "IPV6Gateway": "fe75::1699:6f09:43dd:ffff",
    #   "IPV6PrefixLength": 75,
    #   "ParentInterface": "ens192",
    #   "VlanId": 75,
    #   "@odata.id": "/redfish/v1/SFSSApp/IpAddressManagements('ens192.75')",
    #   "@odata.type": "#IpAddressManagements.IpAddressManagements",
    #   "@odata.context": "/redfish/v1/SFSSApp/$metadata#IpAddressManagements/IpAddressManagements/$entity"
    # }
    # ]
    #
    #
    # Using deleted
    #
    # Before state:
    # -------------
    #redfish/v1/SFSSApp/IpAddressManagements?$expand=IpAddressManagements
    # "IpAddressManagements": [
    # {
    #   "Interface": "ens192.51",
    #   "Type": "VLAN",
    #   "IPV4Address": [
    #       "52.1.1.2"
    #   ],
    #   "IPV4Config": "MANUAL",
    #   "IPV4Gateway": "52.1.1.254",
    #   "IPV4PrefixLength": 16,
    #   "IPV6Address": [
    #       "fe52::1699:6f09:43dd:56c2"
    #   ],
    #   "IPV6Config": "MANUAL",
    #   "IPV6Gateway": "fe52::1699:6f09:43dd:ffff",
    #   "IPV6PrefixLength": 64,
    #   "ParentInterface": "ens192",
    #   "VlanId": 51,
    #   "@odata.id": "/redfish/v1/SFSSApp/IpAddressManagements('ens192.51')",
    #   "@odata.type": "#IpAddressManagements.IpAddressManagements",
    #   "@odata.context": "/redfish/v1/SFSSApp/$metadata#IpAddressManagements/IpAddressManagements/$entity"
    # },
    # {
    #   "Interface": "ens192.76",
    #   "Type": "VLAN",
    #   "IPV4Address": [
    #       "76.1.1.2"
    #   ],
    #   "IPV4Config": "MANUAL",
    #   "IPV4Gateway": "76.1.1.254",
    #   "IPV4PrefixLength": 16,
    #   "IPV6Address": [
    #       "fe76::1699:6f09:43dd:56c2"
    #   ],
    #   "IPV6Config": "MANUAL",
    #   "IPV6Gateway": "fe76::1699:6f09:43dd:ffff",
    #   "IPV6PrefixLength": 64,
    #   "ParentInterface": "ens192",
    #   "VlanId": 76,
    #   "@odata.id": "/redfish/v1/SFSSApp/IpAddressManagements('ens192.76')",
    #   "@odata.type": "#IpAddressManagements.IpAddressManagements",
    #   "@odata.context": "/redfish/v1/SFSSApp/$metadata#IpAddressManagements/IpAddressManagements/$entity"
    # },
    # {
    #   "Interface": "ens192.77",
    #   "Type": "VLAN",
    #   "IPV4Address": [
    #       "77.1.1.2"
    #   ],
    #   "IPV4Config": "MANUAL",
    #   "IPV4Gateway": "77.1.1.254",
    #   "IPV4PrefixLength": 16,
    #   "IPV6Address": [
    #       "fe77::1699:6f09:43dd:56c2"
    #   ],
    #   "IPV6Config": "MANUAL",
    #   "IPV6Gateway": "fe77::1699:6f09:43dd:ffff",
    #   "IPV6PrefixLength": 77,
    #   "ParentInterface": "ens192",
    #   "VlanId": 77,
    #   "@odata.id": "/redfish/v1/SFSSApp/IpAddressManagements('ens192.77')",
    #   "@odata.type": "#IpAddressManagements.IpAddressManagements",
    #   "@odata.context": "/redfish/v1/SFSSApp/$metadata#IpAddressManagements/IpAddressManagements/$entity"
    # },
    # {
    #   "Interface": "ens192.74",
    #   "Type": "VLAN",
    #   "IPV4Address": [
    #       "74.1.1.2"
    #   ],
    #   "IPV4Config": "MANUAL",
    #   "IPV4Gateway": "74.1.1.254",
    #   "IPV4PrefixLength": 16,
    #   "IPV6Address": [
    #       "fe74::1699:6f09:43dd:56c2"
    #   ],
    #   "IPV6Config": "MANUAL",
    #   "IPV6Gateway": "fe74::1699:6f09:43dd:ffff",
    #   "IPV6PrefixLength": 74,
    #   "ParentInterface": "ens192",
    #   "VlanId": 74,
    #   "@odata.id": "/redfish/v1/SFSSApp/IpAddressManagements('ens192.74')",
    #   "@odata.type": "#IpAddressManagements.IpAddressManagements",
    #   "@odata.context": "/redfish/v1/SFSSApp/$metadata#IpAddressManagements/IpAddressManagements/$entity"
    # },
    # {
    #   "Interface": "ens192.64",
    #   "Type": "VLAN",
    #   "IPV4Config": "AUTOMATIC",
    #   "IPV6Config": "AUTOMATIC",
    #   "ParentInterface": "ens192",
    #   "VlanId": 64,
    #   "@odata.id": "/redfish/v1/SFSSApp/IpAddressManagements('ens192.64')",
    #   "@odata.type": "#IpAddressManagements.IpAddressManagements",
    #   "@odata.context": "/redfish/v1/SFSSApp/$metadata#IpAddressManagements/IpAddressManagements/$entity"
    # },
    # {
    #   "Interface": "ens192",
    #   "Type": "ETHERNET",
    #   "IPV4Config": "AUTOMATIC",
    #   "IPV6Config": "AUTOMATIC",
    #   "@odata.id": "/redfish/v1/SFSSApp/IpAddressManagements('ens192')",
    #   "@odata.type": "#IpAddressManagements.IpAddressManagements",
    #   "@odata.context": "/redfish/v1/SFSSApp/$metadata#IpAddressManagements/IpAddressManagements/$entity"
    # },
    # {
    #   "Interface": "ens160",
    #   "Type": "ETHERNET",
    #   "IPV4Address": [
    #       "100.104.26.127"
    #   ],
    #   "IPV4Config": "MANUAL",
    #   "IPV4Gateway": "100.104.26.254",
    #   "IPV4PrefixLength": 24,
    #   "IPV6Config": "AUTOMATIC",
    #   "@odata.id": "/redfish/v1/SFSSApp/IpAddressManagements('ens160')",
    #   "@odata.type": "#IpAddressManagements.IpAddressManagements",
    #   "@odata.context": "/redfish/v1/SFSSApp/$metadata#IpAddressManagements/IpAddressManagements/$entity"
    # },
    # {
    #   "Interface": "ens192.75",
    #   "Type": "VLAN",
    #   "IPV4Address": [
    #       "75.1.1.2"
    #   ],
    #   "IPV4Config": "MANUAL",
    #   "IPV4Gateway": "75.1.1.254",
    #   "IPV4PrefixLength": 16,
    #   "IPV6Address": [
    #       "fe75::1699:6f09:43dd:56c2"
    #   ],
    #   "IPV6Config": "MANUAL",
    #   "IPV6Gateway": "fe75::1699:6f09:43dd:ffff",
    #   "IPV6PrefixLength": 75,
    #   "ParentInterface": "ens192",
    #   "VlanId": 75,
    #   "@odata.id": "/redfish/v1/SFSSApp/IpAddressManagements('ens192.75')",
    #   "@odata.type": "#IpAddressManagements.IpAddressManagements",
    #   "@odata.context": "/redfish/v1/SFSSApp/$metadata#IpAddressManagements/IpAddressManagements/$entity"
    # }
    # ]
    - name: Stfs interface ip management
      dellemc.sfss.interface_ip_mgmt:
        config: []
        state: deleted
    #
    # After state:
    # ------------
    # redfish/v1/SFSSApp/IpAddressManagements?$expand=IpAddressManagements
    # {
    # "IpAddressManagements@odata.count": 0,
    # "@odata.id": "/redfish/v1/SFSSApp/IpAddressManagements?$expand=IpAddressManagements",
    # "@odata.context": "/redfish/v1/SFSSApp/$metadata#IpAddressManagements",
    # "@odata.type": "#IpAddressManagementsCollection.IpAddressManagementsCollection"
    # }
    #
    # Using merged
    #
    # Before state:
    # -------------
    #
    # redfish/v1/SFSSApp/IpAddressManagements?$expand=IpAddressManagements
    # "IpAddressManagements": [
    # {
    #   "Interface": "ens192.76",
    #   "Type": "VLAN",
    #   "IPV4Address": [
    #       "76.1.1.2"
    #   ],
    #   "IPV4Config": "MANUAL",
    #   "IPV4Gateway": "76.1.1.254",
    #   "IPV4PrefixLength": 16,
    #   "IPV6Address": [
    #       "fe76::1699:6f09:43dd:56c2"
    #   ],
    #   "IPV6Config": "MANUAL",
    #   "IPV6Gateway": "fe76::1699:6f09:43dd:ffff",
    #   "IPV6PrefixLength": 64,
    #   "ParentInterface": "ens192",
    #   "VlanId": 76,
    #   "@odata.id": "/redfish/v1/SFSSApp/IpAddressManagements('ens192.76')",
    #   "@odata.type": "#IpAddressManagements.IpAddressManagements",
    #   "@odata.context": "/redfish/v1/SFSSApp/$metadata#IpAddressManagements/IpAddressManagements/$entity"
    # },
    # {
    #   "Interface": "ens192.77",
    #   "Type": "VLAN",
    #   "IPV4Address": [
    #       "77.1.1.2"
    #   ],
    #   "IPV4Config": "MANUAL",
    #   "IPV4Gateway": "77.1.1.254",
    #   "IPV4PrefixLength": 16,
    #   "IPV6Address": [
    #       "fe77::1699:6f09:43dd:56c2"
    #   ],
    #   "IPV6Config": "MANUAL",
    #   "IPV6Gateway": "fe77::1699:6f09:43dd:ffff",
    #   "IPV6PrefixLength": 77,
    #   "ParentInterface": "ens192",
    #   "VlanId": 77,
    #   "@odata.id": "/redfish/v1/SFSSApp/IpAddressManagements('ens192.77')",
    #   "@odata.type": "#IpAddressManagements.IpAddressManagements",
    #   "@odata.context": "/redfish/v1/SFSSApp/$metadata#IpAddressManagements/IpAddressManagements/$entity"
    # },
    # {
    #   "Interface": "ens192.74",
    #   "Type": "VLAN",
    #   "IPV4Address": [
    #       "74.1.1.2"
    #   ],
    #   "IPV4Config": "MANUAL",
    #   "IPV4Gateway": "74.1.1.254",
    #   "IPV4PrefixLength": 16,
    #   "IPV6Address": [
    #       "fe74::1699:6f09:43dd:56c2"
    #   ],
    #   "IPV6Config": "MANUAL",
    #   "IPV6Gateway": "fe74::1699:6f09:43dd:ffff",
    #   "IPV6PrefixLength": 74,
    #   "ParentInterface": "ens192",
    #   "VlanId": 74,
    #   "@odata.id": "/redfish/v1/SFSSApp/IpAddressManagements('ens192.74')",
    #   "@odata.type": "#IpAddressManagements.IpAddressManagements",
    #   "@odata.context": "/redfish/v1/SFSSApp/$metadata#IpAddressManagements/IpAddressManagements/$entity"
    # },
    # {
    #   "Interface": "ens192.64",
    #   "Type": "VLAN",
    #   "IPV4Config": "AUTOMATIC",
    #   "IPV6Config": "AUTOMATIC",
    #   "ParentInterface": "ens192",
    #   "VlanId": 64,
    #   "@odata.id": "/redfish/v1/SFSSApp/IpAddressManagements('ens192.64')",
    #   "@odata.type": "#IpAddressManagements.IpAddressManagements",
    #   "@odata.context": "/redfish/v1/SFSSApp/$metadata#IpAddressManagements/IpAddressManagements/$entity"
    # },
    # {
    #   "Interface": "ens192",
    #   "Type": "ETHERNET",
    #   "IPV4Config": "AUTOMATIC",
    #   "IPV6Config": "AUTOMATIC",
    #   "@odata.id": "/redfish/v1/SFSSApp/IpAddressManagements('ens192')",
    #   "@odata.type": "#IpAddressManagements.IpAddressManagements",
    #   "@odata.context": "/redfish/v1/SFSSApp/$metadata#IpAddressManagements/IpAddressManagements/$entity"
    # },
    # {
    #   "Interface": "ens160",
    #   "Type": "ETHERNET",
    #   "IPV4Address": [
    #       "100.104.26.127"
    #   ],
    #   "IPV4Config": "MANUAL",
    #   "IPV4Gateway": "100.104.26.254",
    #   "IPV4PrefixLength": 24,
    #   "IPV6Config": "AUTOMATIC",
    #   "@odata.id": "/redfish/v1/SFSSApp/IpAddressManagements('ens160')",
    #   "@odata.type": "#IpAddressManagements.IpAddressManagements",
    #   "@odata.context": "/redfish/v1/SFSSApp/$metadata#IpAddressManagements/IpAddressManagements/$entity"
    # },
    # {
    #   "Interface": "ens192.75",
    #   "Type": "VLAN",
    #   "IPV4Address": [
    #       "75.1.1.2"
    #   ],
    #   "IPV4Config": "MANUAL",
    #   "IPV4Gateway": "75.1.1.254",
    #   "IPV4PrefixLength": 16,
    #   "IPV6Address": [
    #       "fe75::1699:6f09:43dd:56c2"
    #   ],
    #   "IPV6Config": "MANUAL",
    #   "IPV6Gateway": "fe75::1699:6f09:43dd:ffff",
    #   "IPV6PrefixLength": 75,
    #   "ParentInterface": "ens192",
    #   "VlanId": 75,
    #   "@odata.id": "/redfish/v1/SFSSApp/IpAddressManagements('ens192.75')",
    #   "@odata.type": "#IpAddressManagements.IpAddressManagements",
    #   "@odata.context": "/redfish/v1/SFSSApp/$metadata#IpAddressManagements/IpAddressManagements/$entity"
    # }
    # ]
    - name: Stfs interface ip management
      dellemc.sfss.interface_ip_mgmt:
        config:
        - ipv4_address: 52.1.1.2
          ipv4_config_type: manual
          ipv4_gateway: 52.1.1.254
          ipv4_netmask: 16
          ipv6_address: fe52::1699:6f09:43dd:56c2
          ipv6_config_type: manual
          ipv6_gateway: fe52::1699:6f09:43dd:ffff
          ipv6_netmask: 64
          parent_interface: ens192
          vlan_id: 51
    #
    # After state:
    # -------------
    #
    # redfish/v1/SFSSApp/IpAddressManagements?$expand=IpAddressManagements
    # "IpAddressManagements": [
    # {
    #   "Interface": "ens192.51",
    #   "Type": "VLAN",
    #   "IPV4Address": [
    #       "52.1.1.2"
    #   ],
    #   "IPV4Config": "MANUAL",
    #   "IPV4Gateway": "52.1.1.254",
    #   "IPV4PrefixLength": 16,
    #   "IPV6Address": [
    #       "fe52::1699:6f09:43dd:56c2"
    #   ],
    #   "IPV6Config": "MANUAL",
    #   "IPV6Gateway": "fe52::1699:6f09:43dd:ffff",
    #   "IPV6PrefixLength": 64,
    #   "ParentInterface": "ens192",
    #   "VlanId": 51,
    #   "@odata.id": "/redfish/v1/SFSSApp/IpAddressManagements('ens192.51')",
    #   "@odata.type": "#IpAddressManagements.IpAddressManagements",
    #   "@odata.context": "/redfish/v1/SFSSApp/$metadata#IpAddressManagements/IpAddressManagements/$entity"
    # },
    # {
    #   "Interface": "ens192.76",
    #   "Type": "VLAN",
    #   "IPV4Address": [
    #       "76.1.1.2"
    #   ],
    #   "IPV4Config": "MANUAL",
    #   "IPV4Gateway": "76.1.1.254",
    #   "IPV4PrefixLength": 16,
    #   "IPV6Address": [
    #       "fe76::1699:6f09:43dd:56c2"
    #   ],
    #   "IPV6Config": "MANUAL",
    #   "IPV6Gateway": "fe76::1699:6f09:43dd:ffff",
    #   "IPV6PrefixLength": 64,
    #   "ParentInterface": "ens192",
    #   "VlanId": 76,
    #   "@odata.id": "/redfish/v1/SFSSApp/IpAddressManagements('ens192.76')",
    #   "@odata.type": "#IpAddressManagements.IpAddressManagements",
    #   "@odata.context": "/redfish/v1/SFSSApp/$metadata#IpAddressManagements/IpAddressManagements/$entity"
    # },
    # {
    #   "Interface": "ens192.77",
    #   "Type": "VLAN",
    #   "IPV4Address": [
    #       "77.1.1.2"
    #   ],
    #   "IPV4Config": "MANUAL",
    #   "IPV4Gateway": "77.1.1.254",
    #   "IPV4PrefixLength": 16,
    #   "IPV6Address": [
    #       "fe77::1699:6f09:43dd:56c2"
    #   ],
    #   "IPV6Config": "MANUAL",
    #   "IPV6Gateway": "fe77::1699:6f09:43dd:ffff",
    #   "IPV6PrefixLength": 77,
    #   "ParentInterface": "ens192",
    #   "VlanId": 77,
    #   "@odata.id": "/redfish/v1/SFSSApp/IpAddressManagements('ens192.77')",
    #   "@odata.type": "#IpAddressManagements.IpAddressManagements",
    #   "@odata.context": "/redfish/v1/SFSSApp/$metadata#IpAddressManagements/IpAddressManagements/$entity"
    # },
    # {
    #   "Interface": "ens192.74",
    #   "Type": "VLAN",
    #   "IPV4Address": [
    #       "74.1.1.2"
    #   ],
    #   "IPV4Config": "MANUAL",
    #   "IPV4Gateway": "74.1.1.254",
    #   "IPV4PrefixLength": 16,
    #   "IPV6Address": [
    #       "fe74::1699:6f09:43dd:56c2"
    #   ],
    #   "IPV6Config": "MANUAL",
    #   "IPV6Gateway": "fe74::1699:6f09:43dd:ffff",
    #   "IPV6PrefixLength": 74,
    #   "ParentInterface": "ens192",
    #   "VlanId": 74,
    #   "@odata.id": "/redfish/v1/SFSSApp/IpAddressManagements('ens192.74')",
    #   "@odata.type": "#IpAddressManagements.IpAddressManagements",
    #   "@odata.context": "/redfish/v1/SFSSApp/$metadata#IpAddressManagements/IpAddressManagements/$entity"
    # },
    # {
    #   "Interface": "ens192.64",
    #   "Type": "VLAN",
    #   "IPV4Config": "AUTOMATIC",
    #   "IPV6Config": "AUTOMATIC",
    #   "ParentInterface": "ens192",
    #   "VlanId": 64,
    #   "@odata.id": "/redfish/v1/SFSSApp/IpAddressManagements('ens192.64')",
    #   "@odata.type": "#IpAddressManagements.IpAddressManagements",
    #   "@odata.context": "/redfish/v1/SFSSApp/$metadata#IpAddressManagements/IpAddressManagements/$entity"
    # },
    # {
    #   "Interface": "ens192",
    #   "Type": "ETHERNET",
    #   "IPV4Config": "AUTOMATIC",
    #   "IPV6Config": "AUTOMATIC",
    #   "@odata.id": "/redfish/v1/SFSSApp/IpAddressManagements('ens192')",
    #   "@odata.type": "#IpAddressManagements.IpAddressManagements",
    #   "@odata.context": "/redfish/v1/SFSSApp/$metadata#IpAddressManagements/IpAddressManagements/$entity"
    # },
    # {
    #   "Interface": "ens160",
    #   "Type": "ETHERNET",
    #   "IPV4Address": [
    #       "100.104.26.127"
    #   ],
    #   "IPV4Config": "MANUAL",
    #   "IPV4Gateway": "100.104.26.254",
    #   "IPV4PrefixLength": 24,
    #   "IPV6Config": "AUTOMATIC",
    #   "@odata.id": "/redfish/v1/SFSSApp/IpAddressManagements('ens160')",
    #   "@odata.type": "#IpAddressManagements.IpAddressManagements",
    #   "@odata.context": "/redfish/v1/SFSSApp/$metadata#IpAddressManagements/IpAddressManagements/$entity"
    # },
    # {
    #   "Interface": "ens192.75",
    #   "Type": "VLAN",
    #   "IPV4Address": [
    #       "75.1.1.2"
    #   ],
    #   "IPV4Config": "MANUAL",
    #   "IPV4Gateway": "75.1.1.254",
    #   "IPV4PrefixLength": 16,
    #   "IPV6Address": [
    #       "fe75::1699:6f09:43dd:56c2"
    #   ],
    #   "IPV6Config": "MANUAL",
    #   "IPV6Gateway": "fe75::1699:6f09:43dd:ffff",
    #   "IPV6PrefixLength": 75,
    #   "ParentInterface": "ens192",
    #   "VlanId": 75,
    #   "@odata.id": "/redfish/v1/SFSSApp/IpAddressManagements('ens192.75')",
    #   "@odata.type": "#IpAddressManagements.IpAddressManagements",
    #   "@odata.context": "/redfish/v1/SFSSApp/$metadata#IpAddressManagements/IpAddressManagements/$entity"
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

