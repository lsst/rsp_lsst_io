#########################################
Get started on the Rubin Science Platform
#########################################

:doc:`Create an account and log into the Rubin Science Platform <get-an-account>`, and start exploring Rubin data.

.. toctree::
   :caption: Account set up
   :name: getting-started-accounts
   :titlesonly:

   get-an-account

.. jinja:: rsp

   .. toctree::
      :caption: Quick start tutorials
      :name: getting-started-tutorials
      :titlesonly:

      {% if env.portal_url %}portal-first-steps{% endif %}
      {% if env.nb_url %}notebook-first-steps{% endif %}
