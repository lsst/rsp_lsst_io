##############################
Alerts API
##############################

The Alerts API provides access to LSST alert packets via a phalanx service named Herald.
These alert packets are the per-detection records produced by the Alert Production pipeline whenever a transient, variable, or moving source is found in a nightly difference image.
Each packet contains source measurements, a historical light curve, and postage stamp cutout images, and can be retrieved in Avro, FITS, or JSON format.
This API can be used programmatically, while the RSP Portal (Firefly) also provides a user interface for browsing and inspecting alert packets.

.. note::

   Access to the Alerts API requires authentication.
   See :doc:`/guides/auth/index` for instructions on generating an RSP access token.

Alert IDs
=========

Every alert has a unique integer ID.
The API accepts IDs in two forms:

- **Bare integer** - e.g., ``12345``
- **IAU format** - e.g., ``LSST-AP-DS-12345``

Endpoints
=========

All endpoints are available under ``/api/alerts``.

Retrieve an alert packet
------------------------

``GET /api/alerts?ID=<alert_id>``

Returns the full alert packet for the given ID.
Use the ``RESPONSEFORMAT`` parameter to select the format:

.. list-table::
   :header-rows: 1
   :widths: 20 40 40

   * - Format
     - ``RESPONSEFORMAT`` value
     - Content type
   * - Avro OCF (default)
     - *(omit parameter)*
     - ``application/x-avro-ocf``
   * - FITS
     - ``fits`` or ``application/fits``
     - ``application/fits``
   * - JSON
     - ``json`` or ``application/json``
     - ``application/json``

The Avro OCF format includes the schema embedded in the container and is the most compact representation.
In JSON, binary fields (cutouts) are Base64-encoded.

The FITS format is described in detail below.

FITS file structure
~~~~~~~~~~~~~~~~~~~

The alert FITS file is a multi-extension file with the following HDUs, in order:

.. list-table::
   :header-rows: 1
   :widths: 20 15 65

   * - EXTNAME
     - Type
     - Contents
   * - *(primary)*
     - ``PrimaryHDU``
     - Empty data array. Headers: ``TELESCOP = Rubin Observatory``, ``INSTRUME = LSSTCam``.
   * - ``ALERT``
     - ``BinTableHDU``
     - One row containing top-level scalar alert fields. Columns from ``diaObject`` (for stellar/galactic sources) or ``ssObject`` and ``mpc_orbits`` (for solar system objects) are merged into this HDU rather than placed in separate extensions.
   * - ``DIFFIM``
     - ``ImageHDU``
     - Difference image postage stamp (present when available).
   * - ``SCIENCE``
     - ``ImageHDU``
     - Science image postage stamp (present when available).
   * - ``TEMPLATE``
     - ``ImageHDU``
     - Template image postage stamp (present when available).
   * - ``DIASOURCE``
     - ``BinTableHDU``
     - Source detections. Row 0 is the triggering detection. Subsequent rows are previous detections (``prvDiaSources``). Includes two extra columns: ``trigger`` (boolean, ``True`` for the detection that triggered the alert, ``False`` for historical detections) and ``iau_id`` (IAU-format string identifier for each detection). ``psfFlux`` is placed immediately after ``midpointMjdTai`` to facilitate light-curve plotting.
   * - ``FORCEDPHOT``
     - ``BinTableHDU``
     - Forced-photometry measurements at the source position (``prvDiaForcedSources``). Zero or more rows.
   * - ``SSSOURCE``
     - ``BinTableHDU``
     - Solar system source record (``ssSource``). Zero or one rows. Present only for moving-object alerts.


Retrieve cutout images
----------------------

``GET /api/alerts/cutouts?ID=<alert_id>``

Returns a multi-extension FITS file containing only the postage stamp cutout images for the alert, without source measurements.
This is useful when you need the cutouts quickly without the overhead of the full alert packet.
The file contains a primary HDU followed by up to three image extensions (``DIFFIM``, ``SCIENCE``, and ``TEMPLATE``)
each present only when the corresponding cutout is available in the alert.

Retrieve the Avro schema
------------------------

``GET /api/alerts/schema?ID=<alert_id>``

Returns a JSON representation of the Avro schema used to serialize the given alert.
This endpoint allows clients to discover the schema for a specific alert, which can be useful for parsing the
packet or understanding its structure.

DataLink
--------

``GET /api/alerts/links?ID=<alert_id>``

Returns a DataLink VOTable listing all available data products for the alert, including the packet itself, cutout images, and schema.
This endpoint follows the `IVOA DataLink <https://www.ivoa.net/documents/DataLink/>`_ standard and can be used by VO-aware tools to discover related resources.

Questions? :doc:`Get support </support/index>`.
