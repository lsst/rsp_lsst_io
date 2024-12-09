#######################################
Introduction to the RSP Notebook Aspect
#######################################

The Notebook aspect enables scientific analysis in a web browser by running Jupyter Notebooks and shell scripts.
The Notebook aspect is powered by JupyterLab_.

Most RSP users will find Jupyter Notebooks to be the most efficient and powerful way to interact with the LSST data sets.

**Always save and shutdown all notebooks and log out of JupyterLab when done with a work session.**
This is important to preserve resources for other users and to ensure re-entry to the RSP in a known state every time.
To help users avoid issues with stale instances, sessions will be automatically shut-down after 5 days of inactivity, or after 25 days.

.. _NB-Conceptual-Overview:

RSP Notebook Aspect conceptual overview
---------------------------------------

The RSP Notebook Aspect offers a variety of functionality, including but not limited to :doc:`Jupyter Notebooks <jupyter-notebooks/index>`.

* The RSP Notebook Aspect is intended to function as a cloud server for analyzing and processing Rubin/LSST data (beyond issuing Portal queries, which can be done in the RSP :doc:`Portal Aspect <../portal/index>`) and without needing to download the Rubin/LSST data to any local machine.
* In addition to Jupyter Notebooks, the RSP Notebook Aspect offers powerful access to the Rubin/LSST software stack and the :doc:`JupyterLab terminal <jupyterlab-terminal/index>`, where one can issue shell commands to organize, analyze, and reprocess data.

The pages within this guide, listed below, illustrate how to do RSP Notebook Aspect activities, from logging in, to using Jupyter Notebooks, to learning from Rubin/LSST tutorial notebooks, to accessing `LSST Science Pipelines`_ software, and logging out.


This guide focuses on the basic instructions for using the RSP Notebook Aspect, and a few frequently asked questions (FAQs) and troubleshooting tips.
The full documentation for the RSP Notebook Aspect is available at `nb.lsst.io <https://nb.lsst.io/>`_.

.. toctree::
   :maxdepth: 2
   :titlesonly:

   starting-and-stopping/index
   jupyter-notebooks/index
   jupyterlab-terminal/index
   Using the Science Pipelines <science-pipelines/index>
   configuration/index
   faq/index
