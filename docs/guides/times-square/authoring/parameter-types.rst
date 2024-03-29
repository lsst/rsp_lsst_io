###############
Parameter types
###############

Times Square notebooks use parameters to pass inputs into the notebook.
Different types of parameters are supported, and these types inform the interface for users to enter values and the validation that's performed on those values.
This page lists the different types of parameters that are supported.
For information about the sidecar metadata file as a whole, see :doc:`sidecar-schema`.

Strings
=======

A string is the most basic parameter type that supports any kind of text.
There isn't any validation performed on the string.

.. code-block:: yaml
   :caption: Notebook YAML sidecar

   parameters:
     message:
       type: string
       description: A message to display.
       default: "Hello world"

.. code-block:: python
   :caption: Notebook parameters cell

   message = "Hello world"

Dates and times
===============

Times Square does not yet provide special support for dates and times.
In the meantime you can use a string parameter and provide validation in the notebook's code.

Example with a date
-------------------

.. code-block:: yaml
   :caption: Notebook YAML sidecar

   parameters:
     date:
       type: string
       description: An ISO8601 date
       default: "2024-01-01"

.. code-block:: python
   :caption: Notebook parameters cell

   date = "2024-01-01"

.. code-block:: python
   :caption: Notebook code

   from datetime import datetime

   try:
       dt = datetime.strptime(date, "%Y-%m-%d")
   except ValueError:
       raise ValueError("Invalid date format. Expected YYYY-MM-DD")

Examples with a date and time
-----------------------------

.. code-block:: yaml
   :caption: Notebook YAML sidecar

   parameters:
     date:
       type: string
       description: An ISO8601 date and time
       default: "2024-01-01T12:00:00+00:00"

.. code-block:: python
   :caption: Notebook parameters cell

   date = "2024-01-01T12:00:00+00:00"

.. code-block:: python
   :caption: Notebook code

   from datetime import datetime

   try:
       dt = datetime.strptime(date, "%Y-%m-%dT%H:%M:%S%z")
   except ValueError:
       raise ValueError("Invalid date format. Expected YYYY-MM-DDTHH:MM:SS+HH:MM")

Integers
========

For decimal numbers, use the ``integer`` type.
In your code, cast the value to a Python integer for use in calculations:

.. code-block:: yaml
   :caption: Notebook YAML sidecar

   parameters:
     number:
       type: integer
       description: An integer
       default: 42

.. code-block:: python
   :caption: Notebook parameters cell

   number = "42"

.. code-block:: python
   :caption: Notebook code

   number = int(number)

Validation constraints
----------------------

The ``integer`` type supports validation constraints.
You can specify minimum values and maximum values (both or either):

.. code-block:: yaml
   :caption: Notebook YAML sidecar

   parameters:
     number:
       type: integer
       description: An integer
       default: 42
       minimum: 0
       maximum: 100

Floating point numbers
======================

For floating point numbers, use the ``number`` type.
In your code, cast the value to a Python float for use in calculations:

.. code-block:: yaml
   :caption: Notebook YAML sidecar

   parameters:
     number:
       type: number
       description: A number
       default: 27.5

.. code-block:: python
   :caption: Notebook parameters cell

   number = "27.5"

.. code-block:: python
   :caption: Notebook code

   number = float(number)

Validation constraints
----------------------

Like the ``integer`` type, the ``number`` type supports validation constraints.
You can specify minimum values and maximum values (both or either):

.. code-block:: yaml
   :caption: Notebook YAML sidecar

   parameters:
     number:
       type: number
       description: A number
       default: 27.5
       minimum: 0
       maximum: 100

Booleans
========

Boolean (true/false) values are supported with the ``boolean`` type.
The string representation is based on JSON's ``true`` and ``false`` values.
To convert the string into a Python boolean, you can compare the string:

.. code-block:: yaml
   :caption: Notebook YAML sidecar

   parameters:
     switch_param:
       type: boolean
       description: A boolean
       default: true

.. code-block:: python
   :caption: Notebook parameters cell

   switch_param = "true"

.. code-block:: python
   :caption: Notebook code

   switch_param = switch_param == "true"

Related documentation
=====================

- :doc:`sidecar-schema`
