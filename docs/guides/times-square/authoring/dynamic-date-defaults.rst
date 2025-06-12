#######################################################
Setting dynamic defaults for date and dayobs parameters
#######################################################

Times Square notebooks use date parameters to generate reports for specific dates or date ranges.
With *dynamic defaults* for date parameters, you can set the default value of a date parameter to be relative to the current date so that users see the most relevant data when they view your notebook.

Using a dynamic default
=======================

Parameters require a default value, which is set with the ``default`` field for that parameter.
To make a date, dayobs, or dayobs-date parameter's default dynamic, replace that ``default`` field with a ``dynamic_default`` field:

.. code-block:: diff
   :caption: Example of a dynamic default for a date parameter

   parameters:
     start_date:
        type: string
        format: date
   -  default: 2024-10-01
   +  dynamic_default: "today"

Dynamic defaults work with date, dayobs, and dayobs-date parameters:

.. code-block:: yaml
   :caption: Example of a dynamic default for a dayobs parameter.

   parameters:
     start_dayobs:
       type: string
       format: dayobs-date
       dynamic_default: "today"

In the case of dayobs and dayobs-date, the default follows the UTC-12 timezone that dayobs dates are defined in.

Format for the dynamic_default field
====================================

The ``dynamic_default`` field's syntax allows you to specify a date relative to the current date for a variety of use cases.

Simple relative dates
---------------------

You can specify "today", "yesterday", or "tomorrow" to set the default to the current date, one day ago, or one day in the future, respectively:

.. code-block:: yaml

   dynamic_default: "today"     # Current date
   dynamic_default: "yesterday" # One day ago
   dynamic_default: "tomorrow"  # One day in the future

Relative days with offsets
--------------------------

You can use a ``-<offset>d`` or ``+<offset>d`` syntax to specify a number of days in the past or future:

.. code-block:: yaml

   dynamic_default: "-2d" # Two days ago
   dynamic_default: "+5d" # 5 days in the future


Relative number of weeks
------------------------

You can use a ``-<offset>w`` or ``+<offset>w`` syntax to specify a number of weeks in the past or future:

.. code-block:: yaml

   dynamic_default: "-1w" # One week ago
   dynamic_default: "+3w" # Three weeks in the future

Relative number of months
--------------------------

You can use a ``-<offset>m`` or ``+<offset>m`` syntax to specify a number of months in the past or future:

.. code-block:: yaml

   dynamic_default: "-2m"  # Two months ago
   dynamic_default: "+4m"  # Four months in the future

Relative number of years
--------------------------

You can use a ``-<offset>y`` or ``+<offset>y`` syntax to specify a number of years in the past or future:

.. code-block:: yaml

   dynamic_default: "-1y"  # One year ago
   dynamic_default: "+2y"  # Two years in the future

Start or end of the current week, month, or year
------------------------------------------------

You can use the ``<unit>_start`` or ``<unit>_end`` syntax to set the default to the start or end of the current week, month, or year:

.. code-block:: yaml

   dynamic_default: "week_start"  # Start of the current week
   dynamic_default: "week_end"    # End of the current week
   dynamic_default: "month_start" # Start of the current month
   dynamic_default: "month_end"   # End of the current month
   dynamic_default: "year_start"  # Start of the current year
   dynamic_default: "year_end"    # End of the current year

.. note:: The start of a week is a Monday, and the end of a week is a Sunday.

Start or end of the week, month, or year with offsets
-----------------------------------------------------

You can also specify an offset for the start or end of the week, month, or year:

.. code-block:: yaml

   dynamic_default: "-1week_start"   # Start of the previous week
   dynamic_default: "+2week_end"     # End of the week two weeks in the future
   dynamic_default: "-3month_start"  # Start of the month three months ago
   dynamic_default: "+1month_end+1m" # End of the month, next month
   dynamic_default: "-5year_start"   # Start of the year five years ago
   dynamic_default: "+1year_end"     # End of next year
