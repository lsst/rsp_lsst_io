##################################
times-square.yaml schema reference
##################################

The :file:`times-square.yaml` file is a YAML file that configures a GitHub repository for use with Times Square.
Any repository that publishes notebooks to Times Square needs this file in its root directory.

This page describes the schema of the :file:`times-square.yaml` file.

Example
=======

Here is an example of a :file:`times-square.yaml` file:

.. code-block:: yaml
   :caption: times-square.yaml

   enabled: true
   description: >
     A sentence or two describing what kinds of notebooks
     this repository provides.

Schema
======

description
-----------

(*string*, optional) A sentence or two describing what kinds of notebooks this repository provides.

enabled
-------

(*boolean*, optional) A flag indicating whether a repository is enabled for Times Square.
Even if a GitHub App is installed in the repository, you can set this flag to ``false`` to remove the repository and its notebooks from Times Square.
Default is ``true``.

ignore
------

(*array of strings*, optional) A list of file paths or patterns to ignore when scanning the repository for notebooks. You can use globs (``*``) to match multiple files (see Python's `pathlib.PurePath.match` documentation for syntax).

root
----

(*string*, optional) The root directory of the repository where notebooks are found.
The default is an empty string, which is the root of the Git repository.

This setting is useful for publishing notebooks in situ from projects like a Python package.
