###############
Notebook aspect
###############

The Notebook aspect enables scientific analysis in a web browser by running Jupyter Notebooks and shell scripts.
The Notebook aspect is powered by JupyterLab_.

Most RSP users will find Jupyter Notebooks to be the most efficient and powerful way to interact with the LSST data sets.

**Always save and shutdown all notebooks and log out of JupyterLab when done with a work session.**
This is important to preserve resources for other users and to ensure re-entry to the RSP in a known state every time.
To help users avoid issues with stale instances, sessions will be automatically shut-down after 5 days of inactivity, or after 25 days.


.. _NB-Conceptual-Overview:

Conceptual overview
-------------------

The Notebook aspect offers a variety of functionality, including:

* programmatic access and analysis of LSST data
* :doc:`Jupyter Notebooks <jupyter-notebooks/index>`
* :doc:`terminal <jupyterlab-terminal/index>` and iPython interface
* stable, Python-based software environment
* pre-installed `LSST Science Pipelines`_
* shared computational resources and disk space


.. _NB-User-Guide:

User guide
----------

.. toctree::
   :maxdepth: 2
   :titlesonly:

   starting-and-stopping/index
   jupyter-notebooks/index
   jupyterlab-terminal/index
   Using the Science Pipelines <science-pipelines/index>
   configuration/index
   faq/index


Questions? :doc:`Get support </docs/support/index>`.
