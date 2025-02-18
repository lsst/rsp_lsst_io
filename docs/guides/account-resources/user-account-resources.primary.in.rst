It is a requirement defined by the `Science Requirements Document <https://docushare.lsst.org/docushare/dsweb/Get/LPM-17>`_ that the "Data Management System will also provide at least 10% of its total capability for user-dedicated processing and user-dedicated storage" (Section 3.5).

This page quantifies the individual and shared resources that every account at the US Data Access Center (US DAC) has access to, by default, via the Rubin Science Platform at |rsp-url|.

   .. important::
      The US DAC, the Rubin Science Platform, and this documentation are currently under construction.
      The estimates quoted below include current, planned, and to-be-determined (TBD) values, all of which are subject to change as hardware, software, and user habits evolve.

**Page last updated:** Tue Feb 18 2025


Number of users
===============

Design specification: 10000 individual user accounts.

Number of simultaneous users above which service may degrade:

 * Notebook Aspect (JupyterLab servers): 517 :sup:`a`
 * Portal Aspect sessions: TBD
 * API connections: TBD

Maximum number of simultaneous users (hard limit):

 * Notebook Aspect (JupyterLab servers): TBD
 * Portal Aspect sessions: TBD
 * API connections: TBD

Maximum number of services accessed simultaneously per user:

 * Notebook Aspect (JupyterLab servers): 1 :sup:`b`
 * Portal Aspect sessions: 1 :sup:`b`
 * API connections: TBD

Notebook sessions will be automatically shut-down after 5 days of inactivity, or after 25 days.

:sup:`a` This is the number of science platform cores for users, from row one of Table 37 in the `DM Sizing Model <https://dmtn-135.lsst.io/>`_.
Note that the RSP was designed to include 517 cores for users, and to expand to accommodate more simultaneous users.
Table 43 shows this increasing to 4664 by LSST year 10.

:sup:`b` But, users can have multiple browser tabs open to the same session.

Computational processing
========================

Computational resources are available via the Notebook Aspect (JupyterLab).

Notebook server options:

 * Small (1.0 CPU, 4G B RAM)
 * Medium (2.0 CPU, 8 GB RAM)
 * Large (4.0 CPU, 16 GB RAM)

Only CPUs (central processing units) are available.
No GPU (graphical processing units) are available and there is no plan to add them.

Cores per science user: 0.1 :sup:`c`

:sup:`c` The number of cores per science user is from Table 37 in the `DM Sizing Model <https://dmtn-135.lsst.io/>`_.
Table 43 shows this increasing to 0.6 by LSST year 10. It is :math:`<1` because it includes oversubscription and assumes not all users are simultaneously connected.

Batch processing
----------------

This refers to parallel processing (asynchronous) job submission.
The user batch facility is focused on supporting a large variety of smaller needs for the broader community (`DMTN-202 <https://dmtn-202.lsst.io/>`_).
User batch processing will be available by Data Release 1 (DR1).
Access to user batch processing will be allocated by the Resource Allocation Committee.

Number of core hours total per year: 4.53E+06 :sup:`d`
Number of core hours per user available via RAC: TBD; to be set by DR1

:sup:`d` This preliminary estimate is 10% of the total number of core-hours needed for Data Release Processing as quoted in Table 27, Section 6.1 of the `DM Sizing Model <https://dmtn-135.lsst.io/>`_, and is number is subject to change.

Storage
=======

During the Early Science era (the Data Previews and Data Release 1), the total amount of shared user space across all user directories (home, project, and scratch) is 24 TB.

During the Operations era, the anticipated amount of individual home directory disk space (in the cloud) is 0.4 TB :sup:`e`.

The total shared disk space for batch users approved by the RAC remains TBD.

:sup:`e` This preliminary estimate comes from the "Storage per science user" row of Table 31, Section 7.2 of the `DM Sizing Model <https://dmtn-135.lsst.io/>`_.
Table 39 shows this increasing to 1.3 TB by LSST year 10.

Backups
-------

Users are encouraged to use services such as GitHub for software version control and to take care not to accidentally delete files from their home directory.

While there is no guarantee that accidentally deleted data can be recovered, users are encouraged to use the resources for :doc:`/docs/support/index` immediately if mistakes do happen.

