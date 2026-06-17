###########################
lsst.rsp — Python utilities
###########################

The ``lsst.rsp`` package provides Python helpers for working inside the Rubin Science Platform Notebook aspect.
These utilities handle common tasks such as connecting to the platform's TAP service, retrieving access tokens, and interacting with other RSP services.
For example, the :func:`~lsst.rsp.get_tap_service` helper returns a ready-to-use client for querying LSST catalogs:

.. code-block:: python

   from lsst.rsp import get_tap_service

   service = get_tap_service("tap")

The ``lsst.rsp`` package is pre-installed in the RSP Notebook environment, so it is available to import in any notebook or terminal session without additional setup.

This reference documents the latest released version of ``lsst.rsp``.
To use the package outside the RSP — for example, on a local machine — install it from PyPI:

.. code-block:: bash

   pip install lsst-rsp

.. automodapi:: lsst.rsp
   :skip: RSPInternalDiscovery
   :skip: format_bytes
   :skip: forward_lsst_log
   :skip: IPythonHandler
