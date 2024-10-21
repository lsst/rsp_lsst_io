#################################################################
Developing LSST Science Pipelines packages in the Notebook Aspect
#################################################################

The Notebook Aspect combines all the facilities you need to develop for, or alongside, the `LSST Science Pipelines`_:

-  A base ``lsst_distrib`` installation
-  Butler repositories
-  Compilers and other developer tools
-  Jupyter notebooks and console
-  A fully-featured bash shell

This tutorial shows you a workflow for developing LSST Science Pipelines packages in the Notebook Aspect.

.. seealso::

   For a more comprehensive look at the code development workflow for the LSST Science Pipelines, see the `LSST DM Developer Guide <https://developer.lsst.io/work/flow.html>`__.
   This tutorial only covers procedures particular to working in the Notebook Aspect.

.. _eups-prereqs:

Prerequisites
=============

Log in with a current daily image
---------------------------------

When you're developing an LSST Science Pipelines package, you're generally working from a branch based on the package's ``main`` branch.
To ensure that your package can be compiled and used with other LSST Science Pipelines packages, you need to select a recent daily build of the LSST Science Pipelines when you log into the Notebook Aspect.

If you aren't sure you are running the most recent daily, save your work and exit from the current session.
Then log back in with the most recent daily build.

Set up Git
----------

Before you get started with any development, be sure to :doc:`configure Git and set up your GitHub credentials <../configuration/git-configuration>` (particularly if you will be pushing code).

.. _eups-tutorial-setup:

Step 1: open a terminal and set up lsst_distrib
===============================================

First open a `terminal`_.
From the file browser click the **+** button to open the launcher (or type :kbd:`command`\ -\ :kbd:`shift`\ -\ :kbd:`L`).
Then click on the **Terminal** icon.

Follow the onscreen instructions to activate the LSST environment:

.. code-block:: bash

   setup lsst_distrib

.. _eups-tutorial-clone:

Step 2: clone an existing package
=================================

In this tutorial, you’ll add a new Task to LSST’s `pipe_tasks <https://github.com/lsst/pipe_tasks>`__ package.
First, you need to clone it from GitHub.
In the same terminal, run:

.. code-block:: bash

   git clone https://github.com/lsst/pipe_tasks
   cd pipe_tasks

.. _eups-tutorial-setup-package:

Step 3: set up the package
==========================

Next, you need to set up this cloned version of ``pipe_tasks``, replacing the version built into the Notebook Aspect’s image.
In the same terminal, run:

.. code-block:: bash

   setup -k -r .

You can see that the ``pipe_tasks`` package that’s set up is your local copy:

.. code-block:: bash

   eups list pipe_tasks

The other packages from ``lsst_distrib`` are still set up:

.. code-block:: bash

   eups list -s

.. _eups-tutorial-build:

Step 4: build the package
=========================

All LSST Science Pipelines packages, even pure-Python packages like ``pipe_tasks``, need to be built before they can be imported and used.
In the same terminal, run:

.. code-block:: bash

   scons

.. _eups-tutorial-notebook-setup:

Step 5: set up the package for notebooks
========================================

In Step 3 you set up the cloned ``pipe_tasks`` package for that specific terminal session. This change isn’t carried over to notebooks.
Instead, you need to add this ``setup`` command to the :ref:`~/notebooks/.user_setups <lsst-kernel-user-setups>` file.

In a terminal text editor like Vim or Emacs, create or open ``~/notebooks/.user_setups`` and edit the file to be:

.. code-block:: bash

   setup -k -r ~/pipe_tasks

You can check that this works by :ref:`opening a new notebook with the LSST kernel <lsst-kernel-create>` and running:

.. code-block:: python

   import lsst.pipe.tasks

   print(lsst.pipe.tasks.__file__)

As you can see, the module’s path is your clone in :file:`~/pipe_tasks/`, rather than the preinstalled package in :file:`/opt/lsst/software/stack`.

.. _eups-tutorial-code:

Step 6: write some code
=======================

There’s a lot that can be done in this step, but as a demonstration we’ll create a simple Task called ``MyTask``.

First, create a Git branch from the terminal:

.. code-block:: bash

   git checkout -b my-task

Second, create a new file for Task at :file:`python/lsst/pipe/tasks/myTask.py` (inside :file:`~/pipe_tasks`) and paste these contents into it:

.. code-block:: python

   __all__ = ("MyTask",)

   from lsst.pipe.base import Task
   from lsst.pex.config import Config


   class MyTask(Task):

       _DefaultName = "MyTask"
       ConfigClass = Config

       def run(self):
           print("Running MyTask")

.. _eups-tutorial-run:

Step 7: run the new code in a notebook
======================================

Go back to the notebook and reload the kernel.
Then run the task:

.. code-block:: python

   from lsst.pipe.tasks.myTask import MyTask

   myTask = MyTask()
   myTask.run()

.. tip::

   Instead of restarting the notebook’s kernel, you can sometimes reload a module that you’ve previously imported.
   See the Python documentation for `importlib.reload`, including caveats for when this function will not work.

.. tip::

   It is sometimes useful to open the notebook as a classic notebook with the same kernel as is running in the JupyterLab environment.
   To do this, select **Help → Launch Classic Notebook** from the menu at the top of the JupyterLab page.
   This can be especially helpful if you are trying to debug with `pdb` since `pdb` behaves better in classic notebooks than it currently does in JupyterLab.

.. _eups-tutorial-cleanup:

Step 8: cleaning up
===================

At this point, you will typically use Git to commit this work and push your new branch to GitHub.

After your work is done, you will want to revert the ``~/notebooks/.user_setups`` file so that notebooks use the LSST Science Pipelines packages built into the Notebook Aspect image, instead of your local clone. Delete any lines with ``setup`` commands you no longer need.

.. _eups-tutorial-summary:

Summary
=======

Keep these steps in mind while developing LSST Science Pipelines software in the Notebook Aspect:

-  **In terminals:**

   1. ``setup lsst_distrib``.
   2. Clone the package you're developing.
   3. Set up the specific package you’re developing with ``setup -k -r {{path}}``.
   4. Build the package by running ``scons``.

-  **For notebooks,** add a ``setup -k -r {{path}}`` command for your package to ``~/notebooks/.user_setups``.

.. _`LSST Science Pipelines`: https://pipelines.lsst.io
.. _terminal: https://jupyterlab.readthedocs.io/en/latest/user/terminal.html
