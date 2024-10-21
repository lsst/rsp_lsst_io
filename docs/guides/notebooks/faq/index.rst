##########################
Frequently Asked Questions
##########################

.. _NB-Intro-Use-A-NB-faq:

Jupyter notebook frequently asked questions
===========================================


.. _NB-Intro-Use-A-NB-faq-kernel:

What is a kernel?
-----------------

In the RSP Notebook Aspect, your notebooks will be operating in a kernel that has access to the full LSST Science Pipelines, including the Butler (see :ref:`NB-Intro-Use-A-NB-faq-butler`, below).
Many standard Python libraries and modules will be available, and users can `install <https://nb.lsst.io/environment/python.html>`_ additional Python tools they wish to use.
See also `this tutorial on installing python packages <https://packaging.python.org/en/latest/tutorials/installing-packages/>`_
(which includes, e.g., use of "pip install").
To view a list of packages available to you, type "pip list" in a terminal.


.. _NB-Intro-Use-A-NB-faq-python:

Is all the code in Python?
--------------------------

Yes, the RSP Notebook Aspect will only have python environments for `Data Preview 0 <https://dp0.lsst.io/>`_ (DP0), which encompasses `Data Preview 0.2`_ (DP0.2; extragalactic and Galactic) and `Data Preview 0.3 <https://dp0-3.lsst.io/>`_ (DP0.3; solar system).

To access data from the Notebook Aspect, users will need to use Python commands and code.
Much of the LSST Science Pipelines code is in Python, and the `DP0.2 tutorial notebooks <https://dp0-2.lsst.io/tutorials-examples/index.html#dp0-2-tutorials-notebooks>`_ use Python as well.
These tutorials contain executable examples of the commands required to access and analyze data.
All DP0 delegates should feel free to copy and paste from the provided tutorials.

Anyone new to Python and looking to learn more might benefit from this `Python for Beginners <https://www.python.org/about/gettingstarted>`_ website (which includes links to tutorial in a variety of languages),
or this Community Forum thread where DP0 delegates can share `resources for python beginners <https://community.lsst.org/t/5975>`_.
Web searches for "python *(thing you want to do)*" are usually pretty successful too.


.. _NB-Intro-Use-A-NB-faq-environments:

How do I install packages in my user environment?
-------------------------------------------------

Basic User Installs
~~~~~~~~~~~~~~~~~~~

The Rubin Science Platform (RSP) comes with the ``rubin-env`` conda environment, including the LSST Science Pipelines, pre-installed and activated within the Notebook and Terminal.
If you need to extend the ``rubin-env`` environment by installing other Python packages to enable your work, you can use the ``pip install`` command.
In the RSP, ``pip`` actually invokes ``conda`` to do its work, ensuring that dependencies that are already present in ``rubin-env`` are used (if compatible).
Packages installed with ``pip`` will be placed in a subdirectory of your home directory.
These packages are only guaranteed to work when the conda environment in which you installed them is activated.

If you need to install other conda packages but don't need to use them at the same time as the ``rubin-env`` and LSST Science Pipelines packages, you can install them into a new conda environment.
Start by doing ``source /opt/lsst/software/stack/loadLSST.bash`` to initialize conda.
Use the ``conda create -n myenv`` command to create the new environment.
Use the ``conda activate myenv`` command to activate this environment.
Use the ``mamba install {package} ...`` command to install one or more packages into the environment.
(``mamba`` is a faster version of conda for installing packages.)
If the package to be installed is not available from the current channels, then the channel will have to be specified, e.g., ``mamba install -c {channel} {package}``.
When you're done using the environment and want to revert to the ``rubin-env`` one, use ``conda deactivate``.

If you need to directly extend the ``rubin-env`` environment with other conda packages, the only way to do so at present is to clone the environment.
This is a time- and space-consuming process, so we do not recommend it.

More Complex User Installs
~~~~~~~~~~~~~~~~~~~~~~~~~~

