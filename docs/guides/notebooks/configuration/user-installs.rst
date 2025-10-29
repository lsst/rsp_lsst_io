####################################
Install packages in user environment
####################################

Basic User Installs
~~~~~~~~~~~~~~~~~~~

The Rubin Science Platform (RSP) comes with the ``rubin-env`` conda environment, including the LSST Science Pipelines, pre-installed and activated within the Notebook and Terminal.
If it is necessary to extend the ``rubin-env`` environment by installing other Python packages, use the ``pip install`` command.
In the RSP, ``pip`` actually invokes ``conda`` to do its work, ensuring that dependencies that are already present in ``rubin-env`` are used (if compatible).
Packages installed with ``pip`` will be placed in a subdirectory of the home directory.
These packages are only guaranteed to work when the conda environment in which they are installed is activated.

If it's necessary to install other conda packages but don't need to use them at the same time as the ``rubin-env`` and LSST Science Pipelines packages, install them into a new conda environment.
Start by doing ``source /opt/lsst/software/stack/loadLSST.bash`` to initialize conda.
Use the ``conda create -n myenv`` command to create the new environment.
Use the ``conda activate myenv`` command to activate this environment.
Use the ``mamba install {package} ...`` command to install one or more packages into the environment.
(``mamba`` is a faster version of conda for installing packages.)
If the package to be installed is not available from the current channels, then the channel will have to be specified, e.g., ``mamba install -c {channel} {package}``.
When done using the environment and want to revert to the ``rubin-env`` one, use ``conda deactivate``.

If it's necessary to directly extend the ``rubin-env`` environment with other conda packages, the only way to do so at present is to clone the environment.
This is a time- and space-consuming process, so we do not recommend it.

More Complex User Installs
~~~~~~~~~~~~~~~~~~~~~~~~~~

Suppose one wishes to install a user package on the RSP that has dependencies on non-python libraries.
Typically, these non-python libraries must be installed and built separately, and the ``LD_LIBRARY_PATH`` must be updated.

The following example demonstrates the installation of the ``bagpipes`` Bayesian Analysis of Galaxies package, which depends on ``PyMultiNest`` (a python interface to the ``MultiNest`` package written in C++), so that ``bagpipes`` can be used both from the python command line shell and from inside a notebook.

The basic steps are:

1. Open a terminal in the Notebook aspect of the RSP.

2. Install the bagpipes package with :command:`pip`:

   .. code-block:: bash

      pip install --user bagpipes

   (The ``--user`` flag is necessary due to lack of root access.)

   Among other packages, the above command installs ``PyMultiNest``, a python interface for MultiNest. The ``MultiNest`` package itself is not included.
   Before we can use the ``bagpipes`` package, we must install MultiNest and update the ``LD_LIBRARY`` environment variable.

3. Install and build the dependencies -- in this case, the ``MultiNest`` package -- in the ``~/local`` directory.  In a terminal, execute:

   .. code-block:: bash

	cd ~/local
	git clone https://github.com/JohannesBuchner/MultiNest
	cd MultiNest/build
	cmake ..
	make

4. Update the ``LD_LIBRARY_PATH` in ``~/.bashrc`` file (for terminal-based access):

   .. code-block:: bash

	export LD_LIBRARY_PATH=${LD_LIBRARY_PATH}:${HOME}/local/MultiNest/lib

5. Update the ``LD_LIBRARY_PATH` in ``~/notebooks/.user_setups`` file (for notebook access):

   .. code-block:: bash

	export LD_LIBRARY_PATH=${LD_LIBRARY_PATH}:${HOME}/local/MultiNest/lib

6. After the first time perfoming Steps 4 and/or 5, log out and log back into the RSP.
