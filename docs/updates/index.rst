#######
Updates
#######

June 30 2025
============

`Data Preview 1 <https://dp1.lsst.io/>`_ released.

**Version 29.1.1**:
The recommended build of the LSST Science Pipelines available in the RSP Notebook Aspect has been upgraded to r29.1.1.
This is the same version that was used to process the Data Preview 1 (DP1) dataset.

**User quota is 35 GB**:
User's ``/home`` spaces in the Notebook Aspect now have a quota of 35 GB.
Users in excess of the quota will still be able to log in, but will be unable to write any more files until they've deleted files and are under the quota.

**/scratch is now /deleted-sundays**:
The ``/deleted-sundays`` directory in the Notebook Aspect is writeable by all, and has no quota, but is cleared out on Sundays.
This directory is *temporary storage* for large intermediate files (e.g., byproducts of data processing).

**Use the "Large" container for data analysis**:
The "Medium" container size option has been removed from the Notebook Aspect.
The "Large" size (currently 4 core 16 GB RAM) is the default and should be used for data processing tasks.
The “Small” instance remains available for quick tasks such as file operations.

**Temporary user table upload**:
Users can now upload a table to the TAP server and join it with any of the hosted catalogs.
Previously, this was only available for DP0.3 catalogs.
User uploaded tables are currently limited to 32 MB.

**Job Monitor**:
There is a new tab in the Portal Aspect called “Job Monitor” that provides access to the inputs, status, and results of submitted queries.


April 28 2025
=============

The capability for users to create groups and set directory permissions to enable
private file sharing between group members now exists,
see :ref:`how to create user groups <user-group-create>`.


March 6 2025
============

The DP0.2 images are now being served from their new location US Data Facility at SLAC (instead of Google Cloud).
This change is transparent to users, except for a potential higher latency in image access (10%-30%; a fix is in development).

The recommended image of the Notebook Aspect was updated to Weekly 2025_09, and the Python version upgraded to 3.12.

Tutorials are now available in the Notebook Aspect via the JupyterLab menu.
Those under “Latest” will always correspond to the recommended image.
Select the desired tutorial and a writeable file will automatically save to the ``$HOME/notebooks/tutorials/`` directory.

The GitHub repository for notebook tutorials is now `lsst/tutorial-notebooks <https://github.com/lsst/tutorial-notebooks>`_.


Actions required
----------------

Any packages you installed under Python 3.11 may need to be re-installed because the Notebook Aspect now uses Python 3.12.

Remove old versions of the tutorial notebooks from the old, write-only directory, in order to save space and avoid confusion:

.. code-block:: bash

   chmod -R u+w $HOME/notebooks/tutorial-notebooks/
   rm -rf $HOME/notebooks/tutorial-notebooks/

