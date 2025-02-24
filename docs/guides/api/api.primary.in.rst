The Application Programming Interface (API) allows users to interact with Rubin's data services remotely.
An API (Application Programming Interface) is a structured way for software applications to communicate with each other.
It can be thought of as a back-and-forth exchange between a client and a server: one program (the client) makes a request for data, and another program (the server) provides a response.

In the context of the RSP, the API aspect allows access to Rubin data—including images and catalogs—both within the RSP environment (e.g., via the RSP JupyterLab Notebook aspect) and externally (e.g., through the Tool for OPerations on Catalogues And Tables (`TOPCAT <https://www.star.bris.ac.uk/~mbt/topcat/>`_) or a `PyVO <https://pyvo.readthedocs.io/en/latest>`_-enabled environment like the National Optical-Infrared Astronomy Research Laboratory’s `Astro Data Lab <https://datalab.noirlab.edu/>`_).

**Use the API Aspect to:**

- Access Rubin data from outside the RSP.
- Automate data queries or downloads.
- Integrate Rubin data access into your own software tools.
- Access to external datasets in addition to Rubin data.

API Services
============

The API aspect of the RSP supports several types of services.
These include the `Table Access Protocol <https://www.ivoa.net/documents/TAP/20190927/index.html>`_ (TAP),  `Observation Table Access Protocol <https://www.ivoa.net/documents/ObsCore/>`_ (ObsTAP), the `Server-side Operations for Data Access <https://www.ivoa.net/documents/SODA/20170517/index.html>`_ (SODA) service (which provides image cutouts and mosaics), and the `Hierarchical Progressive Survey <https://aladin.cds.unistra.fr/hips/>`_ (HiPS).

By the time of the first data release, the Rubin Science Platform will also support the `Simple Cone Search (SCS) <https://www.ivoa.net/documents/latest/ConeSearch.html>`_ for basic catalog queries, `Simple Image Access Protocol version 2 <https://www.ivoa.net/documents/SIA/20150730/index.html>`_ (SIAv2) for image searches, and `Virtual Observatory Space <https://www.ivoa.net/documents/VOSpace/>`_ (VOSpace)—alongside `Web Distributed Authoring and Versioning <https://en.wikipedia.org/wiki/WebDAV>`_ (WebDAV)—for user file access.


Table Access Protocol (TAP) Service
===================================

The `Table Access Protocol <https://www.ivoa.net/documents/TAP/20190927/index.html>`_ (TAP) is a specific type of service within the API, implemented according to the `International Virtual Observatory Alliance <https://www.ivoa.net/>`_ (IVOA) standard.

Internal and External TAP Services
-----------------------------------

The RSP TAP service is available in two configurations:

**Internal TAP Service**

The primary means of accessing TAP within the RSP is through the RSP’s Portal and Notebook aspects.
In the Notebook aspect, a TAP service is instantiated within a Python notebook and used to execute an Astronomical Data Query Language (ADQL) query, returning a result set.

**External TAP Service**

The external TAP service is also accessible outside the RSP (e.g., from a personal computer), allowing users to query data using external software such as `PyVO <https://pyvo.readthedocs.io/en/latest>`_, `TOPCAT <https://www.star.bris.ac.uk/~mbt/topcat/>`_, or custom scripts.
To access TAP from external software, users must generate an RSP access token.

*Authentication and Access Tokens*

Access to Rubin data via the API requires authentication.
Users must obtain an RSP authentication token, which serves as a credential when making API requests.
Instructions on generating and using an RSP access token can be found on the `Authentication website <https://rsp.lsst.io/guides/auth/index.html>`_.

Additional Resources
=====================

RSP tutorials are available in the data release documentation.
For the most recent data releases, visit the `Rubin Observatory page <https://rubinobservatory.org/for-scientists/data-products/recent-data-releases>`_.
