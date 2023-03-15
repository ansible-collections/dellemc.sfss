.. _sfss_app_images_module:


sfss_app_images -- Manage SFSS APP images
=========================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

This module is used to manage SFSS application images. Use this module to download images from the image file server using HTTP, HTTPS, FTP, or SCP.






Parameters
----------

  config (optional, list, None)
    This module is used to manage SFSS application images.


    version (optional, str, None)
      Image version.


    image_id (optional, str, None)
      Unique Id assigned to image on creation.


    status (optional, str, None)
      Status of the download process.


    fileserver_username (optional, str, None)
      Username to access the image file server.


    fileserver_password (optional, str, None)
      Password to access the image file server.


    fileserver_host (optional, str, None)
      IP address of the image file server.


    image_file (optional, str, None)
      Path location of the image file.


    status_message (optional, str, None)
      Status message.


    update_password (optional, bool, False)
      Choice to update the password.


    transport_type (True, str, None)
      Transport type.



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
    #redfish/v1/SFSSApp/SFSSImages?$expand=SFSSImages
    # "SFSSImages":[
    # {
    #   "ImageServerLocation": "100.94.72.166:/home/dell/temp_images/sfss-1.2.0.deb",
    #   "StatusMessage": "Download Started",
    #   "ImageServerPassword": "force10",
    #   "Status": "InProgress",
    #   "TransportType": "SCP",
    #   "ImageServerUserName": "dell",
    #   "Version": "1.2.0",
    #   "@odata.id": "/redfish/v1/SFSSApp/SFSSImages('1.2.0')",
    #   "@odata.type": "#SFSSImages.SFSSImages",
    #   "@odata.context": "/redfish/v1/SFSSApp/$metadata#SFSSImages/SFSSImages/$entity"
    # },
    # {
    #     "StatusMessage": "Added during initializing",
    #     "Status": "Success",
    #     "Version": "1.0.0",
    #     "@odata.id": "/redfish/v1/SFSSApp/SFSSImages('1.0.0')",
    #     "@odata.type": "#SFSSImages.SFSSImages",
    #     "@odata.context": "/redfish/v1/SFSSApp/$metadata#SFSSImages/SFSSImages/$entity"
    # }
    # ]
    - name: Stfs App image create
      dellemc.sfss.app_images:
        config:
        - fileserver_host: 100.94.72.166
          fileserver_password: force10
          fileserver_username: dell
          image_file: /home/dell/temp_images1/sfss-1.2.0.deb
          transport_type: scp
          version: 1.2.0
        state: deleted
    #
    # After state:
    # -------------
    #
    #redfish/v1/SFSSApp/SFSSImages?$expand=SFSSImages
    # "SFSSImages": [
    # {
    #   "StatusMessage": "Added during initializing",
    #   "Status": "Success",
    #   "Version": "1.0.0",
    #   "@odata.id": "/redfish/v1/SFSSApp/SFSSImages('1.0.0')",
    #   "@odata.type": "#SFSSImages.SFSSImages",
    #   "@odata.context": "/redfish/v1/SFSSApp/$metadata#SFSSImages/SFSSImages/$entity"
    # }
    # ]
    #
    # Using deleted
    #
    # Before state:
    # -------------
    #
    #redfish/v1/SFSSApp/SFSSImages?$expand=SFSSImages
    # "SFSSImages": [
    # {
    #   "ImageServerLocation": "100.94.72.166:/home/dell/temp_images/sfss-1.2.0.deb",
    #   "StatusMessage": "Download Started",
    #   "ImageServerPassword": "force10",
    #   "Status": "InProgress",
    #   "TransportType": "SCP",
    #   "ImageServerUserName": "dell",
    #   "Version": "1.2.0",
    #   "@odata.id": "/redfish/v1/SFSSApp/SFSSImages('1.2.0')",
    #   "@odata.type": "#SFSSImages.SFSSImages",
    #   "@odata.context": "/redfish/v1/SFSSApp/$metadata#SFSSImages/SFSSImages/$entity"
    # },
    # {
    #   "StatusMessage": "Added during initializing",
    #   "Status": "Success",
    #   "Version": "1.0.0",
    #   "@odata.id": "/redfish/v1/SFSSApp/SFSSImages('1.0.0')",
    #   "@odata.type": "#SFSSImages.SFSSImages",
    #   "@odata.context": "/redfish/v1/SFSSApp/$metadata#SFSSImages/SFSSImages/$entity"
    # }
    # ]
    - name: Stfs App image create
      dellemc.sfss.app_images:
        config: []
        state: deleted
    #
    # After state:
    # -------------
    #
    #redfish/v1/SFSSApp/SFSSImages?$expand=SFSSImages
    # "SFSSImages": [
    # {
    #   "StatusMessage": "Added during initializing",
    #   "Status": "Success",
    #   "Version": "1.0.0",
    #   "@odata.id": "/redfish/v1/SFSSApp/SFSSImages('1.0.0')",
    #   "@odata.type": "#SFSSImages.SFSSImages",
    #   "@odata.context": "/redfish/v1/SFSSApp/$metadata#SFSSImages/SFSSImages/$entity"
    # }
    # ]
    # Using merged
    #
    # Before state:
    # -------------
    #
    #redfish/v1/SFSSApp/SFSSImages?$expand=SFSSImages
    # "SFSSImages": [
    # {
    #   "StatusMessage": "Added during initializing",
    #   "Status": "Success",
    #   "Version": "1.0.0",
    #   "@odata.id": "/redfish/v1/SFSSApp/SFSSImages('1.0.0')",
    #   "@odata.type": "#SFSSImages.SFSSImages",
    #   "@odata.context": "/redfish/v1/SFSSApp/$metadata#SFSSImages/SFSSImages/$entity"
    # }
    # ]
    - name: Stfs App image create
      dellemc.sfss.app_images:
        config:
        - fileserver_host: 100.94.72.166
          fileserver_password: force10
          fileserver_username: dell
          image_file: /home/dell/temp_images1/sfss-1.2.0.deb
          transport_type: scp
          version: 1.2.0

    #
    # After state:
    # -------------
    #
    #redfish/v1/SFSSApp/SFSSImages?$expand=SFSSImages
    # "SFSSImages": [
    # {
    #   "ImageServerLocation": "100.94.72.166:/home/dell/temp_images/sfss-1.2.0.deb",
    #   "StatusMessage": "Download Started",
    #   "ImageServerPassword": "force10",
    #   "Status": "InProgress",
    #   "TransportType": "SCP",
    #   "ImageServerUserName": "dell",
    #   "Version": "1.2.0",
    #   "@odata.id": "/redfish/v1/SFSSApp/SFSSImages('1.2.0')",
    #   "@odata.type": "#SFSSImages.SFSSImages",
    #   "@odata.context": "/redfish/v1/SFSSApp/$metadata#SFSSImages/SFSSImages/$entity"
    # },
    # {
    #   "StatusMessage": "Added during initializing",
    #   "Status": "Success",
    #   "Version": "1.0.0",
    #   "@odata.id": "/redfish/v1/SFSSApp/SFSSImages('1.0.0')",
    #   "@odata.type": "#SFSSImages.SFSSImages",
    #   "@odata.context": "/redfish/v1/SFSSApp/$metadata#SFSSImages/SFSSImages/$entity"
    # }
    # ]





Return Values
-------------

before (always, list, ['StatusMessage: Added during initializing', 'Status: Success', 'Version: 1.0.0'])
  The configuration prior to the model invocation.


after (when changed, list, ['StatusMessage: Added during initializing', 'Status: Success', 'Version: 1.0.0'])
  The resulting configuration model invocation.


commands (always, list, ['command 1', 'command 2', 'command 3'])
  The set of commands pushed to the remote device.





Status
------





Authors
~~~~~~~

- Mohamed Javeed (@javeedf)

