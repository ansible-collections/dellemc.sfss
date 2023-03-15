.. _sfss_security_authentication_module:


sfss_security_authentication -- Manage remote RADIUS and TACACS servers
=======================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

This module is used to manage remote RADIUS and TACACS servers and to define the authentication sequence.






Parameters
----------

  config (optional, list, None)
    A list of authentication servers.


    authentication_sequence (True, list, None)
      The authentication sequence list.


    authentication_servers (optional, list, None)
      Details of the authentication servers.


      server_ip (optional, str, None)
        Server IP address.


      password (optional, str, None)
        Server password.


      authentication_type (True, str, None)
        Authentication type.




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
    # Before state:
    # -------------
    #
    # redfish/v1/SFSSApp/RadiusServers
    # "RadiusServers": [
    # {
    #     "ServerIp": "3.3.3.3",
    #     "ServerPass": "6c8hua7A3Sc5ZS6aoviDPFbOt04XgOIrTPnY2F5Or0pt1jGSF6DQTisPQFQRsxuo",
    #     "@odata.id": "/redfish/v1/SFSSApp/RadiusServers('3.3.3.3')",
    #     "@odata.type": "#RadiusServers.RadiusServers",
    #     "@odata.context": "/redfish/v1/SFSSApp/$metadata#RadiusServers/RadiusServers/$entity"
    # },
    # {
    #     "ServerIp": "1.1.1.1",
    #     "ServerPass": "+h7vBfukV+dybhSrCC1dG5bamPlNBEZqW2iBIXCLaHf2jlEd44ToqI5y63vCwFbR",
    #     "@odata.id": "/redfish/v1/SFSSApp/RadiusServers('1.1.1.1')",
    #     "@odata.type": "#RadiusServers.RadiusServers",
    #     "@odata.context": "/redfish/v1/SFSSApp/$metadata#RadiusServers/RadiusServers/$entity"
    # },
    # {
    #     "ServerIp": "2.3.4.5",
    #     "ServerPass": "+05QvIgOaO5zsQ6kY4o6/SL3xBk4Wif81ZpONVPqUSiPIl86qrvqkQPwmlNnRdu1",
    #     "@odata.id": "/redfish/v1/SFSSApp/RadiusServers('2.3.4.5')",
    #     "@odata.type": "#RadiusServers.RadiusServers",
    #     "@odata.context": "/redfish/v1/SFSSApp/$metadata#RadiusServers/RadiusServers/$entity"
    # }
    # ]
    #
    - name: security auth create
      dellemc.sfss.security_authentication:
        config:
          - authentication_sequence: ["local"]
            authentication_servers:
            - authentication_type: "radius"
              server_ip: "1.1.1.1"
              password: "xxxx"
        state: deleted
    #
    # After state:
    # ------------
    # redfish/v1/SFSSApp/RadiusServers
    # "RadiusServers": [
    # {
    #   "ServerIp": "3.3.3.3",
    #   "ServerPass": "6c8hua7A3Sc5ZS6aoviDPFbOt04XgOIrTPnY2F5Or0pt1jGSF6DQTisPQFQRsxuo",
    #   "@odata.id": "/redfish/v1/SFSSApp/RadiusServers('3.3.3.3')",
    #   "@odata.type": "#RadiusServers.RadiusServers",
    #   "@odata.context": "/redfish/v1/SFSSApp/$metadata#RadiusServers/RadiusServers/$entity"
    # },
    # {
    #   "ServerIp": "2.3.4.5",
    #   "ServerPass": "+05QvIgOaO5zsQ6kY4o6/SL3xBk4Wif81ZpONVPqUSiPIl86qrvqkQPwmlNnRdu1",
    #   "@odata.id": "/redfish/v1/SFSSApp/RadiusServers('2.3.4.5')",
    #   "@odata.type": "#RadiusServers.RadiusServers",
    #   "@odata.context": "/redfish/v1/SFSSApp/$metadata#RadiusServers/RadiusServers/$entity"
    # }
    # ]

    # Using deleted
    #
    # Before state:
    # -------------
    #
    # redfish/v1/SFSSApp/RadiusServers
    # "RadiusServers": [
    # {
    #   "ServerIp": "10.1.1.1",
    #   "ServerPass": "2+YGyhuqn5Kn3TWYbwZu+yWtLBhM97+pAsMG+L/Sd1qTJdSwBq7i0PM1RNW6pmtb",
    #   "@odata.id": "/redfish/v1/SFSSApp/RadiusServers('10.1.1.1')",
    #   "@odata.type": "#RadiusServers.RadiusServers",
    #   "@odata.context": "/redfish/v1/SFSSApp/$metadata#RadiusServers/RadiusServers/$entity"
    # },
    # {
    #   "ServerIp": "21.1.1.1",
    #   "ServerPass": "+RgniIfG21lRvtWqTZEAZKm3ParQWdtFYf+g6YUWavhVpPfUxPcEoO+ntE43A6yq",
    #   "@odata.id": "/redfish/v1/SFSSApp/RadiusServers('21.1.1.1')",
    #   "@odata.type": "#RadiusServers.RadiusServers",
    #   "@odata.context": "/redfish/v1/SFSSApp/$metadata#RadiusServers/RadiusServers/$entity"
    # },
    # {
    #   "ServerIp": "2.3.4.5",
    #   "ServerPass": "+05QvIgOaO5zsQ6kY4o6/SL3xBk4Wif81ZpONVPqUSiPIl86qrvqkQPwmlNnRdu1",
    #   "@odata.id": "/redfish/v1/SFSSApp/RadiusServers('2.3.4.5')",
    #   "@odata.type": "#RadiusServers.RadiusServers",
    #   "@odata.context": "/redfish/v1/SFSSApp/$metadata#RadiusServers/RadiusServers/$entity"
    # },
    # {
    #   "ServerIp": "1.1.1.1",
    #   "ServerPass": "vDYv9ApwdJFVeoFvu8BfL1FuA44ivP1+yfgP9f4wRSln6/9c+XRC1WMPaHE6wsFD",
    #   "@odata.id": "/redfish/v1/SFSSApp/RadiusServers('1.1.1.1')",
    #   "@odata.type": "#RadiusServers.RadiusServers",
    #   "@odata.context": "/redfish/v1/SFSSApp/$metadata#RadiusServers/RadiusServers/$entity"
    # },
    # {
    #   "ServerIp": "3.3.3.3",
    #   "ServerPass": "6c8hua7A3Sc5ZS6aoviDPFbOt04XgOIrTPnY2F5Or0pt1jGSF6DQTisPQFQRsxuo",
    #   "@odata.id": "/redfish/v1/SFSSApp/RadiusServers('3.3.3.3')",
    #   "@odata.type": "#RadiusServers.RadiusServers",
    #   "@odata.context": "/redfish/v1/SFSSApp/$metadata#RadiusServers/RadiusServers/$entity"
    # }
    # ]

    #redfish/v1/SFSSApp/TacacsServers
    # "TacacsServers": [
    # {
    #   "ServerIp": "2.2.2.2",
    #   "ServerPass": "MkNgvF14iIDJXGxfAnDABawtiFQ6/rLrahcr1d2KaQNt9i4NVAOQxwieDYYYl6y+",
    #   "@odata.id": "/redfish/v1/SFSSApp/TacacsServers('2.2.2.2')",
    #   "@odata.type": "#TacacsServers.TacacsServers",
    #   "@odata.context": "/redfish/v1/SFSSApp/$metadata#TacacsServers/TacacsServers/$entity"
    # },
    # {
    #   "ServerIp": "60.8.8.8",
    #   "ServerPass": "iBQbXHDIVRkfeYA2NWQj3b/yvUFmWnerNttUxQQK2XNByc/CqXQSne+Wyjh9qck1",
    #   "@odata.id": "/redfish/v1/SFSSApp/TacacsServers('60.8.8.8')",
    #   "@odata.type": "#TacacsServers.TacacsServers",
    #   "@odata.context": "/redfish/v1/SFSSApp/$metadata#TacacsServers/TacacsServers/$entity"
    # },
    # {
    #   "ServerIp": "11.1.1.1",
    #   "ServerPass": "DRRUDxiwdzYNLH+2DyxoR7qR07RYUfVZcwSWGdeHPo/8b8Ykr6YjJ7DhpOpMaV09",
    #   "@odata.id": "/redfish/v1/SFSSApp/TacacsServers('11.1.1.1')",
    #   "@odata.type": "#TacacsServers.TacacsServers",
    #   "@odata.context": "/redfish/v1/SFSSApp/$metadata#TacacsServers/TacacsServers/$entity"
    # }
    # ]
    - name: security auth create
      dellemc.sfss.security_authentication:
        config: []
        state: deleted
    #
    # After state:
    # ------------
    #redfish/v1/SFSSApp/RadiusServers
    # {
    #   "RadiusServers@odata.count": 0,
    #   "@odata.id": "/redfish/v1/SFSSApp/RadiusServers?$expand=RadiusServers",
    #   "@odata.context": "/redfish/v1/SFSSApp/$metadata#RadiusServers",
    #   "@odata.type": "#RadiusServersCollection.RadiusServersCollection"
    # }
    #redfish/v1/SFSSApp/TacacsServers
    # {
    #   "TacacsServers@odata.count": 0,
    #   "@odata.id": "/redfish/v1/SFSSApp/TacacsServers?$expand=TacacsServers",
    #   "@odata.context": "/redfish/v1/SFSSApp/$metadata#TacacsServers",
    #   "@odata.type": "#TacacsServersCollection.TacacsServersCollection"
    # }
    # Using merged
    #
    # Before state:
    # -------------
    #
    # redfish/v1/SFSSApp/RadiusServers
    # "RadiusServers": [
    # {
    #   "ServerIp": "3.3.3.3",
    #   "ServerPass": "6c8hua7A3Sc5ZS6aoviDPFbOt04XgOIrTPnY2F5Or0pt1jGSF6DQTisPQFQRsxuo",
    #   "@odata.id": "/redfish/v1/SFSSApp/RadiusServers('3.3.3.3')",
    #   "@odata.type": "#RadiusServers.RadiusServers",
    #   "@odata.context": "/redfish/v1/SFSSApp/$metadata#RadiusServers/RadiusServers/$entity"
    # },
    # {
    #   "ServerIp": "2.3.4.5",
    #   "ServerPass": "+05QvIgOaO5zsQ6kY4o6/SL3xBk4Wif81ZpONVPqUSiPIl86qrvqkQPwmlNnRdu1",
    #   "@odata.id": "/redfish/v1/SFSSApp/RadiusServers('2.3.4.5')",
    #   "@odata.type": "#RadiusServers.RadiusServers",
    #   "@odata.context": "/redfish/v1/SFSSApp/$metadata#RadiusServers/RadiusServers/$entity"
    # }
    # ]
    #
    - name: security auth create
      dellemc.sfss.security_authentication:
        config:
          - authentication_sequence: ["local"]
            authentication_servers:
            - authentication_type: "radius"
              server_ip: "1.1.1.1"
              password: "xxxx"
    #
    # After state:
    # ------------
    # redfish/v1/SFSSApp/RadiusServers
    # "RadiusServers": [
    # {
    #   "ServerIp": "3.3.3.3",
    #   "ServerPass": "6c8hua7A3Sc5ZS6aoviDPFbOt04XgOIrTPnY2F5Or0pt1jGSF6DQTisPQFQRsxuo",
    #   "@odata.id": "/redfish/v1/SFSSApp/RadiusServers('3.3.3.3')",
    #   "@odata.type": "#RadiusServers.RadiusServers",
    #   "@odata.context": "/redfish/v1/SFSSApp/$metadata#RadiusServers/RadiusServers/$entity"
    # },
    # {
    #   "ServerIp": "1.1.1.1",
    #   "ServerPass": "vDYv9ApwdJFVeoFvu8BfL1FuA44ivP1+yfgP9f4wRSln6/9c+XRC1WMPaHE6wsFD",
    #   "@odata.id": "/redfish/v1/SFSSApp/RadiusServers('1.1.1.1')",
    #   "@odata.type": "#RadiusServers.RadiusServers",
    #   "@odata.context": "/redfish/v1/SFSSApp/$metadata#RadiusServers/RadiusServers/$entity"
    # },
    # {
    #   "ServerIp": "2.3.4.5",
    #   "ServerPass": "+05QvIgOaO5zsQ6kY4o6/SL3xBk4Wif81ZpONVPqUSiPIl86qrvqkQPwmlNnRdu1",
    #   "@odata.id": "/redfish/v1/SFSSApp/RadiusServers('2.3.4.5')",
    #   "@odata.type": "#RadiusServers.RadiusServers",
    #   "@odata.context": "/redfish/v1/SFSSApp/$metadata#RadiusServers/RadiusServers/$entity"
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

- Namrata Chatterjee (@nchatterjee)

