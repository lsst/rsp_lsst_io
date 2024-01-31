####################################
Sidecar metadata YAML file reference
####################################

Every notebook in Times Square GitHub repository has an associated sidecar metadata file.
These files have the same path and name as the notebook, but with a ``.yaml`` extension.
This file describes the notebook and its parameterization.

This page explains the contents (schema) of the sidecar metadata files.
For a more general introduction to authoring notebooks for Times Square, see :doc:`authoring-howto`.

Example file
============

.. literalinclude:: example-sidecar.yaml
   :language: yaml
   :caption: Example sidecar metadata file.

YAML field reference
====================

title
-----

(*string*) This is the title of the notebook as it appears in the Times Square UI.

It should be fairly short because it is is deplayed in a narrow column.

The name can be contextual with the notebook's directory path (and repository name and even GitHub organization name).

description
-----------

(*Markdown string*, optional) This is the description of the notebook as it appears in the Times Square UI. The description can be formatted as Markdown to include links to other URLs.

authors
-------

(*array of objects*, optional) A notebook can have multiple authors. Each author is an object with the following fields:

- ``name`` (*string*) The name of the author.
- ``slack`` (*string*, optional) The Rubin Slack username of the author.
- ``email`` (*string*, optional) The email address of the author.
- ``affiliation_name`` (*string*, optional) The name of the author's affiliation.

tags
----

(*array of strings*, optional) A notebook can have multiple tags. Each tag is a string.

parameters
----------

(*mapping of objects*, optional) A notebook can have multiple parameters.
A parameter is a user-configurable value that is set in the notebook when it is executed.
For more information about parameter types, see :doc:`parameter-types`.

The name of each parameter is the Python variable name that is set in the notebook.
Thus each parameter name must be a valid Python variable name.

For example:

.. code-block:: yaml
   :caption: Valid parameter names

   parmeters:
     start_date:
       type: string
       default: 2024-02-01
     end_date:
       type: string
       default: 2024-02-29

.. code-block:: yaml
    :caption: Invalid parameter names

    parmeters:
      start date:
         type: string
         default: 2024-02-01
      end-date:
         type: string
         default: 2024-02-29

Each parameter is an object with the following fields:

- ``type`` (*string*, required) is one of:

  - ``string``
  - ``integer`` (whole number)
  - ``number`` (floating-point number)
  - ``boolean``

- ``default`` (*string*, required) is the default value of the parameter.

- ``description`` (*Markdown string*) is the description of the parameter as it appears in the Times Square UI.

- ``minimum`` (*integer* or *number*, optional) is the minimum value of the parameter, for numeric parameters.

- ``maximum`` (*integer* or *number*, optional) is the maximum value of the parameter, for numeric parameters.

For more information about parameters, see :doc:`parameter-types`.
