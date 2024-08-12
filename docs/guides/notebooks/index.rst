#######################################
Introduction to the RSP Notebook Aspect
#######################################

The Notebook aspect enables you to do scientific analysis in your web browser by running Jupyter Notebooks and shell scripts.
The Notebook aspect is powered by JupyterLab_.

Most RSP users will find Jupyter Notebooks to be the most efficient and powerful way to interact with the LSST data sets.

**Always save and shutdown all notebooks and log out of JupyterLab when you are done with your day's work.**
This is important to preserve resources for other users and to ensure you re-enter the RSP in a known state every time.
To help users avoid issues with stale instances, sessions will be automatically shut-down after 5 days of inactivity, or after 25 days.

This page focuses on the basic instructions for using the RSP Notebook Aspect, and a few FAQs and Troubleshooting Tips.
The full documentation for the RSP Notebook Aspect is available at `nb.lsst.io <https://nb.lsst.io/>`_.

.. _NB-Intro-Login:

How to log in, navigate, and log out of JupyterLab
==================================================

From the RSP landing page at `data.lsst.cloud <https://data.lsst.cloud/>`_ click on the central panel for Notebooks.

**Software Version and Server Size:**
The first page offers a choice of software environment version (left) and server size (right), as shown in the next figure.
Most users will choose the recommended software version and a medium server size.

.. toctree::
   :maxdepth: 2
   :titlesonly:

   starting-and-stopping/index
   Using the Science Pipelines <science-pipelines/index>
   configuration/index
