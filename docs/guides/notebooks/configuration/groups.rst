###################
User-managed groups
###################

Create and manage closed user groups in order to share private files.

.. _user-group-create:

Create a group
==============

Groups are created an managed in the Comanage system at `id.lsst.cloud <https://id.lsst.cloud>`_
(not from the terminal command line, as in some other systems).

From the terminal command line it is possible to list all groups with ``getent group``.

How to create a group in Comanage:

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


Manage group membership
=======================

Only group owners can manage group membership.

A user can only be a member of up to 15 groups at this time.
Joining additional groups will have no effect.

From the terminal command line it is possible to see all groups a user belongs to with ``groups <username>``
(see your own username with ``whoami``).

How to manage group membership in Comanage:

* In a browser, navigate to `id.lsst.cloud <https://id.lsst.cloud>`_ and log in.
* In the left menu sidebar, click on "Groups" and then "My Groups".
* At right, a list of all the groups associated with your account will appear.
* In the "Name" column, click on the group name you want to add members to.
* From the "Group Properties" page, select the tab "Members".
* At upper right, use the "Add member" box to find and add group members.
* In the "Permissions" column, make other group members "Owners" using the check boxes.

The next time these users enter the Notebook Aspect, they will be able to access files shared with the group.



Set directory permissions
=========================

The point of creating a closed group is to permit group members to access privately shared files.

Shared files are not managed via the Comanage webpage; use the terminal command line in the Notebook Aspect.

These instructions are not all unique to the Rubin Science Platform or JupyterLab;
some are generic processes for manipulating directory permissions in Unix-like operating systems.

Instructions for creating and sharing a directory with a group:

* In a browser, navigate to `data.lsst.cloud <https://data.lsst.cloud>`_ and log in to the Notebook Aspect.

* Open a terminal, navigate to ``/home``, and modify the permissions on your home directory to let others access any shared directories within it (see your own username with ``whoami``).

   .. code-block:: bash

      cd /home
      chmod o+x <user-name>

* Navigate to your home directory and create a new directory for sharing.

   .. code-block:: bash

      cd ~
      mkdir <shared-dir-name>

* Add the group to the new directory and give group members write permissions (``g+w``) and add the "sticky" bit (``s``) so that all files created in the directory are accessible to group members.

   .. code-block:: bash

      chgrp <group-name> <shared-dir-name>
      chmod g+ws <shared-dir-name>

* Review the final permissions on the new directory.

   .. code-block:: bash

      ls -lah <shared-dir-name>

  The results should resemble the following.

   .. code-block:: bash

      drwxrwsr-x  2 <user-name> <group-name> 4.0K <MMM DD HH:SS> <shared-dir-name>

