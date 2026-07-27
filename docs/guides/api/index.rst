##########
API aspect
##########

The Application Programming Interface (API) allows users to interact with Rubin Science Platform's data services programmatically or through appropriate clients.

If you are an authorized user, you can use our API services both from within the RSP (e.g., via the RSP's JupyterLab Notebook aspect) and externally from your own computer or other computing facilities you might have access to.
Either way, your API usage is subject to the same quotas and limits, regardless of its origin.

Expect more API services to be added in the future.

Available API services
======================

.. toctree::
   :hidden:

   tap
   sia
   alerts

All Rubin Science Platform APIs are web (REST) services.

.. important::
   You can find the endpoints for all these APIs on the API page accessible from the masthead of the :rsp-link:`RSP homepage <rsp>`.

When possible, our API Services implement relevant `International Virtual Observatory Alliance <https://www.ivoa.net/>`_ (IVOA) protocols.
In some cases, no appropriate IVOA standard exists (or not yet).

IVOA services
-------------

These are best accessed with clients that understand these protocols, such as `PyVO <https://pyvo.readthedocs.io/en/latest>`_.
For other client suggestions, consult the documentation for individual services.

:doc:`tap`
    Catalog and table search via the IVOA `Table Access <https://www.ivoa.net/documents/TAP/20190927/index.html>`_ protocol.

:doc:`sia`
    Image search via the IVOA `Simple Image Access <https://www.ivoa.net/documents/SIA/20150730/index.html>`_ protocol version 2.

**Image cutouts**
    Image cutouts via the IVOA `Server-side Operations for Data Access <https://www.ivoa.net/documents/SODA/20170517/index.html>`_ (SODA) protocol.

**HiPS**
    Survey data via the IVOA `Hierarchical Progressive Survey <https://www.ivoa.net/documents/HiPS/>`_ (HiPS) protocol.


Other REST services
--------------------

:doc:`alerts`
    Retrieval of LSST alerts via Alert ID.


Additional resources
====================

For detailed science-motivated examples of how to use these APIs to access Rubin data, please refer to the `tutorials <https://rubinobservatory.org/for-scientists/resources/tutorials>`_.

Questions? :doc:`Get support </support/index>`.
