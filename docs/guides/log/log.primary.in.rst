Mar 6 2025
==========

DP0.2 images are now being served from their new location US Data Facility at SLAC (instead of Google Cloud).
This change is transparent to users, except for a potential higher latency in image access (10-30%); a fix is in development.

The recommended image of the Notebook Aspect was updated to Weekly 2025_09, and the Python version upgraded to 3.12.

Tutorials are now available in the Notebook Aspect via the JupyterLab menu.
Those under “Latest” will always correspond to the recommended image.
Select the desired tutorial and a writeable file will automatically save to the ``$HOME/notebooks/tutorials/`` directory.

The GitHub repository for notebook tutorials is now `lsst/tutorial-notebooks <https://github.com/lsst/tutorial-notebooks>`_.


Action items
------------

Any user-installed python packages with version 3.11 may need to be re-installed.

Remove old versions of the tutorial notebooks from the old, write-only directory, in order to save space and avoid confusion.

.. code-block:: bash

   chmod -R u+w $HOME/notebooks/tutorial-notebooks/
   rm -rf $HOME/notebooks/tutorial-notebooks/

