################
Using the Portal
################

The best way to learn how to use the Portal is to work through the tutorials that
are available in the documentation for each data release.

.. toctree::
   :titlesonly:
   :maxdepth: 2
   :caption: How-to guides

   portal-tutorials


Navigate the main landing page
------------------------------

From the main landing page (see the figure below), click on any tab to go to the graphical user interface for querying data.

  .. figure:: images/portal_landing.png
      :alt: A screenshot of the Portal landing page with tabs and links to access the Portal query interfaces.
      :width: 400
      :name: portal_landing_2

      A screenshot of the Portal's main landing page after log in.


Access the menu
---------------

In the figure above, at upper left there is a menu icon (three horizontal bars).
Click on it to reveal the full menu of options.

  .. figure:: images/portal_sidebar.png
      :alt: A screenshot of the Portal's sidebar.
      :width: 200
      :name: portal_sidebar

      A screenshot of the Portal's sidebar menu options.


Choose a tab to interact with data
----------------------------------

To interact with data, click on one of the tabs that are displayed across the top of the Portal window, or one of the menu options from the menu shown above. There are menu options (which will open new tabs) with the following functionalities:

* **Catalogs**: query catalog data products, either via an interactive GUI, or with ADQL queries
* **Images**: search for images, including Rubin data as well as images from the IRSA archives
* **HiPS**: find `HiPS <https://aladin.cds.unistra.fr/hips/>`_ (Hierarchical Progressive Survey) images created from the Rubin deep coadd images
* **Multi-archive TAP**: execute ADQL queries to retrieve catalogs from external (non-Rubin) TAP tables
* **Upload**: upload your own tables, which can then be joined with Rubin catalogs
* **Job Monitor**: check the status of your executed queries, see the actual query and information about the results (for completed queries)
* **Results**: see the catalogs and/or images resulting from your executed queries, and interact with them. The image viewer and interactive plotting tools are based on `Firefly <https://data-int.lsst.cloud/portal/app/onlinehelp/>`_, which is built by `IPAC <https://www.ipac.caltech.edu/>`_.


Execute a query and view results
--------------------------------

Exactly how to execute a query and view the results depends on which datasets are
queried, and the type of data retrieved (e.g., images or catalogs).
Image and catalog queries can be done by specifying desired search parameters in the user interface,
or may be entered directly as `ADQL <https://www.ivoa.net/documents/ADQL/>`_ queries.
Users can toggle between the two view using the ``View`` buttons at the upper right of the query tabs (labeled ``UI assisted`` and ``Edit ADQL``).

In addition to the general :ref:`Portal tutorials <portal-tutorials>`,
the specific tutorials that accompany every data release are the best resource
for learning how to query and visualize LSST data.


Switch to dark mode
-------------------

Access the menu as described above.
At the bottom of the menu, switch from "Light" to "Dark" mode,
or set the Portal to match your local system's settings.
