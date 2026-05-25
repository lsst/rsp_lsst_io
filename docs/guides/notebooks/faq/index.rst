##########################
Frequently Asked Questions
##########################

.. _NB-Intro-Use-A-NB-faq-python:

Is all the code in Python?
--------------------------

Yes, the RSP Notebook Aspect will only have python environments.

To access data from the Notebook Aspect, users will need to use Python commands and code.
Much of the LSST Science Pipelines code is in Python, and the Rubin/LSST tutorial notebooks use Python as well.
These tutorials contain executable examples of the commands required to access and analyze data.
All Rubin/LSST users should feel free to copy and paste from the provided tutorials.

Anyone new to Python and looking to learn more might benefit from this `Python for Beginners <https://www.python.org/about/gettingstarted>`_ website (which includes links to tutorials in a variety of languages),
or this Community Forum thread where Rubin/LSST users can share `resources for python beginners <https://community.lsst.org/t/5975>`_.
Web searches for "python ..." are usually pretty successful too.

.. _NB-Intro-Use-A-NB-faq-butler:

What is the Butler, and when do I use it?
-----------------------------------------

The Butler is a `middleware <https://pipelines.lsst.io/middleware/index.html>`_ component of the Data Management System (DMS) for persisting and retrieving datasets.
The third generation "Gen3" Butler is being used.
Full `Butler documentation <https://pipelines.lsst.io/modules/lsst.daf.butler/index.html>`_ is available, and several of the Rubin/LSST tutorial notebooks demonstrate Butler use as well.
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

.. _NB-Intro-Use-A-NB-faq-externalrsp:

Can the lsst.rsp module be installed outside the RSP?
-----------------------------------------------------

Yes, it is possible to install ``lsst.rsp`` on one's own computer and run it locally. It is a standard `PyPi package <https://pypi.org/project/lsst-rsp/>`_ and can be installed by using ``pip install lsst-rsp``.

Note that accessing data that are hosted at the IDF will additionally require a security token. See this documentation here: https://nb.lsst.io/environment/tokens.html for how to get a security token.

As an example, we will walk through how to access the Rubin LSST TAP service locally.

After getting an access token, set the value of the environment variable ``ACCESS_TOKEN`` to the path to the token.

Then set the TAP URL endpoint ``EXTERNAL_TAP_URL`` to ``"https://data.lsst.cloud/api/tap"`` (e.g. for macOS, execute the following)

.. code-block:: bash

   export EXTERNAL_TAP_URL="https://data.lsst.cloud/api/tap"

In a python shell or notebook environment, it should then be possible to execute the following:

.. code-block:: bash

   from lsst.rsp import get_tap_service, retrieve_query
   service = get_tap_service()
   query = "SELECT * FROM tap_schema.schemas"
   results = service.search(query).to_table()
   print(results)


*Although the LSST environment can be run locally, we strongly recommend to use it in the RSP environment.*


Is the rubin_sim/rubin_scheduler data available on the RSP?
-----------------------------------------------------------

A shared copy of the current rubin_sim data is available under '/rubin/rubin_sim_data'. Adding an environment variable for RUBIN_SIM_DATA_DIR to your notebook or symlinking '/rubin/rubin_sim_data' to your home directory under 'rubin_sim_data' will let the rubin_sim package find the shared data.

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


How to make Git stop asking for my password?
--------------------------------------------

Follow the :doc:`guide on configuring Git and credentials <../configuration/git-configuration>` to set your Git username and set up credentials for services like GitHub.

