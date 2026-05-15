##########
API aspect
##########

The Application Programming Interface (API) allows users to interact with Rubin's data services remotely.
An API is a structured way for software applications to communicate with each other.
It can be thought of as a back-and-forth exchange between a client and a server: one program (the client) makes a request for data, and another program (the server) provides a response.

In the context of the RSP, the API aspect allows access to Rubin data—including images and catalogs—both within the RSP environment (e.g., via the RSP JupyterLab Notebook aspect) and externally (e.g., through the Tool for OPerations on Catalogues And Tables (`TOPCAT <https://www.star.bris.ac.uk/~mbt/topcat/>`_), a personal computer with the `PyVO <https://pyvo.readthedocs.io/en/latest>`_ software, or a `PyVO <https://pyvo.readthedocs.io/en/latest>`_-enabled environment like the National Optical-Infrared Astronomy Research Laboratory's `Astro Data Lab <https://datalab.noirlab.edu/>`_).

**Use the API Aspect to:**

- Access Rubin data from outside the RSP.
- Automate data queries or downloads.
- Integrate Rubin data access into your own software tools.
- Access external datasets in addition to Rubin data.

API Services
============

The API aspect of the RSP supports several types of services, primarily based on the `International Virtual Observatory Alliance <https://www.ivoa.net/>`_ (IVOA) protocols.
These include the `Table Access Protocol <https://www.ivoa.net/documents/TAP/20190927/index.html>`_ (TAP), the `Observation Table Access Protocol <https://www.ivoa.net/documents/ObsCore/>`_ (ObsTAP), the `Server-side Operations for Data Access <https://www.ivoa.net/documents/SODA/20170517/index.html>`_ (SODA) service (which provides image cutouts and mosaics), the `Simple Image Access Protocol version 2 <https://www.ivoa.net/documents/SIA/20150730/index.html>`_ (SIAv2) for image searches, and the `Hierarchical Progressive Survey <https://www.ivoa.net/documents/HiPS/>`_ (HiPS).

By the time of the first data release, the Rubin Science Platform will also support the `Simple Cone Search (SCS) <https://www.ivoa.net/documents/latest/ConeSearch.html>`_ for basic catalog queries, and the `Virtual Observatory Space <https://www.ivoa.net/documents/VOSpace/>`_ (VOSpace)—alongside `Web Distributed Authoring and Versioning <https://en.wikipedia.org/wiki/WebDAV>`_ (WebDAV)—for user file access.

.. toctree::
   :maxdepth: 2
   :titlesonly:

   tap
   sia
   alerts

Additional Resources
====================

For more information about Rubin data access, please refer to the `tutorials <https://rubinobservatory.org/for-scientists/resources/tutorials>`_.
For the most recent data releases, visit the `Rubin Observatory page <https://rubinobservatory.org/for-scientists/data-products/recent-data-releases>`_.

Questions? :doc:`Get support </support/index>`.
