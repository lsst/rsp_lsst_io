:html_theme.sidebar_secondary.remove:

####################################
Rubin Science Platform Documentation
####################################

The Rubin Science Platform is an online service that enables you to access and analyze Rubin LSST data.
This documentation will help you set up your user account and work with the Rubin Science Platform's software and services.

For the current status of RSP capabilities and future plans, see :doc:`roadmap`.

.. jinja:: rsp

   {% if not env.is_primary %}
   .. important::

      This documentation covers the |rsp-at|, an environment for Rubin Observatory staff.
      For :abbr:`DP1 (Data Preview 1)`\ , please use the `documentation for the {{all_envs.primary.title_full}} <{{all_envs.primary.ltd_url_prefix}}>`__\ .
   {% endif %}

.. toctree::
   :hidden:

   Guides <guides/index>
   Support <support/index>
   Roadmap <roadmap>
   Contributing <contributing/index>
   Updates <updates/index>

.. grid:: 1 2 4 4
   :gutter: 2

   .. grid-item-card:: Sign up for an account
      :link: guides/getting-started/get-an-account
      :link-type: doc

      Learn how to request an account and log in.

   .. grid-item-card:: User guides
      :link: guides/index
      :link-type: doc

      Learn how to use the Rubin Science Platform's portal, notebook, and API services.

   .. grid-item-card:: Support
      :link: support/index
      :link-type: doc

      Get additional help with the Rubin Science Platform and related Rubin Observatory projects.

   .. grid-item-card:: Updates
      :link: updates/index
      :link-type: doc

      Find out what's new regarding the services and tools in the Rubin Science Platform.


Related documentation
=====================

- `Data Preview 1`_ — Data Preview 1 contains image and catalog products from LSST Science Pipelines v29 processing of observations obtained with the LSST Commissioning Camera of seven ~1 square degree fields over seven weeks in late 2024.
- `Data Preview 0`_ — DP0 is the first of three data previews during the period leading up to the start of Rubin Observatory Operations. DP0.2 features simulated Galactic and extragalactic data products. DP0.3 contains simulated Solar System objects.
- `LSST Science Pipelines`_ — Learn about the Rubin LSST's Python data processing, measurement, and access software, which you can use from the Rubin Science Platform.
