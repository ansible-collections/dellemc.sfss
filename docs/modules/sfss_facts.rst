.. _sfss_facts_module:


sfss_facts -- Get facts about SFSS devices
==========================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Collects facts from network devices running the SFSS application. This module places the facts gathered in the fact tree keyed by the respective resource name.  The facts module will always collect a base set of facts from the device and can enable or disable collection of additional facts.






Parameters
----------

  gather_subset (False, list, !config)
    When supplied, this argument restricts the facts collected to a given subset. Possible values for this argument include all, min, hardware, config, legacy, and interfaces. Can specify a list of values to include a larger subset. Values can also be used with an initial '!' to specify that a specific subset should not be collected.


  gather_network_resources (False, list, None)
    When supplied, this argument restricts the facts collected to a given subset. Possible values for this argument include all and the resources like interfaces, vlans etc. Can specify a list of values to include a larger subset. Values can also be used with an initial '!' to specify that a specific subset should not be collected.









Examples
--------

.. code-block:: yaml+jinja

    
    # Gather all facts
    - sfss_facts:
        gather_subset: all
        gather_network_resources: all

    # Collect only the endpoints facts
    - sfss_facts:
        gather_subset:
          -!all
          -!min
        gather_network_resources:
        - endpoints
        - zones
        - zone_alias
        - cdc_instances
        - security_authentication
        - app_images
        - interface_ip_mgmt
        - app_image_upgrade

    # Do not collect endpoints facts
    - sfss_facts:
        gather_network_resources:
        - "!endpoints"

    # Collect endpoints and minimal default facts
    - sfss_facts:
        gather_subset: min
        gather_network_resources: endpoints





Status
------





Authors
~~~~~~~

- Mohamed Javeed (@javeedf)

