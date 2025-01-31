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

Conceptual overview
-------------------

The RSP Notebook Aspect offers a variety of functionality, including:

* :doc:`Jupyter Notebooks <jupyter-notebooks/index>`
* Python scripts
* access and analyze data in the cloud
* :doc:`terminal <jupyterlab-terminal/index>` and iPython interface
* stable software environment
* pre-installed `LSST Science Pipelines`_
* shared disk space

The pages within this guide, listed below, illustrate how to do RSP Notebook Aspect activities, from logging in, to using Jupyter Notebooks, to learning from Rubin/LSST tutorial notebooks, to accessing `LSST Science Pipelines`_ software, and logging out.

This guide focuses on the basic instructions for using the RSP Notebook Aspect, and a few frequently asked questions (FAQs) and troubleshooting tips.
The full documentation for the RSP Notebook Aspect is available at `nb.lsst.io <https://nb.lsst.io/>`_.

User support
------------

Get support at any time via the `Rubin Observatory Community Forum <https://community.lsst.org/>`_ or via GitHub Issues.
Another option is to attend the Rubin Science Assemblies which will feature live tutorials and question-and-answer time with Rubin Observatory staff.

Beginner-level questions are very welcome, both in the Community Forum and during the Rubin Science Assemblies.
To encourage questions in the Forum, a couple of beginner-level topics have been started to share resources for
learning `python <https://community.lsst.org/t/resources-for-python-beginners/5975>`_ and `SQL <https://community.lsst.org/t/sql-adql-beginner-resources/6051>`_.
People new to the Rubin Community Forum might appreciate `this video demonstrating how to navigate and post topics to the forum <https://www.youtube.com/watch?v=d_Z5xmkR4P4&list=PLPINAcUH0dXZSx2aY6wTIjLCWiexs3dZR&index=10>`_.

User guide
------------

.. toctree::
   :maxdepth: 2
   :titlesonly:

   starting-and-stopping/index
   jupyter-notebooks/index
   jupyterlab-terminal/index
   Using the Science Pipelines <science-pipelines/index>
   configuration/index
   faq/index
