############
Getting help
############

.. jinja:: rsp

   {% if env.is_primary %}

   Technical and scientific support
   ================================

   Get support at any time via the `Rubin Community Forum <https://community.lsst.org/>`_.

   To ask a question about any aspect of the RSP or the LSST data products, services, and tools,
   `create a new topic <https://community.lsst.org/t/how-to-ask-a-question-in-the-forum/8198>`_
   in the `Support category <https://community.lsst.org/c/support/6>`_ of the Community Forum.
   Rubin staff monitor the Support category and will respond there.
   Beginner-level, "naive" questions, and students are all very much encouraged.

   For the rare cases where it might be necessary,
   `confidential support <https://community.lsst.org/t/how-to-ask-a-question-confidentially/8200>`_ is also available.

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
   For a list of recent data releases and their associated documentation, visit `rubinobservatory.org <https://rubinobservatory.org/for-scientists>`_.
   {% endif %}

You can also search the `Rubin Documentation Portal <https://www.lsst.io/>`__ for more technical information.
