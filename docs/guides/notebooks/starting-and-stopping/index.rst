###############################################
Starting and Stopping a Notebook Aspect Session
###############################################

.. _NB-Intro-Login:

How to log in, navigate, and log out of JupyterLab
==================================================

From the RSP landing page at `data.lsst.cloud <https://data.lsst.cloud/>`_ click on the central panel for Notebooks.

**Software Version and Server Size:**
The first page offers a choice of software environment version (left) and server size (right), as shown in the next figure.
Most users will choose the recommended software version and a medium server size.

  .. figure:: images/RSP_NB_select_a_server.png
      :alt: This image is a screenshot of the Server Options page that users encounter first when they log into the Notebook Aspect. At left, users can select the version of the LSST Science Pipelines that they want to use, with the recommended version pre-selected as the default. At right, users can select a server size of small, medium, or large. Small is pre-selected as the default. Two additional options to enable debug logs or clear the user’s dot-local directory also appear at right. Neither of these options are pre-selected. At the bottom is a button marked start.
      :width: 400
      :name: RSP_NB_select_a_server

      A screenshot of the server options available to RSP users, with the default options selected as indicated by the blue filled circles.

The term "image" atop the left box refers to a "Docker image" that defines the software packages and their versions which will be automatically loaded in the server environment.
The "recommended" image will be updated on a regular (monthly) basis to encourage users to adapt to using software that is in active development, and to benefit from the bug fixes and updates made by Rubin Observatory staff.
Older images will remain accessible to users.

RSP users who are doing a lot of image processing might need to select a large server, and those who are working with small subsets of catalog data can use a small server.

**Start the Server:**
Pressing the orange "Start" button to start the server returns this page with a blue progress bar:

  .. figure:: images/RSP_NB_progress_bar.png
      :alt: This image is a screenshot of the progress bar that displays for a minute or two while a user’s server is starting up in the Notebook Aspect. At the top there is text that says “Your server is starting up” and “You will be redirected automatically when it’s ready for you.” Below that is a progress bar. Underneath the bar, the date and time is shown. This page is not interactive and is replaced by the main work area of the Notebook Aspect once the server has started.
      :width: 400
      :name: RSP_NB_progress_bar

      A screenshot of the progress bar that will show while the server is starting up. Be patient. Sometimes it takes a couple of minutes to start a server.

**Navigating the JupyterLab Interface:**
The JupyterLab landing page in the figure below is the launch pad for all JupyterLab functionality (e.g., Notebook, Terminal, Python console).
Return to this launch pad at any time by clicking the plus symbol at upper-left.

  .. figure:: images/RSP_NB_launcher_options.png
      :alt: This image is a screenshot of the main work area of the Notebook Aspect, as it appears when a user starts a new server. Across the top is the main menu, with options such as file, edit, view, run, kernel, rubin, tabs, settings, and help. The left sidebar offers options to browse the file system, open files, and upload data. At right, in the main work area, one tab is open. It is the launcher tab, which offers options to open a new notebook, coding console, terminal, text file, markdown file, python file, or help file.
      :width: 400
      :name: RSP_NB_launcher_options

      The JupyterLab landing page from which several tools can be launched and the file system can be browsed (left sidebar).

In the very left-most vertical sidebar of icons, the top icon is a file folder, and that is the default view.
The left sidebar lists folders in the user's home directory (e.g., DATA, WORK, and notebooks).
Launching a terminal (the default is a linux bash terminal) and using the command "ls" will return the same list.
Navigate the file system and open files by double-clicking on folders and files in the left sidebar.
Clicking the folder icon above the list of files will take you back to your home directory.

Although the file browser is a handy way to navigate the user home space, it does not allow navagating to e.g., the shared data space.
One way to make other spaces available in the file browser is to create a `symbolic link <https://en.m.wikipedia.org/wiki/Symbolic_link>`_ pointing to the desired resource using the Terminal, with this symbolic link placed somewhere in the home directory.

**Safely Log Out of JupyterLab:**
Use the "File" menu in the top menu bar.
To safely shut down a Notebook, choose "Close and Shutdown Notebook".
Note that clicking the "x" on a Notebook tab does not shut down the Notebook's kernel.
To safely shut down a JupyterLab server and log out of the RSP, choose "Save all, Exit, and Log Out".
It is recommended to log out every time upon finishing with a session in order to both preserve resources for other users and to ensure re-entering the RSP in a known state every time.
To help users avoid issues with stale instances, sessions will be automatically shut-down after 5 days of inactivity, or after 25 days.
