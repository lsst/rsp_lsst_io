##############################
Table Access Protocol (TAP)
##############################

The `Table Access Protocol <https://www.ivoa.net/documents/TAP/20190927/index.html>`_ (TAP) service allows you to query Rubin catalog tables from a notebook, a script, or an external tool like `TOPCAT <https://www.star.bris.ac.uk/~mbt/topcat/>`_.
The RSP Portal (Firefly) also uses the TAP service to power its catalog queries.
Queries are written in `ADQL <https://www.ivoa.net/documents/ADQL/>`_, a dialect of SQL that adds geometry functions for cone searches, polygon queries, and spatial joins.
Results come back as `VOTable <https://www.ivoa.net/documents/VOTable/>`_, which PyVO converts automatically to an astropy Table.

.. note::

   Access to the TAP service requires an RSP token with the ``read:tap`` scope.
   For internal access from the Notebook aspect this token is provided automatically.
   For external access, see :doc:`/guides/auth/creating-user-tokens`.

TAP endpoint
============

.. jinja:: rsp

   {% if env.api_tap_url %}
   The TAP service is available at |rsp-tap-url|.
   {% else %}
   Contact your RSP administrator for the TAP endpoint URL for this deployment.
   {% endif %}

Querying with PyVO
==================

`PyVO <https://pyvo.readthedocs.io/en/latest>`_ is the recommended Python client for the TAP service and is pre-installed in the RSP Notebook environment.
Inside the RSP Notebook aspect, it is available via a pre-configured helper function that returns a TAPService object connected to the RSP TAP endpoint (including authentication):

.. code-block:: python

   from lsst.rsp import get_tap_service

   tap_service = get_tap_service("tap")

For external access from outside the RSP, see `External access`_ below.

Asynchronous queries (recommended)
-----------------------------------

For most queries,  the asynchronous interface is the preferrred query method.
The synchronous endpoint imposes a short server-side timeout (< 1 minute) that is easily exceeded by any non-trivial query, and are also subject to http client timeouts.
Asynchronous jobs run to completion regardless of how long they take.

.. code-block:: python

   job = tap_service.submit_job(
       "SELECT ra, dec, psfFlux FROM dp1.DiaSource WHERE psfFlux > 1000"
   )
   job.run()
   job.wait(phases=["COMPLETED", "ERROR"])
   job.raise_if_error()

   table = job.fetch_result().to_table()  # astropy Table
   job.delete()

Call ``job.delete()`` when you are done with the results to free server-side resources.

For straightforward queries where you don't need to inspect the job object, ``run_async`` wraps the full process into a single call:

.. code-block:: python

   table = tap_service.run_async(
       "SELECT ra, dec, psfFlux FROM dp1.DiaSource WHERE psfFlux > 1000"
   ).to_table()

The explicit form can be used when you need control over timeout, job status polling, or error handling, but in most cases the simpler ``run_async`` is sufficient.
Worth noting that ``run_async`` will call ``job.delete()`` for you, so the job will not be visible in the `UWS job list`_ after the job has completed.
There is however a way to keep the job around for inspection after completion by passing ``delete=False`` to ``run_async``.

Synchronous queries
--------------------

Use synchronous queries only for quick exploratory work where you know the result will be small and fast.
For example, it can be used to fetch a handful of rows to inspect a table's columns.
Because the sync endpoint is a plain HTTP GET, you can also run a quick query directly in a browser by appending your ADQL query to the ``/sync`` endpoint URL as a ``QUERY`` parameter.

.. code-block:: python

   results = tap_service.search("SELECT TOP 10 * FROM dp1.DiaSource")
   table = results.to_table()

UWS job list
------------

Asynchronous jobs are managed by the `Universal Worker Service <https://www.ivoa.net/documents/UWS/>`_ (UWS) protocol.
Each job is assigned a URL you can use to check its status, retrieve its results, or delete it.
PyVO tracks the job URL automatically when you use ``submit_job``, but you can also browse your active and recently completed jobs directly.

.. jinja:: rsp

   {% if env.api_tap_url %}
   The job list is available at ``{{ env.api_tap_url }}/async``.
   {% else %}
   Contact your RSP administrator for the UWS job list URL for this deployment.
   {% endif %}

The RSP Portal displays the same list under its **Job Monitor** tab.

External access
===============

The TAP service is also accessible from outside the RSP, for example from a personal computer running PyVO or `TOPCAT <https://www.star.bris.ac.uk/~mbt/topcat/>`_.
External clients authenticate by passing an RSP token as a password with the username ``x-oauth-basic``:

For example, with PyVO:

.. code-block:: python

   import pyvo as vo
   from pyvo.auth import AuthSession

   token = "your-rsp-token"
   session = AuthSession()
   session.credentials.set_password("x-oauth-basic", token)

   tap_service = vo.dal.TAPService("<TAP_URL>", session=session)

For a step-by-step walkthrough of connecting TOPCAT to the TAP service, see :doc:`/guides/auth/using-topcat-outside-rsp`.

TAP sub-endpoints
=================

The TAP service exposes the following sub-endpoints.
VO clients handle these transparently and will not require you to interact with them directly, but they are listed here for completeness.

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Path
     - Purpose
   * - ``/sync``
     - Execute a synchronous ADQL query. Subject to a short server-side timeout.
   * - ``/async``
     - Submit and manage asynchronous UWS jobs.
   * - ``/tables``
     - Retrieve table and column metadata (TAP_SCHEMA).
   * - ``/capabilities``
     - Describe service capabilities and supported standards.
   * - ``/availability``
     - Check whether the service is currently available.

Related services
================

The RSP TAP service also exposes an **ObsTAP** interface (`Observation Table Access Protocol <https://www.ivoa.net/documents/ObsCore/>`_) for querying image metadata using the standardised ``ivoa.ObsCore`` table.

Questions? :doc:`Get support </support/index>`.
