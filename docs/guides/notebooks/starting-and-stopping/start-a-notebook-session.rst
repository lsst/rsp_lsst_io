###########################
Starting a notebook session
###########################

This page explains how to start a JupyterLab server on the |rsp-at|.

You'll need an account for the |rsp-at|.
For more information about logging into the |rsp-at|, including getting an account, see :doc:`/guides/getting-started/get-an-account`.

Step 1. Go to the server options page
=====================================

From the Homepage_, click on :guilabel:`Notebooks` in the header (or use
the direct link: |nb-url|).

.. tip::

   If you already have an active notebook session, the links above will take you straight to that session.

Step 2. Select a machine image and size
=======================================

The Server Options page lets you select the machine image and size that you’ll work in.

.. _logging-in-image:

Image
-----

The machine images are based on `LSST Science Pipelines`_ Docker images, which are built on the CentOS 7 Linux operating system.

You can choose which version of the LSST Science Pipelines to run:

- Recommended
- Release (``rX.Y``)
- Weekly releases (``YYYY_WW``)
- Daily releases (``YYYY_MM_DD``)

The **Recommended** image is often the best choice because it has update-to-date versions of both the LSST Science Pipelines and supporting Jupyter and Python software, and is backed by additional testing.

For scientific analysis work where reproducibility between Notebook Aspect sessions is important, you may wish to select a specific major or weekly release, and stick with that release for each log in.
To continue using a specific release, you may need to select it from the **historical image** drop down.

For developing with the `LSST Science Pipelines`_, we recommend using the latest daily release to ensure your work is compatible with current versions of Science Pipelines packages.
See :doc:`/guides/notebooks/science-pipelines/science-pipelines-development` for more information.

Options: size
-------------

You can also choose your machine size from the **Server Options** page.
Since the |rsp-at| is a shared resource, try to use the smallest machine possible so that resources are available to other users.

For running data processing tasks with the `LSST Science Pipelines`_, choose the **Medium** or **Large** images to ensure that datasets fit in RAM.

For lightweight tasks, such as editing notebooks or analyzing small datasets, small-scale analyses, the **Small** images will be just fine.

Options: Enable debug logs
--------------------------

Only select this option if requested by Rubin Observatory staff.

Options: Clear the .local directory
-----------------------------------

Only select this option if you are having difficulties starting the Notebook Aspect because Python packages or other software that you installed yourself are now incompatible with the :ref:`image <logging-in-image>` that you want to launch.

Start the Notebook Aspect
-------------------------

Click :guilabel:`Start` to launch into the Notebook Aspect.
