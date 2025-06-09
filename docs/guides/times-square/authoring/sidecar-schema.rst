####################################
Sidecar metadata YAML file reference
####################################

Every notebook in a Times Square GitHub repository has an associated sidecar metadata file.
These files have the same path and name as the notebook, but with a ``.yaml`` extension.

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

It should be fairly short because it is displayed in a narrow column.

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

   parameters:
     start_date:
       type: string
       format: date
       default: 2024-02-01
     end_date:
       type: string
       format: date
       default: 2024-02-29

.. code-block:: yaml
    :caption: Invalid parameter names

    parameters:
      start date:
         type: string
         format: date
         default: 2024-02-01
      end-date:
         type: string
         format: date
         default: 2024-02-29

Each parameter is an object with the following fields:

- ``type`` (*string*, required) is one of:

  - ``string``
  - ``integer`` (whole number)
  - ``number`` (floating-point number)
  - ``boolean``

- ``format`` (*string*, optional) is a format string that describes the expected format of the parameter value:

  - ``date`` for date parameters (e.g., ``2024-10-10``)
  - ``dayobs`` for Rubin DAYOBS dates (e.g., ``20241010``), defined as the date in UTC-12.
  - ``date-time`` for date-time parameters (e.g., ``2024-10-10T04:00Z``).

- ``default`` (*string*, required) is the default value of the parameter. The default must be a valid value for the parameter.

  For ``date`` and ``dayobs`` format parameters, the ``default`` field can be replaced with a ``dynamic_default`` field to set a default relative to the current date. See :doc:`dynamic-date-defaults` for more information.

- ``description`` (*Markdown string*) is the description of the parameter as it appears in the Times Square UI.

- ``minimum`` (*integer* or *number*, optional) is the minimum value of the parameter, for numeric parameters.

- ``maximum`` (*integer* or *number*, optional) is the maximum value of the parameter, for numeric parameters.

For more information about parameters, see :doc:`parameter-types`.

schedule
--------

(*array of objects*, optional) A notebook can have multiple schedule rules that define when the notebook should be executed automatically.
Each schedule rule is an object that can take one of three forms:

Fixed date schedule
^^^^^^^^^^^^^^^^^^^

A schedule rule for a fixed date and time:

.. code-block:: yaml
   :caption: Fixed date schedule example

   schedule:
     - date: 2024-12-25T09:00:00Z
       exclude: false

Fields:

- ``date`` (*string*, required) A fixed date-time to include (or exclude) from the schedule. The date-time should be in ISO 8601 format (e.g., ``2024-12-25T09:00:00Z``).
- ``exclude`` (*boolean*, optional) Set to ``true`` to exclude this date from the schedule. Defaults to ``false``.

Recurring schedule from a start date
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

A schedule rule that repeats from a specific starting date:

.. code-block:: yaml
   :caption: Recurring schedule from start date example

   schedule:
     - start: 2024-01-01T09:00:00Z
       freq: monthly
       interval: 2
       count: 6
       exclude: false

Fields:

- ``start`` (*string*, required) The date-time when the repeating rule starts. Should be in ISO 8601 format.
- ``freq`` (*string*, required) Frequency of recurrence. One of: ``yearly``, ``monthly``, ``weekly``, ``daily``, ``hourly``, ``minutely``.
- ``interval`` (*integer*, optional) The interval between each iteration. For example, if ``freq`` is ``monthly``, an interval of ``2`` means every two months. Defaults to ``1``.
- ``end`` (*string*, optional) The date-time when this rule ends. The last recurrence is less than or equal to this date. Cannot be used with ``count``.
- ``count`` (*integer*, optional) The number of occurrences of this recurring rule. Cannot be used with ``end``.
- ``exclude`` (*boolean*, optional) Set to ``true`` to exclude these events from the schedule. Defaults to ``false``.

Complex recurring schedule
^^^^^^^^^^^^^^^^^^^^^^^^^^

A schedule rule with advanced recurrence patterns (based on RFC 5545 iCalendar standard):

.. code-block:: yaml
   :caption: Complex recurring schedule example

   schedule:
     - freq: monthly
       weekday:
         - day: friday
           index: 1  # First Friday of the month
       hour: [9]
       minute: [0]
       exclude: false

Fields:

- ``freq`` (*string*, required) Frequency of recurrence. One of: ``yearly``, ``monthly``, ``weekly``, ``daily``, ``hourly``, ``minutely``.
- ``week_start`` (*string*, optional) The week start day for weekly frequencies. One of: ``sunday``, ``monday``, ``tuesday``, ``wednesday``, ``thursday``, ``friday``, ``saturday``. Defaults to ``monday``.
- ``set_position`` (*integer*, or *array of integers*, optional) Specifies occurrence numbers within the recurrence frequency. For example, with monthly frequency and ``weekday`` of Friday, a value of ``1`` specifies the first Friday of the month, ``-1`` specifies the last Friday.
- ``month`` (*integer*, or *array of integers*, optional) The months (1-12) when recurrence happens. Use negative integers to specify from end of year.
- ``day_of_month`` (*integer*, or *array of integers*, optional) The days of the month (1-31) when recurrence happens. Use negative integers to specify from end of month.
- ``day_of_year`` (*integer*, or *array of integers*, optional) The days of the year (1-366) when recurrence happens. Use negative integers to specify from end of year.
- ``week`` (*integer*, or *array of integers*, optional) The weeks of the year (1-52) when recurrence happens. Use negative integers to specify from end of year.
- ``weekday`` (*string*, *array of strings*, *object*, or *array of objects*, optional) The days of the week when recurrence happens. As a string this is the day of the week. Use the object form to also include an index in the frequency period. Each object has:

  - ``day`` (*string*, required) The day of the week: ``sunday``, ``monday``, ``tuesday``, ``wednesday``, ``thursday``, ``friday``, ``saturday``.
  - ``index`` (*integer*, optional) The index of the weekday. For monthly frequency, ``1`` means the first occurrence of that weekday in the month, ``-1`` means the last.

- ``hour`` (*integer*, or *array of integers*, optional) The hours of the day (0-23) when recurrence happens. Defaults to ``[0]``.
- ``minute`` (*integer*, or *array of integers*, optional) The minutes of the hour (0-59) when recurrence happens. Defaults to ``[0]``.
- ``second`` (*integer*, or *integer*, optional) The second of the minute (0-59) when recurrence happens. Defaults to ``0``.
- ``exclude`` (*boolean*, optional) Set to ``true`` to exclude these events from the schedule. Defaults to ``false``.

schedule_enabled
----------------

(*boolean*, optional) If set to ``false``, the schedule is disabled and no automatic notebook runs will occur.
