.. _instance_info_module:


instance_info
=============

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Get info about a Linode instance.



Requirements
------------
The below requirements are needed on the host that executes this module.

- python >= 2.7
- linode_api4 >= 3.0



Parameters
----------

  label (optional, string, None)
    The instance’s label.


  id (optional, int, None)
    The unique id of the instance.









Examples
--------

.. code-block:: yaml+jinja

    
    - name: Get info about an instance by label
      linode.cloud.instance_info:
        label: 'my-instance'
        
    - name: Get info about an instance by id
      linode.cloud.instance_info:
        id: 12345




Return Values
-------------

**instance (always, dict):**

The instance description in JSON serialized form.

`Linode Response Object Documentation <https://www.linode.com/docs/api/linode-instances/#linode-view__responses>`_

Sample Response:

.. code-block:: JSON

    {
     "alerts": {
      "cpu": 90,
      "io": 10000,
      "network_in": 10,
      "network_out": 10,
      "transfer_quota": 80
     },
     "backups": {
      "enabled": false,
      "schedule": {
       "day": null,
       "window": null
      }
     },
     "created": "xxxx-xx-xxTxx:xx:xx",
     "group": "app",
     "hypervisor": "kvm",
     "id": "xxxxxx",
     "image": "linode/ubuntu20.04",
     "ipv4": [
      "xxx.xxx.xxx.xxx"
     ],
     "ipv6": "xxxx:xxxx::xxxx:xxxx:xxxx:xxxx/64",
     "label": "my-linode",
     "region": "us-east",
     "specs": {
      "disk": 25600,
      "memory": 1024,
      "transfer": 1000,
      "vcpus": 1
     },
     "status": "running",
     "tags": [
      "env=prod"
     ],
     "type": "g6-nanode-1",
     "updated": "xxxx-xx-xxTxx:xx:xx",
     "watchdog_enabled": true
    }





Status
------




- This module is maintained by Linode.



Authors
~~~~~~~

- Luke Murphy (@decentral1se)
- Charles Kenney (@charliekenney23)
- Phillip Campbell (@phillc)
- Lena Garber (@lbgarber)

