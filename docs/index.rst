:html_theme.sidebar_secondary.remove:

####################################
Rubin Science Platform Documentation
####################################

The Rubin Science Platform is an online service that enables you to access and analyze Rubin LSST data.
This documentation will help you set up your user account and work with the Rubin Science Platform's software and services.

For the current status of RSP capabilities and future plans see <roadmap.rst>

.. jinja:: rsp

   {% if not env.is_primary %}
   .. important::

      This documentation covers the |rsp-at|, an environment for Rubin Observatory staff.
      For :abbr:`DP0 (Data Preview 0)`\ , please use the `documentation for the {{all_envs.primary.title_full}} <{{all_envs.primary.ltd_url_prefix}}>`__\ .
   {% endif %}

.. toctree::
   :hidden:

   Guides <guides/index>
   Support <support/index>
   Contributing <contributing/index>

.. grid:: 3

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

Related documentation
=====================

- `Data Preview 0.2`_ — Learn about the DESC DC2 simulated dataset and get tutorials for analyzing data with the Rubin Science Platform.
- `LSST Science Pipelines`_ — Learn about the Rubin LSST's Python data processing, measurement, and access software, which you can use from the Rubin Science Platform.
