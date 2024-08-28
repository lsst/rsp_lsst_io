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

   .. image:: images/RSP_NB_select_a_server.png
       :alt: This image is a screenshot of the Server Options page that users encounter first when they log into the Notebook Aspect. At left, users can select the version of the LSST Science Pipelines that they want to use, with the recommended version pre-selected as the default. At right, users can select a server size of small, medium, or large. Small is pre-selected as the default. Two additional options to enable debug logs or clear the user’s dot-local directory also appear at right. Neither of these options are pre-selected. At the bottom is a button marked start.
       :width: 400
       :name: RSP_NB_select_a_server

A screenshot of the server options available to RSP users, with the default options selected as indicated by the blue filled circles. Users should choose the recommended software version and a medium size.

The term "image" atop the left box refers to a "Docker image" that defines the software packages and their versions which will be automatically loaded in the server environment.
The "recommended" image will be updated on a regular (monthly) basis to encourage users to adapt to using software that is in active development, and to benefit from the bug fixes and updates made by Rubin Observatory staff.
Older images will remain accessible to users.

RSP users who are doing a lot of image processing might need to select a large server, and those who are working with small subsets of catalog data can use a small server.

**Start the Server:**
Pressing the orange "Start" button to start the server returns this page with a blue progress bar:

   .. image:: images/RSP_NB_progress_bar.png
       :alt: This image is a screenshot of the progress bar that displays for a minute or two while a user’s server is starting up in the Notebook Aspect. At the top there is text that says “Your server is starting up” and “You will be redirected automatically when it’s ready for you.” Below that is a progress bar. Underneath the bar, the date and time is shown. This page is not interactive and is replaced by the main work area of the Notebook Aspect once the server has started.
       :width: 400
       :name: RSP_NB_progress_bar

A screenshot of the progress bar that will show while the server is starting up. Be patient. Sometimes it takes a couple of minutes to start a server.

**Navigating the JupyterLab Interface:**
The JupyterLab landing page in the figure below is the launch pad for all JupyterLab functionality (e.g., Notebook, Terminal, Python console).
Return to this launch pad at any time by clicking the plus symbol at upper-left.

.. toctree::
   :maxdepth: 2
   :titlesonly:

   starting-and-stopping/index
   Using the Science Pipelines <science-pipelines/index>
   configuration/index
