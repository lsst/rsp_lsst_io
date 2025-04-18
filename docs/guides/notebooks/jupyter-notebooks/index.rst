#######################
Using Jupyter Notebooks
#######################

The JupyterLab Notebooks `documentation <https://jupyterlab.readthedocs.io/en/latest/user/notebook.html>`_ has more information on creating and using notebooks.

.. toctree::
   :titlesonly:
   :maxdepth: 2
   :caption: How-to guides

   tutorial-notebooks


Executing cells
---------------

Jupyter notebooks provide "cells" within which is typed either Python code or markdown language (for formatted text).

Choose the cell to execute by clicking in it with the mouse (the cursor must be in the desired cell).
To execute the cell, hold down the *shift* key and press either *enter* or *return* (depending on keyboard type), or click the 'Play' button in the notebook toolbar.

If the cell type is code, and the cell contains python code, the code will be executed.
If the cell type is markdown, then it will be rendered upon execution to yield nicely formatted text.

  .. figure:: images/notebook.png
      :name: notebook_aspect
      :alt: This image is a screenshot of a Rubin tutorial notebook. The notebook has been scrolled down to Section 3.3, which contains both markdown text and code cells which have been executed. The last code cell has produced a grayscale sky image.

      A screenshot from an executed Rubin/LSST tutorial notebook. Multiple notebooks can be opened in separate tabs. You can monitor memory usage by checking the numbers listed after "Mem:" along the bottom gray bar of the RSP window.


See also the `user guide for markdown cells in the Jupyter Notebooks documentation <https://jupyter-notebook.readthedocs.io/en/stable/examples/Notebook/Working%20With%20Markdown%20Cells.html>`_.

See :ref:`these instructions <lsst-kernel-create>` to create a new notebook with the LSST kernel.

**Take care to execute notebook cells in order.**
Jupyter notebook cells *can* be executed out of order.
This provides a degree of flexibility in executing Jupyter notebooks, but could also lead to errors if, for instance, a cell is executed before prior cells that define necessary functions and/or variables.
If you've executed a notebook's cells out of order and are concerned about having caused potential issues in doing so, you can restart the notebook's kernel.


What is a kernel?
-----------------

The kernel is the process that interprets and executes the code in a notebook, and holds its data in memory, all within a defined software environment.
In the RSP Notebook aspect, notebooks use a kernel that has access to the full LSST Science Pipelines, including the Butler (see :ref:`NB-Intro-Use-A-NB-faq-butler`).
Many standard Python libraries and modules will be available, and users can `install <https://nb.lsst.io/environment/python.html>`_ additional Python tools they wish to use.
See also `this tutorial on installing python packages <https://packaging.python.org/en/latest/tutorials/installing-packages/>`_
(which includes, e.g., use of "pip install").
To view a list of packages available, type "pip list" in a terminal.

**Restarting the kernel:**
To completely refresh a notebook, in the main menu bar select "Kernel" and then "Restart kernel and clear all outputs".


Opening multiple notebooks
--------------------------

Multiple notebooks and terminals can be open at a time in the main work area.
Notebooks and/or terminal windows can be arranged next to or on top of each other by dragging the notebook or terminal around by the top bar.
Arranging the windows can be convenient when working in both a terminal and notebook at the same time, or when using another notebook as a reference.


Autosave
--------

JupyterLab autosaves notebooks at a default interval of 2 minutes.
