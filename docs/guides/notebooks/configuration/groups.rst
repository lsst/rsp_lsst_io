############################
User groups for file sharing
############################

Create and manage closed user groups in order to share private files in the ``/project`` directory.

.. _user-group-create:

Create a closed group
=====================

Comanage webpage
----------------

* In a browser, navigate to `id.lsst.cloud <https://id.lsst.cloud>`_ and log in.

* In the left menu sidebar, click on "Groups" and then "My Groups".

* At right, a list of all the groups associated with your account will appear.

* In the top horizontal menu, click on "Add Group".

* Set the group properties:

  * The group name should be short and must start with ``g_``.

  * Write a short description.

  * Leave the status as the default "Active".

  * Leave the checkbox next to "Open" unselected, to create a closed group.

  * Leave the checkbox next to "Require All for Nested Memberships" unchecked; this can be changed later if nested sub-groups are created.

* Click the blue "Add" button.


The next time you enter the Notebook Aspect, this group will be accessible.


Command line
------------

At this time, it is not possible to create new groups from the terminal command line in the Notebook Aspect.

It is possible to list all groups with ``getent group``, and to see all groups a
user belongs to with ``groups <username>`` (see your own username with ``whoami``).


Manage group membership
=======================

Only group owners can manage group membership.

Comanage webpage
----------------

* In a browser, navigate to `id.lsst.cloud <https://id.lsst.cloud>`_ and log in.
* In the left menu sidebar, click on "Groups" and then "My Groups".
* At right, a list of all the groups associated with your account will appear.
* In the "Name" column, click on the group name you want to add members to.
* From the "Group Properties" page, select the tab "Members".
* At upper right, use the "Add member" box to find and add group members.
* In the "Permissions" column, make other group members "Owners" using the check boxes.


Command line
------------

At this time, it is not possible to add users to groups from the terminal command line in the Notebook Aspect.



Set directory permissions
=========================

The point of creating a closed group is to use it to give access permissions to a privately shared directory
in ``/project``.

Comanage webpage
----------------

Shared files are not managed via the Comanage webpage.


Command line
------------

These instructions are not unique to the Rubin Science Platform or JupyterLab;
they are generic processes for manipulating directory permissions in Unix-like operating systems.

* In a browser, navigate to `data.lsst.cloud <https://data.lsst.cloud>`_ and log in to the Notebook Aspect.

* Open a terminal and go to the shared ``/project`` directory.

   .. code-block:: bash

      cd /project

* Create a new directory for sharing, and name it ``new-dir-name``.

   .. code-block:: bash

      mkdir <new-dir-name>

* Add the group to the new directory.

   .. code-block:: bash

      chgrp <group-name> <new-dir-name>

* Give the group read, write, and execute permission on the directory.

   .. code-block:: bash

      chmod g+rwx <new-dir-name>

* Review the final permissions on the new directory.

   .. code-block:: bash

      ls -lah <new-dir-name>

  The results should resemble the following.

   .. code-block:: bash

      drwxrwsr-x  2 <user-name> <group-name> 4.0K <MMM DD HH:SS> <new-dir-name>

