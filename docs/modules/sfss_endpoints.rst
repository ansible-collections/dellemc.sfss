.. _sfss_endpoints_module:


sfss_endpoints -- Manage SFSS endpoint attributes
=================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

This module is used to manage SFSS endpoint attributes. Use this module to add hosts, subsystems, and direct discovery controllers (DDCs) to SFSS.






Parameters
----------

  config (optional, list, None)
    A list of endpoints.


    instance_id (True, int, None)
      Instance ID.


    type (True, str, None)
      Type of endpoints.


    transport_address (True, str, None)
      Transport IP address of endpoints such as hosts, direct discovery controllers (DDCs), and subsystems.


    transport_address_family (True, str, None)
      Transport IP address type of endpoints such as hosts, DDCs, and subsystems.


    transport_type (optional, str, tcp)
      Transport type UDP or TCP.


    transport_service_id (optional, str, None)
      Transport service ID.


    port_id (optional, int, 0)
      Transport port ID.


    nqn_id (optional, str, None)
      NQN ID.


    ddc_activate (optional, bool, None)
      Activate DDC.



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
    #redfish/v1/SFSS/1/Hosts?$expand=Hosts
    # "Hosts": [
    # {
    #     "EId": "nqn.2014-08.org.nvmexpress:uuid:host@1.2.3.4:5452:TCP",
    #     "NQN": "nqn.2014-08.org.nvmexpress:uuid:host",
    #     "TransportAddress": "1.2.3.4",
    #     "TransportAddressFamily": "IPV4",
    #     "PortId": 5452,
    #     "TransportType": "TCP",
    #     "TREQ": 0,
    #     "TSAS": 0,
    #     "RegistrationType": "Manual",
    #     "ConnectionStatus": "Offline",
    #     "@odata.id": "/redfish/v1/SFSS/1/Hosts('nqn.2014-08.org.nvmexpress:uuid:host@1.2.3.4:5452:TCP')",
    #     "@odata.type": "#Hosts.Hosts",
    #     "@odata.context": "/redfish/v1/SFSS/1/$metadata#Hosts/Hosts/$entity"
    # },
    # {
    #     "EId": "@<3::1>:3454:TCP",
    #     "TransportAddress": "3::1",
    #     "TransportAddressFamily": "IPV6",
    #     "PortId": 3454,
    #     "TransportType": "TCP",
    #     "TREQ": 0,
    #     "TSAS": 0,
    #     "RegistrationType": "Manual",
    #     "ConnectionStatus": "Offline",
    #     "@odata.id": "/redfish/v1/SFSS/1/Hosts('@<3::1>:3454:TCP')",
    #     "@odata.type": "#Hosts.Hosts",
    #     "@odata.context": "/redfish/v1/SFSS/1/$metadata#Hosts/Hosts/$entity"
    # }
    # ]
    - name: Stfs endpoints create
      dellemc.sfss.endpoints:
        config:
        - type: host
          instance_id: 1
          port_id: 3454
          transport_address: 3::1
          transport_address_family: ipv6
        state: deleted
    #
    # After state:
    # -------------
    #
    #redfish/v1/SFSS/1/Hosts?$expand=Hosts
    # "Hosts": [
    # {
    #     "EId": "nqn.2014-08.org.nvmexpress:uuid:host@1.2.3.4:5452:TCP",
    #     "NQN": "nqn.2014-08.org.nvmexpress:uuid:host",
    #     "TransportAddress": "1.2.3.4",
    #     "TransportAddressFamily": "IPV4",
    #     "PortId": 5452,
    #     "TransportType": "TCP",
    #     "TREQ": 0,
    #     "TSAS": 0,
    #     "RegistrationType": "Manual",
    #     "ConnectionStatus": "Offline",
    #     "@odata.id": "/redfish/v1/SFSS/1/Hosts('nqn.2014-08.org.nvmexpress:uuid:host@1.2.3.4:5452:TCP')",
    #     "@odata.type": "#Hosts.Hosts",
    #     "@odata.context": "/redfish/v1/SFSS/1/$metadata#Hosts/Hosts/$entity"
    # }
    # ]

    # Using deleted
    #
    # Before state:
    # -------------
    #
    #redfish/v1/SFSS/1/Hosts?$expand=Hosts
    # "Hosts": [
    # {
    #     "EId": "nqn.2014-08.org.nvmexpress:uuid:host@1.2.3.4:5452:TCP",
    #     "NQN": "nqn.2014-08.org.nvmexpress:uuid:host",
    #     "TransportAddress": "1.2.3.4",
    #     "TransportAddressFamily": "IPV4",
    #     "PortId": 5452,
    #     "TransportType": "TCP",
    #     "TREQ": 0,
    #     "TSAS": 0,
    #     "RegistrationType": "Manual",
    #     "ConnectionStatus": "Offline",
    #     "@odata.id": "/redfish/v1/SFSS/1/Hosts('nqn.2014-08.org.nvmexpress:uuid:host@1.2.3.4:5452:TCP')",
    #     "@odata.type": "#Hosts.Hosts",
    #     "@odata.context": "/redfish/v1/SFSS/1/$metadata#Hosts/Hosts/$entity"
    # },
    # {
    #     "EId": "@<3::1>:3454:TCP",
    #     "TransportAddress": "3::1",
    #     "TransportAddressFamily": "IPV6",
    #     "PortId": 3454,
    #     "TransportType": "TCP",
    #     "TREQ": 0,
    #     "TSAS": 0,
    #     "RegistrationType": "Manual",
    #     "ConnectionStatus": "Offline",
    #     "@odata.id": "/redfish/v1/SFSS/1/Hosts('@<3::1>:3454:TCP')",
    #     "@odata.type": "#Hosts.Hosts",
    #     "@odata.context": "/redfish/v1/SFSS/1/$metadata#Hosts/Hosts/$entity"
    # }
    # ]
    - name: Stfs endpoints create
      dellemc.sfss.endpoints:
        config: []
        state: deleted
    #
    # After state:
    # -------------
    #
    #redfish/v1/SFSS/1/Hosts?$expand=Hosts
    # {
    #   "Hosts@odata.count": 0,
    #   "@odata.id": "/redfish/v1/SFSS/1/Hosts?$expand=Hosts",
    #   "@odata.context": "/redfish/v1/SFSS/1/$metadata#Hosts",
    #   "@odata.type": "#HostsCollection.HostsCollection"
    # }
    #redfish/v1/SFSS/1/DDCs?$expand=DDCs
    # {
    #     "DDCs@odata.count": 0,
    #     "@odata.id": "/redfish/v1/SFSS/1/DDCs?$expand=DDCs",
    #     "@odata.context": "/redfish/v1/SFSS/1/$metadata#DDCs",
    #     "@odata.type": "#DDCsCollection.DDCsCollection"
    # }
    #redfish/v1/SFSS/1/Subsystems?$expand=Subsystems
    # {
    #     "Subsystems@odata.count": 0,
    #     "@odata.id": "/redfish/v1/SFSS/1/Subsystems?$expand=Subsystems",
    #     "@odata.context": "/redfish/v1/SFSS/1/$metadata#Subsystems",
    #     "@odata.type": "#SubsystemsCollection.SubsystemsCollection"
    # }

    # Using merged
    #
    # Before state:
    # -------------
    #
    #redfish/v1/SFSS/1/Hosts?$expand=Hosts
    # "Hosts": [
    # {
    #   "EId": "nqn.2014-08.org.nvmexpress:uuid:host@1.2.3.4:5452:TCP",
    #   "NQN": "nqn.2014-08.org.nvmexpress:uuid:host",
    #   "TransportAddress": "1.2.3.4",
    #   "TransportAddressFamily": "IPV4",
    #   "PortId": 5452,
    #   "TransportType": "TCP",
    #   "TREQ": 0,
    #   "TSAS": 0,
    #   "RegistrationType": "Manual",
    #   "ConnectionStatus": "Offline",
    #   "@odata.id": "/redfish/v1/SFSS/1/Hosts('nqn.2014-08.org.nvmexpress:uuid:host@1.2.3.4:5452:TCP')",
    #   "@odata.type": "#Hosts.Hosts",
    #   "@odata.context": "/redfish/v1/SFSS/1/$metadata#Hosts/Hosts/$entity"
    # }
    # ]
    - name: Stfs endpoints create
      dellemc.sfss.endpoints:
        config:
        - type: host
          instance_id: 1
          port_id: 3454
          transport_address: 3::1
          transport_address_family: ipv6
    #
    # After state:
    # -------------
    #
    #redfish/v1/SFSS/1/Hosts?$expand=Hosts
    # "Hosts": [
    # {
    #     "EId": "nqn.2014-08.org.nvmexpress:uuid:host@1.2.3.4:5452:TCP",
    #     "NQN": "nqn.2014-08.org.nvmexpress:uuid:host",
    #     "TransportAddress": "1.2.3.4",
    #     "TransportAddressFamily": "IPV4",
    #     "PortId": 5452,
    #     "TransportType": "TCP",
    #     "TREQ": 0,
    #     "TSAS": 0,
    #     "RegistrationType": "Manual",
    #     "ConnectionStatus": "Offline",
    #     "@odata.id": "/redfish/v1/SFSS/1/Hosts('nqn.2014-08.org.nvmexpress:uuid:host@1.2.3.4:5452:TCP')",
    #     "@odata.type": "#Hosts.Hosts",
    #     "@odata.context": "/redfish/v1/SFSS/1/$metadata#Hosts/Hosts/$entity"
    # },
    # {
    #     "EId": "@<3::1>:3454:TCP",
    #     "TransportAddress": "3::1",
    #     "TransportAddressFamily": "IPV6",
    #     "PortId": 3454,
    #     "TransportType": "TCP",
    #     "TREQ": 0,
    #     "TSAS": 0,
    #     "RegistrationType": "Manual",
    #     "ConnectionStatus": "Offline",
    #     "@odata.id": "/redfish/v1/SFSS/1/Hosts('@<3::1>:3454:TCP')",
    #     "@odata.type": "#Hosts.Hosts",
    #     "@odata.context": "/redfish/v1/SFSS/1/$metadata#Hosts/Hosts/$entity"
    # }
    # ]



Return Values
-------------

before (always, list, ['EId:@<3::1>:3454:TCP', 'TransportAddress:3::1', 'TransportAddressFamily:IPV6', 'PortId:3454'])
  The configuration prior to the model invocation.


after (when changed, list, ['EId:@<3::1>:3454:TCP', 'TransportAddress:3::1', 'TransportAddressFamily:IPV6', 'PortId:3454'])
  The resulting configuration model invocation.


commands (always, list, ['command 1', 'command 2', 'command 3'])
  The set of commands pushed to the remote device.





Status
------





Authors
~~~~~~~

- Mohamed Javeed (@javeedf)

