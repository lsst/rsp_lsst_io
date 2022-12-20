##########################
Configuring Git for GitHub
##########################

Like any other computer, you need to configure Git before you can begin developing software and collaborating on GitHub.
This page will get you started.

Setting up Git
==============

At a minimum, configure your name and email.
Open a `terminal`_ and run:

.. code-block:: bash

   git config --global user.name "Your Name"
   git config --global user.email "your.email@example.com"

You can configure many more aspects of Git.
The `LSST DM Developer guide has some ideas <https://developer.lsst.io/git/setup.html>`_ to get you started. If you’ve already customized a ``~/.gitconfig`` file on your local computer, you might want to copy that over to the ``~/.gitconfig`` on the Notebook Aspect.

Storing GitHub credentials
==========================

You can cache your GitHub credentials in the Notebook Aspect so that you don’t have to type in your password each time you ``git push`` or work with a private repository.

`Open a terminal <https://jupyterlab.readthedocs.io/en/latest/user/terminal.html>`__ and run:

.. code-block:: bash

   git config --global credential.helper store

The next time Git asks for your credentials, it will store them in a ``~/.git-credentials`` file. You can `read more about the “store” credential helper in the Git documentation <https://git-scm.com/docs/git-credential-store>`_.

.. important::

   If you’ve enabled `two-factor authentication <https://help.github.com/articles/securing-your-account-with-two-factor-authentication-2fa/>`_ for GitHub, you need to **use a personal access token instead of your GitHub password.**

   `Follow GitHub’s documentation to create a personal access token <https://help.github.com/articles/creating-a-personal-access-token-for-the-command-line/>`_.

.. tip::

   Even if you haven’t turned on two-factor authentication, we recommend using a personal access token instead of your password as a security best-practice.
   That way you can monitor how your token is used and revoke it quickly if necessary.

Git LFS for LSST
================

The Notebook Aspect includes the `Git LFS <https://git-lfs.github.com>`_ client.

Git LFS is preconfigured to allow anonymous access to LSST’s Git LFS-backed data repositories (such as https://github.com/lsst/afwdata).
Members of the `lsst organization <https://github.com/lsst>`_ on GitHub can set up authenticated Git LFS access to push to LSST’s Git LFS repositories.
See the `LSST DM Developer Guide <https://developer.lsst.io/git/git-lfs.html#authenticating-for-push-access>`__ for details.

.. _`terminal`: https://jupyterlab.readthedocs.io/en/latest/user/terminal.html
