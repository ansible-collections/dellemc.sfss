.. _sfss_global_policies_module:


sfss_global_policies -- This module manages attributes of sfss Global Policies
==============================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

This module manages attributes of sfss Global Policies






Parameters
----------

  config (optional, list, None)
    A list of link aggregation group configurations.


    instance_id (True, int, None)
      The instance identifier


    zoning_policy (optional, bool, None)
      Zoning policy enable or disable


    NameServerEntityPurgeTOV (optional, str, None)
      Timeout value of name server entity



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

    
    # Using merged
    #
    # Before state:
    # -------------
    #
    #redfish/v1/SFSS/1/GlobalPolicies
    # {
    #   "ZoningPolicy": "Disable",
    #   "NameServerEntityPurgeTOV": "48Hr",
    #   "@odata.id": "/redfish/v1/SFNC/2/GlobalPolicies",
    #   "@odata.type": "#GlobalPolicies.GlobalPolicies",
    #   "@odata.context": "/redfish/v1/SFNC/2/$metadata#GlobalPolicies/GlobalPolicies/$entity"
    # }
    #redfish/v1/SFSS/2/GlobalPolicies
    # {
    #   "ZoningPolicy": "Disable",
    #   "NameServerEntityPurgeTOV": "48Hr",
    #   "@odata.id": "/redfish/v1/SFNC/2/GlobalPolicies",
    #   "@odata.type": "#GlobalPolicies.GlobalPolicies",
    #   "@odata.context": "/redfish/v1/SFNC/2/$metadata#GlobalPolicies/GlobalPolicies/$entity"
    # }
    - name: Create Global Policies
      dellemc.sfss.sfss_global_policies:
        config:
        - zoning_policy: false
          NameServerEntityPurgeTOV: 4Hr
          instance_id: 1
        - zoning_policy: false
          NameServerEntityPurgeTOV: 8Hr
          instance_id: 2
    #
    # After state:
    # -------------
    #
    #redfish/v1/SFSS/1/GlobalPolicies
    # {
    #   "ZoningPolicy": "Disable",
    #   "NameServerEntityPurgeTOV": "4Hr",
    #   "@odata.id": "/redfish/v1/SFNC/1/GlobalPolicies",
    #   "@odata.type": "#GlobalPolicies.GlobalPolicies",
    #   "@odata.context": "/redfish/v1/SFNC/1/$metadata#GlobalPolicies/GlobalPolicies/$entity"
    # }
    #redfish/v1/SFSS/2/GlobalPolicies
    # {
    #   "ZoningPolicy": "Disable",
    #   "NameServerEntityPurgeTOV": "8Hr",
    #   "@odata.id": "/redfish/v1/SFNC/2/GlobalPolicies",
    #   "@odata.type": "#GlobalPolicies.GlobalPolicies",
    #   "@odata.context": "/redfish/v1/SFNC/2/$metadata#GlobalPolicies/GlobalPolicies/$entity"
    # }





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

