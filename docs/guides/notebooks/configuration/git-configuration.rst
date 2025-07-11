#################################
Configuring Git and GitHub access
#################################

`Git <https://git-scm.com>`__ is an open source change control system and `GitHub <https://github.com>`__ is a popular code hosting platform that uses Git.
Using Git with GitHub (or another hosting platform) is an excellent way to manage, share, and collaborate on the code, notebooks, and articles you create on the RSP Notebook Aspect.
Like any other computer, you need to configure Git before you can begin developing software and collaborating on GitHub.
This page will get you started.

.. tip::

   New to Git and GitHub?
   See this `Community forum topic for learning resources <https://community.lsst.org/t/resources-for-github/6153>`__.

Setting up Git
==============

At a minimum, configure your name and email.
Open a `terminal`_ and run:

.. code-block:: bash

   git config --global user.name "Your Name"
   git config --global user.email "your.email@example.com"

You can configure many more aspects of Git.
The `Rubin Developer Guide has some ideas <https://developer.lsst.io/git/setup.html>`__ to get you started.
If you’ve already customized a :file:`~/.gitconfig` file on your local computer, you might want to copy that over to the :file:`~/.gitconfig` on the Notebook Aspect.

Storing GitHub credentials
==========================

You can cache your GitHub credentials in the Notebook Aspect so that you don’t have to type in your password each time you ``git push`` or work with a private repository.
The `gh auth login <https://cli.github.com/manual/gh_auth_login>`__ command from GitHub's CLI is the recommended way to authenticate with GitHub.

First, `open a terminal <https://jupyterlab.readthedocs.io/en/latest/user/terminal.html>`__ and run:

.. code-block:: bash

   gh auth login

The first time you run this command, you'll be asked to set your authentication preferences.
The default answers are best for more users:

- *Where do you use GitHub?* Select ``GitHub.com``.
- *What is your preferred protocol for Git operations on this host?* Select ``HTTPS``.
- *Authenticate Git with your GitHub credentials?* Select ``Yes``.
- *How would you like to authenticate GitHub CLI?* Select ``Login with a web browser``.

  You will need to open the provided URL ``github.com`` in a new browser tab and enter the one-time code shown in the terminal.

With this setup complete, you can now use Git with GitHub repositories without needing to enter your username and password each time.

Clearing stored GitHub credentials
----------------------------------

The ``gh auth login`` command stores your GitHub credentials on the Rubin Science Platform.
You may wish to clear these credentials after you're done using the Notebook Aspect.
To do so, open a `terminal`_ and run:

.. code-block:: bash

   gh auth logout

Store credentials for other Git hosts
=====================================

If you’re using a Git host other than GitHub, you can store your credentials in a ``~/.git-credentials`` file.
Open a `terminal`_ and run:

.. code-block:: bash

   git config --global credential.helper store

The next time Git asks for your credentials, it will store them in a ``~/.git-credentials`` file.
You can `read more about the “store” credential helper in the Git documentation <https://git-scm.com/docs/git-credential-store>`__.

Alternatively, your Git host might allow SSH key access.
See their documentation for details.

Git LFS for Rubin Observatory data repositories
===============================================

The Notebook Aspect includes the `Git LFS <https://git-lfs.com>`_ client.

Git LFS is preconfigured to allow anonymous access to Rubin Observatory’s Git LFS-backed data repositories (such as https://github.com/lsst/afwdata).

.. jinja:: rsp

   {% if not env.is_primary %}
   Members of the `lsst organization <https://github.com/lsst>`_ on GitHub can set up authenticated Git LFS access to push to LSST’s Git LFS repositories.
   See the `Developer Guide <https://developer.lsst.io/git/git-lfs.html#authenticating-for-push-access>`__ for details.
   {% endif %}

.. _`terminal`: https://jupyterlab.readthedocs.io/en/latest/user/terminal.html
