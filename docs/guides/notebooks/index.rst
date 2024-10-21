#######################################
Introduction to the RSP Notebook Aspect
#######################################

The Notebook aspect enables you to do scientific analysis in your web browser by running Jupyter Notebooks and shell scripts.
The Notebook aspect is powered by JupyterLab_.

Most RSP users will find Jupyter Notebooks to be the most efficient and powerful way to interact with the LSST data sets.

**Always save and shutdown all notebooks and log out of JupyterLab when you are done with your day's work.**
This is important to preserve resources for other users and to ensure you re-enter the RSP in a known state every time.
To help users avoid issues with stale instances, sessions will be automatically shut-down after 5 days of inactivity, or after 25 days.

This page focuses on the basic instructions for using the RSP Notebook Aspect, and a few FAQs and Troubleshooting Tips.
The full documentation for the RSP Notebook Aspect is available at `nb.lsst.io <https://nb.lsst.io/>`_.

.. _NB-Conceptual-Overview:

RSP Notebook Aspect Conceptual Overview
---------------------------------------

The RSP Notebook Aspect offers a variety of functionality, including but not limited to Jupyter notebooks.
The RSP Notebook Aspect is intended to function as your cloud server for analyzing and processing Rubin/LSST data (beyond issuing Portal queries, which can be done in the RSP Portal Aspect) and without needing to download the Rubin/LSST data to any local machine.
In addition to Jupyter notebooks, the RSP Notebook Aspect offers powerful access to the Rubin/LSST software stack and the JupyterLab terminal, where one can issue shell commands to organize, analyze, and reprocess data.
The pages within this guide, listed below, will walk illustrate how to do RSP Notebook Aspect activities, from logging in, to using Jupyter Notebooks, to learning from Rubin/LSST tutorial notebooks, to accessing `LSST Science Pipelines`_ software, and logging out.

.. toctree::
   :maxdepth: 2
   :titlesonly:

   starting-and-stopping/index
   Using the Science Pipelines <science-pipelines/index>
   configuration/index
   jupyter-notebooks/index
   tutorial-notebooks/index
   jupyterlab-terminal/index
   faq/index
