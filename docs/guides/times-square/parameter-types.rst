###############
Parameter types
###############

Times Square notebooks use parameters to pass inputs into the notebook.
Different types of parameters are supported, and these types inform the interface for users to enter values and the validation that's performaed on those values.
This page lists the different types of parameters that are supported.

Parameters are always strings in the the notebook
=================================================

Keep in mind that parameter types are only for constructing the user interface and for validating input.
Parameters do not change the value's Python type in the notebook.
Values in a notebook's parameter's cell are always strings.

For example, an "integer" parameter is a string in the notebook. It's up to the notebook's code to further convert that string into the appropriate Python type.

.. code-block:: python

   # Parameters cell
   parameter = "42"

   # Notebook code transforms the parameter to a relevant type
   param_int = int(parameter)

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
       description: An ISO8601 daate
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
       default: "2024-01-01"

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
