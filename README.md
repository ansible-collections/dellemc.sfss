Ansible Network Collection for SFSS
===================================

This collection includes Ansible Network resource modules, and plugins needed to manage Dell EMC SFSS Application. Sample playbooks and documentation are also included to show how the collection can be used.

Supported connections
---------------------
The SFSS Ansible collection supports httpapi connections.

Plugins
--------

**HTTPAPI plugin**

Name | Description
--- | ---
[httpapi](https://github.com/ansible-collections/dellemc.sfss)|Use Ansible HTTPAPI to run commands on SFSS

Collection network resource modules
-----------------------------------
Listed are the SFSS Ansible network resource modules which need ***httpapi*** as the connection type. Supported operations are ***merged*** and ***deleted***.

Name | Description
--- | --- 
[**sfss_endpoints**]|Manage SFSS Endpoints like Host, Subsystem and DDC
[**sfss_zone_alias**]|Manage Zone alais configurations
[**sfss_zone_groups**]|Manage Zone Group configurations and its activation
[**sfss_zones**]|Manage Zone configurations
[**sfss_cdc_instances**]|Manage CDC instance configurations
[**sfss_security_authentication**]|Manage TACACS+ and RADIUS configurations
[**sfss_interface_ip_mgmt**]|Manage Interface IP management configurations
[**sfss_app_images**]|Manage APP image downloads


Sample use case playbooks
-------------------------
TBD

Version compatibility
----------------------
* Recommended Ansible version 2.10 or higher
* Supports SFSS 1.0.0
* Recommended Python 3.5 or higher


Installation of Ansible 2.11+
-----------------------------
##### Dependencies for Ansible SFSS collection

      pip3 install paramiko>=2.7
      pip3 install jinja2>=2.8
      pip3 install ansible-core

Installation of Ansible 2.10+
-----------------------------
##### Dependencies for Ansible SFSS collection

      pip3 install paramiko>=2.7
      pip3 install jinja2>=2.8
      pip3 install ansible-base
      
Installation of Ansible 2.9
---------------------------
##### Dependencies for Ansible SFSS collection

      pip3 install paramiko>=2.7
      pip3 install jinja2>=2.8
      pip3 install ansible
      
##### Setting Environment Variables

To use the SFSS collection in Ansible 2.9, it is required to add one of the two available environment variables.

Option 1: Add the environment variable while running the playbook.


      ANSIBLE_NETWORK_GROUP_MODULES=sfss ansible-playbook sample_playbook.yaml -i inventory.yaml
      
      
Option 2: Add the environment variable in user profile.


      ANSIBLE_NETWORK_GROUP_MODULES=sfss
      

Installation of SFSS collection from Ansible Galaxy
---------------------------------------------------------------

Install the latest version of the SFSS collection from Ansible Galaxy.

      ansible-galaxy collection install dellemc.sfss

To install a specific version, specify a version range identifier. For example, to install the most recent version that is greater than or equal to 1.0.0 and less than 2.0.0.

      ansible-galaxy collection install 'dellemc.sfss:>=1.0.0,<2.0.0'


Sample playbooks
-----------------

**Zone configuration using HTTPAPI**

***sfss_zones.yaml***

    ---
    - name: SFSS Ansible Resource modules Examples 
      hosts: sfss_controllers
      gather_facts: no
      connection: httpapi
      tasks:
      - name: Create Zone
        dellemc.sfss.zones:
          config:
            - name: Ansible_Zone
              instance_id: 1
              group_name: Zone_group_11
              members:
                data:
                  - id: nqn.2014-08.org.nvmexpress:uuid:host
                    id_type: nqn
                    role: host
          state: merged

***host_vars/sfss_controller1.yaml***

    hostname: sfss_controller1

    ansible_user: xxxx
    ansible_pass: xxxx
    ansible_network_os: dellemc.sfss.sfss
    ansible_httpapi_use_ssl: true
    ansible_httpapi_validate_certs: false

***inventory.yaml***

    [sfss_controller1]
    sfss_controller1 ansible_host=100.104.28.119

    [sfss_controller2]
    sfss_controller2 ansible_host=100.104.28.120

    [sfss_controllers:children]
    sfss_controller1
    sfss_controller2

Releasing, Versioning and Deprecation
-------------------------------------

This collection follows [Semantic Versioning](https://semver.org/). More details on versioning can be found [in the Ansible docs](https://docs.ansible.com/ansible/latest/dev_guide/developing_collections.html#collection-versions).

We plan to regularly release new minor or bugfix versions once new features or bugfixes have been implemented.

SFSS Ansible Modules deprecation cycle is aligned with [Ansible](https://docs.ansible.com/ansible/latest/dev_guide/module_lifecycle.html).

Code of Conduct
---------------

This repository adheres to the [Ansible Community code of conduct](https://docs.ansible.com/ansible/latest/community/code_of_conduct.html)

(c) 2021 Dell Inc. or its subsidiaries. All Rights Reserved.