This page quantifies the individual and shared resources that every account at the US Data Access Center (US DAC) has access to, by default, via the Rubin Science Platform at |rsp-url|.
The Rubin Science Platform, and the values on this page, will continue to evolve through Rubin Operations.

.. important::
   The US DAC, the Rubin Science Platform, and this documentation are currently under construction.
   The estimates quoted below include current, planned, and to-be-determined (TBD) values, all of which are subject to change.
   See the Roadmap for planned changes (top menu bar).


**Page last updated:** June 4 2025


Computational processing
========================

Computational resources are available via the Notebook Aspect (JupyterLab).

Notebook server options:

- Small (1.0 CPU, 4 GB RAM)
- Medium (2.0 CPU, 8 GB RAM)
- Large (4.0 CPU, 16 GB RAM)

Only CPUs (central processing units) are available.
No GPU (graphical processing units) are available and there is no immediate plan to add them.

- Cores per science user: 0.1 [#f1]_


Batch processing
----------------

This refers to parallel processing (asynchronous) job submission.
The user batch facility is focused on supporting a large variety of smaller needs for the broader community (`DMTN-202 <https://dmtn-202.lsst.io/>`_).
User batch processing will be available by Data Release 1 (DR1).
Access to user batch processing will be allocated by the Resource Allocation Committee.

- Number of core hours total per year: 4.53E+06 [#f2]_
- Number of core hours per user available via RAC: TBD; to be set by DR1


Storage
=======

User home directory quota: 20 GB.

This limit is applied to ensure fairness in access to shared resources during Data Preview 1,
and will increase for Data Preview 2 (with further increases over the ten-year survey likely) [#f3]_.

The total shared disk space for batch users approved by the RAC remains TBD.


Scratch
-------

Shared scratch space: 20 TB.

To enable processing and analysis that requires large intermediate files, a shared "scratch" directory where all users
can write temporary files is provided.

This directory will be named ``/cleared-weekly`` and all contents will be deleted on Sundays.
Scratch space is *not backed up*.

Users should take care to use this shared resource responsibly.
Policies on scratch space size and clearance frequency may change.


Backups
-------

Users are encouraged to use services such as GitHub for software version control and to take care not to accidentally delete files from their home directory.

While there is no guarantee that accidentally deleted data can be recovered, backup mechanisms do exist to protect user data in case of system failures.


Query and memory limits
=======================

All queries are executed with shared resources.
The length of time to query completion depends firstly on query design (number of shards accessed), and secondly on number of queries across all users.
There is no limit on the number of queries a user can do in total but there are query rate limits.

The size of a dataset retrieved by a query and held in memory depends on the server size which, for the Notebook Aspect, is selected by the user.

- Number of TAP queries per user per 15 minutes: 500 [#f4]_
- Reset interval after user excession: 15 minutes [#f5]_


Portal Aspect TAP (Table Access Protocol) service:

- Maximum rows returned: 5,000,000
- Maximum table size returned: TBD

Portal Aspect ObsTAP (TAP access to images):

- Maximum rows of image metadata: 5,000,000

Notebook Aspect TAP (Table Access Protocol) service:

- Maximum rows returned: 5,000,000
- Maximum table size returned: RAM limit of the user-selected server size

Notebook Aspect Butler service:

- Maximum number of simultaneous butler queries per user: TBD (2-5)
- Maximum number of references returned: no limit
- Maximum data volume returned: RAM limit of the user-selected server size

API Aspect TAP (Table Access Protocol) service:

- Maximum rows returned: 5,000,000
- Maximum table size returned: TBD


Download and upload limits
==========================

These estimates remain largely to-be-determined (TBD) and might depend sensitively on user load.
The Data Previews will be used to quantify and optimize user experience with respect to data transfers.

The amount of data a user may download or upload, and the data transfer rates, depend also on the user's internet service provider.

The maximum size of a data table that can be downloaded is 6 GB.

Bulk download services will not be offered.


Number of users
===============

Design specification: 10000 individual user accounts.

Number of simultaneous users above which service may degrade:

- Notebook Aspect (JupyterLab servers): 3000 [#f6]_
- Portal Aspect sessions: TBD
- API connections: TBD

Maximum number of simultaneous users (hard limit):

- Notebook Aspect (JupyterLab servers): TBD
- Portal Aspect sessions: TBD
- API connections: TBD

Maximum number of services accessed simultaneously per user:

- Notebook Aspect (JupyterLab servers): 1 [#f7]_
- Portal Aspect sessions: 1 [#f7]_
- API connections: TBD [#f8]_

Notebook sessions will be automatically shut-down after 5 days of inactivity, or after 25 days.


Resource Allocation Committee (RAC)
===================================

Individuals and groups in need of more than the standard resources, and/or who require batch processing via the RSP deployed at the US DAC (data.lsst.cloud), will submit proposals to the Resource Allocation Committee (RAC).

The quantities of the resources that the RAC will allocate, and the process by which the RAC will operate, are currently under development (see `RTN-084 <https://rtn-084.lsst.io/>`_).

Independent Data Access Centers (IDACs)
=======================================

Individuals and groups in need of more than the standard or batch resources available via the US DAC, and/or who need, e.g., GPUs, specialized software, non-Rubin data sets, should consider using one of the `Independent Data Access Centers <https://www.lsst.org/scientists/in-kind-program/computing-resources>`_ (IDACs).
Some IDACs might contribute their resources for allocation by the RAC.

More information about IDACs is in development.



.. rubric:: Footnotes

.. [#f1] The number of cores per science user is from Table 37 in the `DM Sizing Model <https://dmtn-135.lsst.io/>`_. Table 43 shows this increasing to 0.6 by LSST year 10. It is :math:`<1` because it includes oversubscription and assumes not all users are simultaneously connected.
.. [#f2] This preliminary estimate is 10% of the total number of core-hours needed for Data Release Processing as quoted in Table 27, Section 6.1 of the `DM Sizing Model <https://dmtn-135.lsst.io/>`_, and is number is subject to change.
.. [#f3] A preliminary (outdated) estimate of 0.4 TB can be found in the "Storage per science user" row of Table 31, Section 7.2 of the `DM Sizing Model <https://dmtn-135.lsst.io/>`_. Table 39 shows this increasing to 1.3 TB by LSST year 10. These values are superseded by this page.
.. [#f4] A nominal quota configuration in the `RSP quotas and rate limiting document <https://sqr-073.lsst.io/>`_.
.. [#f5] Also from the `RSP quotas and rate limiting document <https://sqr-073.lsst.io/>`_.
.. [#f6] This is the number of science platform cores for users, from row one of Table 37 in the `DM Sizing Model <https://dmtn-135.lsst.io/>`_. The RSP was designed to include at least 517 cores for users and to expand to accommodate more simultaneous users. Table 43 shows this increasing to 4664 by LSST year 10.
.. [#f7] But, users can have multiple browser tabs open to the same session.
.. [#f8] To be based on rate-limit quotas (e.g., requests per amount of time).