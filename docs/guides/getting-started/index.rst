#########################################
Get started on the Rubin Science Platform
#########################################

:doc:`Create an account and log into the Rubin Science Platform <get-an-account>`, and start exploring Rubin data.

.. toctree::
   :caption: Account set up
   :name: getting-started-accounts
   :titlesonly:

   get-an-account

.. toctree::
   :caption: More about your account
   :name: linking-more-ids
   :titlesonly:

   linking-more-ids

.. jinja:: rsp

   .. toctree::
      :caption: Quick start tutorials
      :name: getting-started-tutorials
      :titlesonly:

      {% if env.portal_url %}First steps with the Portal <https://dp0-2.lsst.io/data-access-analysis-tools/portal-intro.html>{% endif %}
      {% if env.nb_url %}First steps with the Notebooks <https://dp0-2.lsst.io/data-access-analysis-tools/nb-intro.html>{% endif %}
