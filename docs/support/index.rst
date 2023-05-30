############
Getting help
############

.. jinja:: rsp

   {% if env.is_primary %}
   Data Preview 0 science questions
   ================================

   For questions about the Data Preview dataset (DESC DC2) and analyzing those data (such as with the LSST Science Pipelines), `create a new topic in the Data Preview 0 Support category of the Community forum <https://community.lsst.org/c/support/dp0/49>`__.

   Rubin Science Platform technical support and feature requests
   =============================================================

   For technical issues or feature requests related to the Rubin Science Platform itself (the Portal, Notebooks, and API services such as TAP) `create a GitHub issue in the rubin-dp0/Support repository <https://github.com/rubin-dp0/Support/issues/new/choose>`__.
   {% else %}

   Slack
   =====

   Rubin staff using the |rsp-at| can suggest features and debug issues in real-time in the `#dm-rsp-support <https://lsstc.slack.com/archives/CAS7Y9ADS>`__ Slack channel.
   {% endif %}

Related documentation
=====================

This documentation site covers the |rsp-at|.

Other documentation sites cover related projects:

- `LSST Science Pipelines`_
- `JupyterLab`_, from the Jupyter Project, covers the Notebook Aspect's interface features.

.. jinja:: rsp

   {% if env.is_primary %}
   Learn more about the Data Preview datasets and learning programs from the `DP0.2 Guide`_.
   {% endif %}

You can also search the `Rubin Documentation Portal <https://www.lsst.io/>`__ for more technical information.
