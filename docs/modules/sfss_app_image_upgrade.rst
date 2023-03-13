.. _sfss_app_image_upgrade_module:


sfss_app_image_upgrade -- Upgrade or downgrade SFSS APP
=======================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

This module is used to upgrade or downgrade SFSS application to the specified image version.






Parameters
----------

  config (optional, dict, None)
    A list of images.


    image_version (optional, str, None)
      Image version to upgrade to.



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
    # GET redfish/v1/SFNCApp
    # {
    #     "DeploymentModel": "StandAlone",
    #     "Version": "1.0.0.3",
    #     "@odata.id": "/redfish/v1/SFNCApp",
    #     "@odata.type": "#SFNCApp.SFNCApp",
    #     "@odata.context": "/redfish/v1/$metadata#SFNCApp/SFNCApp/$entity"
    # }
    - name: SFSS Image upgrade process started ...
      dellemc.sfss.sfss_app_image_upgrade:
       config:
        image_version: 1.0.0.4
      register: image_upgrade_result
    #
    # After state:
    # -------------
    #
    # GET redfish/v1/SFNCApp
    # {
    #     "DeploymentModel": "StandAlone",
    #     "Version": "1.0.0.4",
    #     "@odata.id": "/redfish/v1/SFNCApp",
    #     "@odata.type": "#SFNCApp.SFNCApp",
    #     "@odata.context": "/redfish/v1/$metadata#SFNCApp/SFNCApp/$entity"
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

- Mohamed Javeed (@javeedf)

