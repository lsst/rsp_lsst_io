############################
Simple Image Access (SIA)
############################

The `Simple Image Access v2 <https://www.ivoa.net/documents/SIA/>`_ (SIAv2) service allows you to search for Rubin images by sky position, time, filter, or calibration level.
The RSP Portal (Firefly) includes an SIA interface to discover images, and the same service is available for direct programmatic access.
Queries return metadata about matching images rather than the images themselves. Each result includes an ``access_url`` you can use to download the file or follow a DataLink to related data products.

.. note::

   Access to the SIA service requires an RSP token with the ``read:image`` scope.
   For internal access from the Notebook aspect this token is provided automatically.
   For external access, see :doc:`/guides/auth/creating-user-tokens`.

SIA endpoint
============

The SIA service is organised by data collection.

.. jinja:: rsp

   {% if env.api_url %}
   The base URL for a given collection is ``{{ env.api_url }}/sia/{collection}``, where ``{collection}`` identifies the data release, for example, ``dp1``.
   {% else %}
   Contact your RSP administrator for the SIA endpoint URL for this deployment.
   {% endif %}

Querying with PyVO
==================

`PyVO <https://pyvo.readthedocs.io/en/latest>`_ is the recommended Python client for the SIA service and is pre-installed in the RSP Notebook environment.
Inside the RSP Notebook aspect, connect using the pre-authenticated convenience function:

.. code-block:: python

   from lsst.rsp.service import get_siav2_service

   sia_service = get_siav2_service("dp1")

For external access from outside the RSP, see `External access`_ below.

Searching by position
----------------------

Positions are ICRS RA and Dec in degrees, and the third value is the search radius:

.. code-block:: python

   results = sia_service.search(pos=(53.01, -28.35, 0.05))
   table = results.to_table()

You can also combine parameters to narrow results.
For example, to filter by calibration level and dataset type:

.. code-block:: python

   results = sia_service.search(
       pos=(53.01, -28.35, 0.05),
       calib_level=3,
       dpsubtype="lsst.deep_coadd",
   ).to_table()

Working with results
---------------------

Each row in the results table contains an ``access_url`` field.
When ``access_format`` is ``application/fits``, this URL is a direct link to a FITS image.
When ``access_format`` is ``application/x-votable+xml;content=datalink``, the URL points to a DataLink endpoint listing available data products for that image:

.. code-block:: python

   from pyvo.dal.adhoc import DatalinkResults

   # Pick a result row
   row = results[0]

   if "datalink" in row.access_format:
       dl = DatalinkResults.from_result_url(row.access_url)
       image_url = dl.getrecord(0).get("access_url")
   else:
       image_url = row.access_url

External access
===============

The SIA service is accessible from outside the RSP using an RSP token as a password with the username ``x-oauth-basic``:

.. code-block:: python

   import requests
   from pyvo.dal import SIA2Service

   token = "your-rsp-token"
   session = requests.Session()
   session.headers["Authorization"] = f"Bearer {token}"

   sia_service = SIA2Service("SIA_URL", session=session)

Query parameters
================

The SIA service accepts the following query parameters.
All parameter names are case-insensitive.

.. list-table::
   :header-rows: 1
   :widths: 20 80

   * - Parameter
     - Description
   * - ``POS``
     - Sky position and search region in ICRS degrees. Formats: ``CIRCLE ra dec radius``, ``RANGE ra1 ra2 dec1 dec2``, ``POLYGON ra1 dec1 ...``
   * - ``TIME``
     - Time interval to search, as MJD values. Use ``-Inf`` or ``+Inf`` for open-ended ranges.
   * - ``BAND``
     - Wavelength range in metres.
   * - ``CALIB``
     - Calibration level: ``0`` raw, ``1`` calibrated, ``2`` science-ready, ``3`` contributed.
   * - ``EXPTIME``
     - Exposure time range in seconds.
   * - ``INSTRUMENT``
     - Instrument name.
   * - ``DPTYPE``
     - Data product type, e.g. ``image`` or ``cube``.
   * - ``DPSUBTYPE``
     - Rubin-specific dataset type, e.g. ``lsst.deep_coadd``.
   * - ``MAXREC``
     - Maximum number of rows to return. Set to ``0`` to retrieve only the service self-description.
   * - ``ID``
     - Dataset identifier.

SIA sub-endpoints
=================

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Path
     - Purpose
   * - ``/{collection}/query``
     - Execute an SIAv2 query. Supports both GET and POST.
   * - ``/{collection}/availability``
     - Check whether the service and underlying data repository are available (VOSI).
   * - ``/{collection}/capabilities``
     - Describe service capabilities and supported parameters (VOSI).

Questions? :doc:`Get support </support/index>`.