Suppose one wishes to install a user package on the RSP that has dependencies on non-python libraries.
Typically, these non-python libraries must be installed and built separately, and the ``LD_LIBRARY_PATH`` must be updated.
Leanne Guy created a simple and effective `tutorial notebook for working with user packages <https://github.com/rubin-dp0/tutorial-notebooks/>`_,  using the install of the ``bagpipes`` Bayesian Analysis of Galaxies package as an example.
(The ``bagpipes`` package depends on ``PyMultiNest``, a python interface to the ``MultiNest`` package, which is written in C++.)
The tutorial notebook runs through the steps to user install the ``bagpipes`` package and build its dependencies on the RSP so that it can be used both from the python command line shell and from inside a notebook.

The basic steps are:

1. Open a terminal in the Notebook aspect of the RSP.

2. Install the bagpipes package with :command:`pip`:

   .. code-block:: bash

      pip install --user bagpipes

   (The ``--user`` flag is necessary because you don’t have root access.)

   Among other packages, the above command installs ``PyMultiNest``, a python interface for MultiNest. The ``MultiNest`` package itself is not included.
   Before we can use the ``bagpipes`` package, we must install MultiNest and update the ``LD_LIBRARY`` environment variable.

3. Install and build the dependencies -- in this case, the ``MultiNest`` package -- in your ``~/local`` direcotry.  In a terminal, execute:

   .. code-block:: bash

	cd ~/local
	git clone https://github.com/JohannesBuchner/MultiNest
	cd MultiNest/build
	cmake ..
	make

4. Update the ``LD_LIBRARY_PATH` in your ``~/.bashrc`` file (for terminal-based access):

   .. code-block:: bash

	export LD_LIBRARY_PATH=${LD_LIBRARY_PATH}:${HOME}/local/MultiNest/lib

5. Update the ``LD_LIBRARY_PATH` in your ``~/notebooks/.user_setups`` file (for notebook access):

   .. code-block:: bash

	export LD_LIBRARY_PATH=${LD_LIBRARY_PATH}:${HOME}/local/MultiNest/lib

6. The first time you perfom Steps 4 and/or 5, log out and log back into the RSP.

For more information, please consult `tutorial notebook for working with user packages <https://github.com/rubin-dp0/tutorial-notebooks/>`_.



.. _NB-Intro-Use-A-NB-faq-github:

Do I need to know Git?
----------------------

Although use of Git and GitHub are not necessary for DP0 participation, most Rubin Observatory staff and LSST Science Collaborations use Git and GitHub, and it is highly recommended for all RSP users.
Git is free open-sourced software for change-tracking and version control of any set of files that are edited by one or more contributors.
GitHub is a web-based provider for Git functionality, plus it offers a few of its own features.
In this Community Forum thread, everyone can find and share `resources for learning about Git and GitHub <https://community.lsst.org/t/resources-for-github/6153>`_.
A few of the :ref:`NB-Intro-Use-A-NB-tips` below involve the use of Git.


.. _NB-Intro-Use-A-NB-faq-butler:

What is the Butler, and when do I use it?
-----------------------------------------

The Butler is a `middleware <https://pipelines.lsst.io/middleware/index.html>`_ component of the Data Management System (DMS) for persisting and retrieving datasets.
The third generation "Gen3" Butler is being used for DP0.2.
Full `Butler documentation <https://pipelines.lsst.io/modules/lsst.daf.butler/index.html>`_ is available, and several of the `DP0.2 tutorial notebooks <https://dp0-2.lsst.io/tutorials-examples/index.html#dp0-2-tutorials-notebooks>`_ demonstrate Butler use as well.
The Butler is also described in the paper `The Vera C. Rubin Observatory Data Butler and Pipeline
Execution System <https://ui.adsabs.harvard.edu/abs/2022SPIE12189E..11J/abstract>`_ (Jenness et al. 2022).

The Butler is only accessible via the Notebook Aspect, whereas the Table Access Protocol (TAP) service can be
used via all three aspects.
TAP is generally better for catalog queries as it performs spatial queries faster (e.g., cone searches),
can join tables together, and makes use of ADQL functionality like unit conversions.

