####################################
Rubin Science Platform Documentation
####################################

Learn how to do science on the |rsp-at|.

.. jinja:: rsp

   {% if not env.is_primary %}
   .. important::

      This documentation covers the |rsp-at|, an environment for Rubin Observatory staff.
      For :abbr:`DP0 (Data Preview 0)`\ , please use the `documentation for the {{all_envs.primary.title_full}} <{{all_envs.primary.ltd_url_prefix}}>`__\ .
   {% endif %}

.. toctree::
   :hidden:

   Guides <guides/index>

.. grid:: 2

   .. grid-item-card:: New to the Science Platform?
      :link: guides/getting-started/index
      :link-type: doc

      Make your first query in the portal and launch your first notebook session.
      Learn how to request an account and log in.

   .. grid-item-card:: User guides
      :link: guides/index
      :link-type: doc

      Learn how to use the Rubin Science Platform's portal, notebook, and API services.
