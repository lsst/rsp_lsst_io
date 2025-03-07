#############################
Rubin Science Platform Guides
#############################

**Learn how to use the Rubin Science Platform for exploring LSST data.**

Getting started
===============

.. toctree::
   :hidden:
   :caption: Getting Started

   getting-started/index

.. grid:: 1

   .. grid-item-card:: Getting started
      :link: getting-started/index
      :link-type: doc

      If you're new to the |rsp-at|, get your account and learn the basics with these step-by-step guides.

Accounts & authentication
=========================

.. toctree::
   :hidden:
   :caption: Accounts

   auth/index

.. grid:: 1

   .. grid-item-card:: Authentication
      :link: auth/index
      :link-type: doc

      Learn how to set up and use tokens to access the Rubin Science Platform and its services.

Aspects
=======

The Rubin Science Platform is a collection of inter-connected aspects that enable you to discover and analyze data.

.. toctree::
   :hidden:
   :caption: Aspects

   Portal <portal/index>
   Notebooks <notebooks/index>
   API <api/index>

.. grid:: 1

   .. grid-item-card:: Portal
      :link: portal/index
      :link-type: doc

      The Portal Aspect is a powerful graphical interface in your web browser for querying and visualizing Rubin catalogs and images.

   .. grid-item-card:: Notebooks
      :link: notebooks/index
      :link-type: doc

      The Notebook Aspect enables you to run Jupyter Notebooks and scripts to analyze Rubin data with your own code.

   .. grid-item-card:: API
      :link: api/index
      :link-type: doc

      The API Aspect connects you to Rubin data, from within the Rubin Science Platform and beyond. It is based on IVOA Virtual Observatory standards.


Log of major updates
====================

.. toctree::
   :hidden:
   :caption: Log

   Log <log/index>

.. grid:: 1

   .. grid-item-card:: Log of major updates
      :link: log/index
      :link-type: doc

      Find out what's new with this list of development updates for the Rubin Science Platform.


.. jinja:: rsp

   {% if env.has_apps %}
   Applications
   ============

   .. toctree::
      :hidden:
      :caption: Applications

      {% if env.times_square_url %}times-square/index{% endif %}

   .. grid:: 1

      {% if env.times_square_url %}
      .. grid-item-card:: Times Square
         :link: times-square/index
         :link-type: doc

         Times Square lets you share Jupyter Notebooks as linkable web pages.
         You can parameterize those notebooks for users to see results for different inputs.
         Times Square is great for sharing reports and analyses.
      {% endif %}
   {% endif %}