However, it is more convenient to use Butler-based catalogs when also using images accessed via the Butler.
The Butler is also used when doing any kind of image reprocessing (e.g., re-doing source detection),
because in that situation the Butler is used for image access and the result is a user-generated catalog persisted by and accessible with Butler.
Furthermore, a few data products are only available via the Butler, such as survey property maps, raw images, and source footprints.

.. _NB-Intro-Use-A-NB-faq-questions:

How do I ask questions about Notebooks?
---------------------------------------

Keep in mind that if you are not experienced at accessing data via Jupyter notebooks, or using a Science Platform more generally, you are not alone!
Most of the DP0 delegates are new to this environment, and all of your questions and feedback will help us improve both the documentation and the tools.

The `DP0 Delegate Homepage <https://dp0.lsst.io>`_ provides information about `getting support <https://dp0.lsst.io/delegate-resources/support.html>`_ at any time via the `Rubin Observatory Community Forum <https://community.lsst.org/>`_ or via GitHub Issues.
Another option is to attend the biweekly `Rubin Science Assemblies <https://dp0.lsst.io/delegate-resources/virtual-events.html#dp0-delegate-resources-virtual-events-assemblies>`_ which will feature live tutorials and question-and-answer time with Rubin Observatory staff.

Beginner-level questions are very welcome, both in the Community Forum and during the Delegate Assemblies.
To encourage questions in the Forum, a couple of beginner-level topics have been started to share resources for
learning `python <https://community.lsst.org/t/resources-for-python-beginners/5975>`_ and `SQL <https://community.lsst.org/t/sql-adql-beginner-resources/6051>`_.
People new to the Rubin Community Forum might appreciate `this video demonstrating how to navigate and post topics to the forum <https://www.youtube.com/watch?v=d_Z5xmkR4P4&list=PLPINAcUH0dXZSx2aY6wTIjLCWiexs3dZR&index=10>`_.


.. _NB-Intro-Use-A-NB-faq-externalrsp:

Can you install the lsst.rsp module outside the RSP?
----------------------------------------------------

Yes, you can indeed install ``lsst.rsp`` on your own computer and run it locally. It is a standard `PyPi package <https://pypi.org/project/lsst-rsp/>`_ and can be installed by using ``pip install lsst-rsp``.

Note that if you want to use it to access data that is hosted at the IDF, you will also need a security token. See this documentation here: https://nb.lsst.io/environment/tokens.html for how to get a security token.

As an example, we will walk through how you can access the Rubin LSST TAP service locally.

After getting an access token, set the value of the environment variable ``ACCESS_TOKEN`` to the path to your token.

Then set the TAP URL endpoint ``EXTERNAL_TAP_URL`` to ``"https://data.lsst.cloud/api/tap"`` (e.g. for macOS, execute the following)

.. code-block:: bash

   export EXTERNAL_TAP_URL="https://data.lsst.cloud/api/tap"

In a python shell or notebook environment, you should then be able to execute the following:

.. code-block:: bash

   from lsst.rsp import get_tap_service, retrieve_query
   service = get_tap_service()
   query = "SELECT * FROM tap_schema.schemas"
   results = service.search(query).to_table()
   print(results)


*Although the LSST environment can be run locally, we strongly recommend to use it in the RSP environment.*



.. _NB-Intro-Use-A-NB-faq-usersettings:

How can the appearance of the user interface be customized?
-----------------------------------------------------------

**The JupyterLab interface**

 * Under "View", selecting "Simple Interface" removes tab navigation from the main work area,
   and the left, right, and status (footer) bar can be shown or not.
 * Under "Settings - Theme", options for JupyterLab Dark and Light are available, and this theme applies
   to the entire user interface and notebooks.
 * This theme will also apply to the text editor if the text editor theme is "jupyter",
   and to the terminal if the terminal theme is "inherit".

