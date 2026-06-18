#############################
Rubin Science Platform Guides
#############################

**Learn how to use the Rubin Science Platform for LSST data analysis.**

Getting started
===============

.. toctree::
   :hidden:

   getting-started/index
   hybrid
   life/patch-thursday
   life/updates

.. grid:: 1

   .. grid-item-card:: Getting started
      :link: getting-started/index
      :link-type: doc

      Get a Rubin Science Platform account and learn the basics.

Accounts & authentication
=========================

.. toctree::
   :hidden:

   auth/index
   recovery/index
   resources/index

.. grid:: 1 2 2 2
   :gutter: 2

   .. grid-item-card:: Authentication
      :link: auth/index
      :link-type: doc

      Set up and use tokens to access the Rubin Science Platform and its services.

   .. grid-item-card:: Recovery
      :link: recovery/index
      :link-type: doc

      How to recover from lost passwords and other account access issues.

Aspects
=======

Inter-connected aspects enable you to discover and analyze data.

.. toctree::
   :hidden:

   Portal <portal/index>
   Notebooks <notebooks/index>
   API <api/index>

.. grid:: 1 2 2 2
   :gutter: 2

   .. grid-item-card:: Portal
      :link: portal/index
      :link-type: doc

      A graphical interface in your web browser for querying and visualizing catalogs and images.

   .. grid-item-card:: Notebooks
      :link: notebooks/index
      :link-type: doc

      Run Jupyter Notebooks and scripts to analyze data with your own code.

   .. grid-item-card:: API
      :link: api/index
      :link-type: doc

      Connect to data from within the Rubin Science Platform and beyond, using IVOA standards.




.. toctree::
   :hidden:

   WebDAV <webdav/index>



.. jinja:: rsp

   {% if env.has_apps %}
   Applications
   ============

   .. toctree::
      :hidden:

      {% if env.times_square_url %}times-square/index{% endif %}

   .. grid:: 1 2 2 2
      :gutter: 2

      {% if env.times_square_url %}
      .. grid-item-card:: Times Square
         :link: times-square/index
         :link-type: doc

         Times Square lets you share Jupyter Notebooks as linkable web pages.
         You can parameterize those notebooks for users to see results for different inputs.
         Times Square is great for sharing reports and analyses.
      {% endif %}
   {% endif %}
