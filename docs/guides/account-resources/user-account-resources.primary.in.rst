It is a requirement defined by the `Science Requirements Document <https://docushare.lsst.org/docushare/dsweb/Get/LPM-17>`_ that the "Data Management System will also provide at least 10% of its total capability for user-dedicated processing and user-dedicated storage" (Section 3.5).

This page quantifies the individual and shared resources that every account at the US Data Access Center (US DAC) has access to, by default, via the Rubin Science Platform at |rsp-url|.

   .. important::
      This page is under construction and includes current, planned, and to-be-determined (TBD) values, all of which are subject to change as hardware, software, and user habits evolve.

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
 * Small (1.0 CPU, 4Gi RAM)
 * Medium (2.0 CPU, 8Gi RAM)
 * Large (4.0 CPU, 16Gi RAM)

Only CPUs (central processing units) are available.
No GPU (graphical processing units) are available and there is no plan to add them.

Cores per science user: 0.1 :sup:`c`

:sup:`c` The number of cores per science user is from Table 37 in the `DM Sizing Model <https://dmtn-135.lsst.io/>`_.
Table 43 shows this increasing to 0.6 by LSST year 10. It is :math:`<1` because it includes oversubscription and assumes not all users are simultaneously connected.