**Jupyter Notebooks**

 * Under "View", selecting "Presentation Mode" makes the fonts larger in a Jupyter Notebook open in the main work area.
 * Under "View", selecting "Show Line Numbers" adds line numbers to the left side of every code cell or unexecuted markdown cell.
 * Under "Settings - Theme", selecting "Theme Scrollbars" makes the right-hand notebook scrollbar permanent in Dark Mode.
 * Under "Settings - Theme" it is possible to increase and decrease code font size (applies to code cells and unexecuted markdown cells) and content font size (applies to executed markdown cells).
 * It is also possible to independently increase and decrease the user interface font size, which applies to the menu bar, side bar, and status bar (footer bar).
 * All of these font size changes will be applied independent of changes to the browser font size, and apply only to Notebooks.

**Text editor**

 * Under "Settings" there are options to increase or decrease text editor font size, choose the preferred text editor indentation (spaces or tabs), and set the editor theme (includes options for, e.g., dark and light modes).
 * Text files saved with, e.g., a .py extension, will have syntax highlighting enabled automatically. If the text editor theme is "jupyter", the theme will be inherited from the JupyterLab theme.

**Terminal**

 * Under "Settings" there are options to increase or decrease the terminal font size and
   choose light or dark mode.
 * If the terminal theme is "inherit", the theme will be inherited from the JupyterLab theme.
 * Note that the text editor emacs is available, but in the terminal, and so the terminal
   options apply when using emacs in-terminal.

**Advanced Settings Editor**

 * At the bottom of the "Settings" drop-down menu is an advanced settings editor.
 * Font families, cursor blink rates, and a wide variety of other customizable parameters
   are available.

**Restore to Defaults**

 * Changes to settings are saved between Notebook Aspect sessions.
 * In the advanced settings editor, a list of the settings that have been modified floats to the top.
 * Click on any modified setting and find, at right, the option to click "Restore to Defaults" to undo every change that has been made.


.. _NB-Intro-Use-A-NB-tips:

Troubleshooting tips
====================

How to recover from package import errors (ImportError)
-------------------------------------------------------

**The Problem:** In this case the problem manifests when a package cannot be properly imported.
This leads to an ImportError for which the last line of the traceback actually points to the file it is trying to import from, and it is in the user's ".local" directory.

If a user sees a mention of ".local" anywhere in the exception, there is a chance they have installed packages that are polluting stack environments, and this is a big red flag that following the solution below will be necessary.

However, this is not the only way this problem can manifest, as issues with user-installed packages can be hard to track down. E.g., it might import fine, but then not be able to find an attribute or method on a particular object.

**The Solution:** Users should exit the RSP and then clear their ".local" file when they log back in to the Notebook Aspect by checking the box "Clear .local directory (caution!)"
on the Hub spawner page (see the "Server Options" image at the top of this page).
This option is simple and effective, and also helps in cases where the user-installed packages are keeping JupyterLab from starting.

**An Alternative Solution:** The user should first close and shutdown the notebook (or, e.g., ipython session) which is experiencing the error, and then launch a terminal in the Notebook Aspect
and move their ".local" file out of the way by renaming it as something else, such as:

.. code-block:: bash

   mv ~/.local ~/.local_[YYYY][MM][DD]

There will be no need to recreate the ".local" directory after this.
The user should then restart the notebook (or, e.g., ipython session) and try to import the packages.


How to make Git stop asking for my password
-------------------------------------------

It is recommended that all Git users working in the RSP configure Git and set up an SSH key.
First, using a terminal in the Notebook aspect, set the global Git configurations.

.. code-block:: bash

   git config --global user.email yourEmail@yourdomain
   git config --global user.name GitUsername

Then, using a terminal in the Notebook aspect, follow these instructions for `generating a new SSH key and adding it to the ssh-agent <https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent?platform=linux>`_.
Be sure to follow the instructions for the Linux environment (i.e., the RSP environment), regardless of your personal computer's environment, because you are generating an SSH key *for your account in the RSP*.

When you ``git clone`` new repositories, use the SSH key.
If successful, you will be able to ``git fetch`` and ``git push`` without entering your Git password.
