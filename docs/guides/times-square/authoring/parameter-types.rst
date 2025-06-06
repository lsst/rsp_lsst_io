###############
Parameter types
###############

Times Square notebooks use parameters to pass inputs into the notebook.
Different types of parameters are supported, and these types inform the interface for users to enter values and the validation that's performed on those values.
You define parameters in a notebook's :doc:`sidecar YAML-formatted metadata file <sidecar-schema>` and their values are assigned in the notebook's *parameters cell*, which is always the first code cell in the notebook.
This page lists the different types of parameters that are supported.

.. _ts-param-types-string:

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

.. _ts-param-types-date:

Dates
=====

Dates (without times) are a *format* of the basic string type.
Users enter dates in the format ``YYYY-MM-DD`` (ISO 8601) and your notebook receives the date as a :py:obj:`datetime.date` object.

.. code-block:: yaml
   :caption: Notebook YAML sidecar

   parameters:
     start_date:
       type: string
       format: date
       description: An ISO8601 date
       default: "2024-01-01"

.. code-block:: python
   :caption: Notebook parameters cell

   import datetime

   start_date = datetime.date.fromisoformat("2024-01-01")

Note how Times Square automatically imports the :py:obj:`datetime` module for you in the parameters cell to parse the date into a :py:obj:`datetime.date` object.
Replicate this pattern in the default parameters cell of your notebook.

Instead of a fixed default date, you can also set a *dynamic default* that is relative to the date the notebook is viewed:

.. code-block:: yaml
   :caption: Notebook YAML sidecar

   parameters:
     start_date:
       type: string
       format: date
       dynamic_default: "today"

See :doc:`dynamic-date-defaults` for more information about the syntax for ``dynamic_default``.

.. _ts-param-types-dayobs:

DAYOBS
======

Rubin Observatory uses DAYOBS to identify an observing night since the DAYOBS is consistent over the course of a night.
DAYOBS is defined as the date in the UTC-12 timezone, and is represented as a string with eight digits: ``YYYYMMDD``.

.. code-block:: yaml
   :caption: Notebook YAML sidecar

   parameters:
     start_dayobs:
       type: string
       format: dayobs
       description: A DAYOBS date
       default: "20240101"

.. code-block:: python
   :caption: Notebook parameters cell

   start_dayobs = "20240101"

The format of the DAYOBS string is validated, but no processing is done in the parameters cell.

Instead of a fixed default DAYOBS, you can also set a *dynamic default* that is relative to the date the notebook is viewed:

.. code-block:: yaml
   :caption: Notebook YAML sidecar

   parameters:
     start_dayobs:
       type: string
       format: dayobs
       dynamic_default: "yesterday"

See :doc:`dynamic-date-defaults` for more information about the syntax for ``dynamic_default``.

.. _ts-param-types-datetime:

Date and time
=============

Dates and times are another *format* of the basic string type that specify a precise moment in time.
Date and time parameters are entered in the format ``YYYY-MM-DDTHH:MM:SS+HH:MM`` (ISO 8601) and your notebook receives the date as a :py:obj:`datetime.datetime` object.
Note that a time zone is required.
Besides specifying a time zone offset, you can also use the ``Z`` suffix to indicate UTC.

.. code-block:: yaml
   :caption: Notebook YAML sidecar

   parameters:
     start_time:
       type: string
       format: date-time
       description: An ISO8601 date and time
       default: "2024-01-01T12:00:00Z"

.. code-block:: python
   :caption: Notebook parameters cell

   import datetime

   start_time = datetime.datetime.fromisoformat("2024-01-01T12:00:00Z")

Note how Times Square automatically imports the :py:obj:`datetime` module for you in the parameters cell to parse the date into a :py:obj:`datetime.date` object.
Replicate this pattern in the default parameters cell of your notebook.

.. _ts-param-types-integer:

Integers
========

For decimal numbers, use the ``integer`` type.
In your code, these values are Python ``int`` objects.

.. code-block:: yaml
   :caption: Notebook YAML sidecar

   parameters:
     number:
       type: integer
       description: An integer
       default: 42

.. code-block:: python
   :caption: Notebook parameters cell

   number = 42

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

.. _ts-param-types-number:

Floating point numbers
======================

For floating point numbers, use the ``number`` type.
In your code, these values are Python ``float`` objects.

.. code-block:: yaml
   :caption: Notebook YAML sidecar

   parameters:
     number:
       type: number
       description: A number
       default: 27.5

.. code-block:: python
   :caption: Notebook parameters cell

   number = 27.5

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

.. _ts-param-types-boolean:

Booleans
========

Boolean (true/false) values are supported with the ``boolean`` type.
The string representation is based on JSON's ``true`` and ``false`` values.
To convert the string into a Python boolean, you can compare the string:
In your code, these values are Python bool (``True`` / ``False``) objects.

.. code-block:: yaml
   :caption: Notebook YAML sidecar

   parameters:
     switch_param:
       type: boolean
       description: A boolean
       default: true

.. code-block:: python
   :caption: Notebook parameters cell

   switch_param = True

Related documentation
=====================

- :doc:`sidecar-schema`
