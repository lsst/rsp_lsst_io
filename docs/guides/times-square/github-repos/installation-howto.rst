###############################################################
How to set up and install a GitHub repository into Times Square
###############################################################

In this page you will learn how to set up a new GitHub repository for hosting notebooks for Times Square.

1. Create a new repository on GitHub
====================================

First, create the new GitHub repository in an appropriate GitHub organization for your team.
Follow the `GitHub documentation <https://docs.github.com/en/get-started/quickstart/create-a-repo>`__ if you're new to the process.

.. tip::

   You don't always need to create a new repository.
   You can collect many notebooks in the same repository, and even use directories to organize them.
   You might also reuse an existing repository.
   Consider the needs of your team and how you want to collaborate.

2. Initial pull request
=======================

Once your repository is created, you'll need to create a pull request that adds the :file:`times-square.yaml` file needed by Times Square and that will make development easier.

To get set up:

1. Clone the repository to your local machine
2. Create a new branch

Next, add or modify files as described below before pushes the changes to GitHub and creating a pull request.

Add a times-square.yaml file
----------------------------

The :file:`times-square.yaml` file is required for Times Square to use a GitHub repository.
A :file:`times-square.yaml` file consists of a description and a flag indicating the repository should be enabled for Times Square:

.. code-block:: yaml
   :caption: times-square.yaml

   enabled: true
   description: >
     A sentence or two describing what kinds of notebooks
     this repository provides.

To see the full range of configurations provided by :file:`times-square.yaml`, see :doc:`times-square-yaml-schema`.

Add a .gitignore file
---------------------

Your repository might already have a :file:`.gitignore` file.
Make sure that, at a minimum, it ignores ``.ipynb_checkpoints``.

A good default :file:`.gitignore` file for a repository with notebooks is the `Python .gitignore file from GitHub <https://github.com/github/gitignore/blob/main/Python.gitignore>`__.

Add a README.md file
--------------------

Make sure that your repository includes a useful :file:`README.md` file.
You might want to link to the Times Square documentation to help your colleagues understand how to add notebooks.

Once you get going, you might also want to link to the notebooks on Times Square itself.

Push and merge the changes
--------------------------

Once you're ready, follow the usual procedure for creating commits, pushing your branch, and creating a GitHub pull request.

3. Install the Times Square GitHub App
======================================

Times Square has a corresponding GitHub App.
For Times Square to access your repository (even if its a public repository), you need to install the Times Square GitHub App into your repository.

These are the Times Square GitHub Apps for each available environment:

.. list-table::
   :header-rows: 1

   * - Environment
     - GitHub App
   * - usdf-rsp-dev.slac.stanford.edu
     - `Times Square (usdf-rsp-dev) <https://github.com/apps/times-square-usdf-rsp-dev>`__
   * - data-dev.slac.stanford.edu
     - `Times Square (data-dev.lsst.cloud) <https://github.com/apps/times-square-data-dev-lsst-cloud>`__

From the GitHub App's page, click the :guilabel:`Install` button and select the repositories you want to enable for Times Square.
For more information installing and uninstalling GitHub Apps, see `the GitHub documentation <https://docs.github.com/en/apps/using-github-apps/installing-a-github-app-from-github-marketplace-for-your-organizations>`__.

While you can install Times Square's GitHub App on a whole organization, it's best to install it on a per-repository basis.

Also be aware that the repository's needs to be on an "accept list" in Times Square's configuration.
See the ``config.githubOrgs`` configuration in Times Square's `Phalanx documentation <https://phalanx.lsst.io/applications/times-square/values.html>`__.
Send a message to ``dm-square`` on Slack to request additional organizations.

.. note::

   Each RSP environment (e.g. ``usdf-rsp.slac.stanford.edu`` versus ``usdf-rsp-dev.slac.stanford.edu``) has its own instance of the Times Square GitHub App.
   You need to install the corresponding Times Square app for each environment you want to use.

4. Add notebooks
================

With the repository set up and installed in Times Square, you can start adding notebooks.
See the :doc:`Authoring notebooks <../authoring/index>` documentation to get started.

Remember that Times Square publishes notebooks (provided they have sidecar metadata files) from any directory in the repository.
You can choose to organize your notebooks into the root of the repository, or create a folder hierarchy.
This organization is reflected in the presentation of notebooks in Times Square.

Additional configuration options
================================

- Set up pre-commit hooks
- Add branch protections
