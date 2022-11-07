.. _sfss_backup_restore_module:


sfss_backup_restore -- This module manages attributes of Sfss Backup and Restore
================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

This module manages attributes of Sfss Backup and Restore






Parameters
----------

  config (optional, list, None)
    A list of link aggregation group configurations.


    imageserver_location (True, str, None)
      Location of the image file on the server


    imageserver_password (True, str, None)
      Password of the image file server


    imageserver_username (True, str, None)
      Username of the image file server


    transport_type (optional, str, SCP)
      Transport type


    operation_type (True, str, None)
      Type of operation Backup or Restore



  state (optional, str, merged)
    The state the configuration should be left in





Notes
-----

.. note::
   - Idempotent is not supported.
   - Supports ``check_mode``.




Examples
--------

.. code-block:: yaml+jinja

    
    # Using merged
    #
    # Before state:
    # -------------
    #
    # /redfish/v1/SFSSApp/Backups
    # "Backups": [
    # {
    #   "ID": "16efc4f3-4940-4b2d-b4fe-239051d32a64",
    #   "ImageServerLocation": "100.104.26.71:/tmp/sfnc-1.0.0.4.deb",
    #   "StatusMessage": "Upload Backup file succeeded. ",
    #   "ImageServerPassword": "force10",
    #   "Status": "Success",
    #   "TimeStamp": "1629117585.7291455",
    #   "TransportType": "SCP",
    #   "ImageServerUserName": "root",
    #   "@odata.id": "/redfish/v1/SFNCApp/Backups('16efc4f3-4940-4b2d-b4fe-239051d32a64')",
    #   "@odata.type": "#Backups.Backups",
    #   "@odata.context": "/redfish/v1/SFNCApp/$metadata#Backups/Backups/$entity"
    # },
    # {
    #   "ID": "45b533a9-d4a0-4490-be0e-095796993f0e",
    #   "ImageServerLocation": "100.104.26.71:/tmp/sfnc-1.0.0.4.deb",
    #   "StatusMessage": "Upload Backup file succeeded. ",
    #   "ImageServerPassword": "force10",
    #   "Status": "Success",
    #   "TimeStamp": "1628872736.8617551",
    #   "TransportType": "SCP",
    #   "ImageServerUserName": "root",
    #   "@odata.id": "/redfish/v1/SFNCApp/Backups('45b533a9-d4a0-4490-be0e-095796993f0e')",
    #   "@odata.type": "#Backups.Backups",
    #   "@odata.context": "/redfish/v1/SFNCApp/$metadata#Backups/Backups/$entity"
    # }
    # ]
    # /redfish/v1/SFSSApp/Restores
    # "Restores": [
    # {
    #   "Status": "Failure",
    #   "TransportType": "SCP",
    #   "TimeStamp": "1629136702.8498998",
    #   "StatusMessage": "Download Backup file failed. [Errno 110] Connection timed out",
    #   "ImageServerPassword": "48zltmhDBNDfD48jJ2hz81NgEKELL4pSMWq3QWvdEOe4zactLshbEMsxXoYyA1sX",
    #   "ID": "63ab85db-06f5-47d1-acfc-7e8699b81ec0",
    #   "ImageServerUserName": "dell55",
    #   "ImageServerLocation": "100.94.55.166:/home/dell/temp_images1/sfnc-1.55.0.deb/backup_file.tar.gz",
    #   "@odata.id": "/redfish/v1/SFSSApp/Restores('63ab85db-06f5-47d1-acfc-7e8699b81ec0')",
    #   "@odata.type": "#Restores.Restores",
    #   "@odata.context": "/redfish/v1/SFSSApp/$metadata#Restores/Restores/$entity"
    # },
    # {
    #   "Status": "Failure",
    #   "TransportType": "SCP",
    #   "TimeStamp": "1629132123.7281032",
    #   "StatusMessage": "Download Backup file failed. [Errno 110] Connection timed out",
    #   "ImageServerPassword": "WLCiieSlBzCqHE3vSoHXRNgcXuW4oeVjdWZ4bvx1Fwn0AFq6WzIlwV+UcUFWSbGG",
    #   "ID": "c93a935a-ff36-4b04-9d03-b7ce45568507",
    #   "ImageServerUserName": "dell55",
    #   "ImageServerLocation": "100.94.55.166:/home/dell/temp_images1/sfnc-1.55.0.deb/backup_file.tar.gz",
    #   "@odata.id": "/redfish/v1/SFSSApp/Restores('c93a935a-ff36-4b04-9d03-b7ce45568507')",
    #   "@odata.type": "#Restores.Restores",
    #   "@odata.context": "/redfish/v1/SFSSApp/$metadata#Restores/Restores/$entity"
    # }
    # ]
    #
    - name: Create backup and restore
      dellemc.sfss.sfss_backup_restore:
        config:
        - imageserver_location: 100.104.26.70:/tmp/sfnc-1.0.0.4.deb
          imageserver_password: force10
          imageserver_username: root
          transport_type: SCP
          type_op: backup
        - imageserver_location: 100.94.55.166:/home/dell/temp_images1/sfnc-1.55.0.deb/backup_file.tar.gz
          imageserver_password: force1055
          imageserver_username: dell55
          transport_type: SCP
          type_op: restore
    #
    # After state:
    # -------------
    #
    # /redfish/v1/SFSSApp/Backups
    # "Backups": [
    # {
    #   "ID": "16efc4f3-4940-4b2d-b4fe-239051d32a64",
    #   "ImageServerLocation": "100.104.26.71:/tmp/sfnc-1.0.0.4.deb",
    #   "StatusMessage": "Upload Backup file succeeded. ",
    #   "ImageServerPassword": "force10",
    #   "Status": "Success",
    #   "TimeStamp": "1629117585.7291455",
    #   "TransportType": "SCP",
    #   "ImageServerUserName": "root",
    #   "@odata.id": "/redfish/v1/SFNCApp/Backups('16efc4f3-4940-4b2d-b4fe-239051d32a64')",
    #   "@odata.type": "#Backups.Backups",
    #   "@odata.context": "/redfish/v1/SFNCApp/$metadata#Backups/Backups/$entity"
    # },
    # {
    #   "ID": "45b533a9-d4a0-4490-be0e-095796993f0e",
    #   "ImageServerLocation": "100.104.26.71:/tmp/sfnc-1.0.0.4.deb",
    #   "StatusMessage": "Upload Backup file succeeded. ",
    #   "ImageServerPassword": "force10",
    #   "Status": "Success",
    #   "TimeStamp": "1628872736.8617551",
    #   "TransportType": "SCP",
    #   "ImageServerUserName": "root",
    #   "@odata.id": "/redfish/v1/SFNCApp/Backups('45b533a9-d4a0-4490-be0e-095796993f0e')",
    #   "@odata.type": "#Backups.Backups",
    #   "@odata.context": "/redfish/v1/SFNCApp/$metadata#Backups/Backups/$entity"
    # },
    # {
    #   "ID": "dc2127aa-07e2-45e1-bbf4-7710f8d45a26",
    #   "ImageServerLocation": "100.104.26.70:/tmp/sfnc-1.0.0.4.deb",
    #   "StatusMessage": "Upload Backup file succeeded. ",
    #   "ImageServerPassword": "2b3bbZgs2ihLFTX/2fneVpJUpOQbGSpcNOaxmnrvDpabL39mVdMpLbFOL5m7/Uel",
    #   "Status": "Success",
    #   "TimeStamp": "1629137911.304514",
    #   "TransportType": "SCP",
    #   "ImageServerUserName": "root",
    #   "@odata.id": "/redfish/v1/SFSSApp/Backups('dc2127aa-07e2-45e1-bbf4-7710f8d45a26')",
    #   "@odata.type": "#Backups.Backups",
    #   "@odata.context": "/redfish/v1/SFSSApp/$metadata#Backups/Backups/$entity"
    # }
    # ]
    # /redfish/v1/SFSSApp/Restores
    # "Restores": [
    # {
    #   "Status": "Failure",
    #   "TransportType": "SCP",
    #   "TimeStamp": "1629136702.8498998",
    #   "StatusMessage": "Download Backup file failed. [Errno 110] Connection timed out",
    #   "ImageServerPassword": "48zltmhDBNDfD48jJ2hz81NgEKELL4pSMWq3QWvdEOe4zactLshbEMsxXoYyA1sX",
    #   "ID": "63ab85db-06f5-47d1-acfc-7e8699b81ec0",
    #   "ImageServerUserName": "dell55",
    #   "ImageServerLocation": "100.94.55.166:/home/dell/temp_images1/sfnc-1.55.0.deb/backup_file.tar.gz",
    #   "@odata.id": "/redfish/v1/SFSSApp/Restores('63ab85db-06f5-47d1-acfc-7e8699b81ec0')",
    #   "@odata.type": "#Restores.Restores",
    #   "@odata.context": "/redfish/v1/SFSSApp/$metadata#Restores/Restores/$entity"
    # },
    # {
    #   "Status": "Failure",
    #   "TransportType": "SCP",
    #   "TimeStamp": "1629132123.7281032",
    #   "StatusMessage": "Download Backup file failed. [Errno 110] Connection timed out",
    #   "ImageServerPassword": "WLCiieSlBzCqHE3vSoHXRNgcXuW4oeVjdWZ4bvx1Fwn0AFq6WzIlwV+UcUFWSbGG",
    #   "ID": "c93a935a-ff36-4b04-9d03-b7ce45568507",
    #   "ImageServerUserName": "dell55",
    #   "ImageServerLocation": "100.94.55.166:/home/dell/temp_images1/sfnc-1.55.0.deb/backup_file.tar.gz",
    #   "@odata.id": "/redfish/v1/SFSSApp/Restores('c93a935a-ff36-4b04-9d03-b7ce45568507')",
    #   "@odata.type": "#Restores.Restores",
    #   "@odata.context": "/redfish/v1/SFSSApp/$metadata#Restores/Restores/$entity"
    # },
    # {
    #   "Status": "Failure",
    #   "TransportType": "SCP",
    #   "TimeStamp": "1629137911.376702",
    #   "StatusMessage": "Download Backup file failed. [Errno 110] Connection timed out",
    #   "ImageServerPassword": "7k5C5LM2hAudjUbs+zYnpLFq8o9CwQWVHIiF8IOJvGntDv8Xe6GOvFjnpT9DpFZy",
    #   "ID": "df3fef09-c7e6-4d0f-a0f0-d71dc6363e5a",
    #   "ImageServerUserName": "dell55",
    #   "ImageServerLocation": "100.94.55.165:/home/dell/temp_images1/sfnc-1.55.0.deb/backup_file.tar.gz",
    #   "@odata.id": "/redfish/v1/SFSSApp/Restores('df3fef09-c7e6-4d0f-a0f0-d71dc6363e5a')",
    #   "@odata.type": "#Restores.Restores",
    #   "@odata.context": "/redfish/v1/SFSSApp/$metadata#Restores/Restores/$entity"
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

