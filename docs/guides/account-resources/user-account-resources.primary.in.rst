It is a requirement defined by the `Science Requirements Document <https://docushare.lsst.org/docushare/dsweb/Get/LPM-17>`_ that the "Data Management System will also provide at least 10% of its total capability for user-dedicated processing and user-dedicated storage" (Section 3.5).

This page quantifies the individual and shared resources that every account at the US Data Access Center (US DAC; data.lsst.cloud) has access to, by default.

   .. important::
      This page is under construction and includes current, planned, and to-be-determined values, all of which are subject to change as hardware, software, and user habits evolve.

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