##################
Tutorial Notebooks
##################

.. _NB-Intro-Use-Tutorial-NBs:

How to use the Tutorial Notebooks
=================================

The best way to learn how to use a Jupyter Notebook is to open the first of the Rubin/LSST tutorial notebooks which are provided in each user's home directory.

**The "notebooks/tutorial-notebooks" directory is read-only:**
The read-only "notebooks/tutorial-notebooks" directory will *always* contain the most up-to-date versions of the tutorials.
Notebooks can be edited and executed in this directory, but **changes cannot be saved to this directory**.
Users wishing to edit, execute, *and save* versions of these notebooks should copy them to a different path in their home directory.

**How to obtain an editable version of a tutorial notebook:**
The commands below demonstrate how to create a copy of a tutorial notebook in the home directory which can be opened, edited, and saved.
Step-by-step, the commands below change directory (``cd``) into the home directory (``~``),
copy the desired tutorial to the (``cp``) into the current directory (``.``),
list (``ls``) the files that are in the current directory to confirm the copy worked,
and list in long format all attributes in human-readable form (``-lah``) for the copied file.
The standard output ``-r--r--r--`` indicates that the file is read-only (``r``) by the user, the group, and everyone
with access to the file (the three ``r``).
Change the mode (``chmod``) of the file to add user write access (``u+w``), and repeate the
list command (``ls -lah``) for the file to see that the user now has read and write access (``-rw-r--r--``).

The dollar signs indicate terminal command line executable statements that should be copy-pasted into the terminal (but do not copy-paste the ``$``).
Lines without dollar signs indicate standard output to be compared with the results in the terminal.

.. code-block:: bash

      $ cd ~
      $ cp notebooks/tutorial-notebooks/<filename>.ipynb .
      $ ls <filename>*
      <filename>.ipynb
      $ ls -lah <filename>.ipynb
      -r--r--r-- 1 melissagraham melissagraham 37K Nov 13 21:14 <filename>.ipynb
      $ chmod u+w <filename>.ipynb
      $ ls -lah <filename>.ipynb
      -rw-r--r-- 1 melissagraham melissagraham 37K Nov 13 21:14 <filename>.ipynb

After executing the above statements, use the left menu bar to navigate to the home directory and open the newly altered version of the introductory notebook, make a change, and notice that it can be saved.
