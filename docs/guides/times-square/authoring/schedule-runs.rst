##################################
Scheduling automatic notebook runs
##################################

By default, Times Square runs a notebook when a user views it and the notebook hasn't already been computed with the requested parameters.
For notebooks that are meant to update on a regular basis, especially those that use dates as parameters, you can schedule automatic runs of the notebook.
Scheduled runs ensure that a notebook is always computed for a given date, and lets users see the page immediately without waiting for the notebook to run.

Scheduled runs always use the parameter defaults defined in the notebook's sidecar metadata file.
Scheduling works well with :doc:`dynamic defaults for date and dayobs parameters <dynamic-date-defaults>`, since those defaults are established at the time the notebook is run.
If a scheduled run repeats the same parameters as a previous run, the results of the previous run are replaced with the new results.

Scheduling is a powerful feature, and although there aren't currently restrictions on how often you can schedule a notebook, you should be careful not to schedule runs too frequently (such as several times an hour).
For near-real-time updates, consider using dashboards in Chronograf or Grafana or even custom web applications instead of Times Square.

Quick start
===========

To schedule a notebook to run automatically, add a ``schedule`` field to the notebook's :doc:`sidecar metadata file <sidecar-schema>`.
Here are some common recipes for scheduling notebooks:

.. code-block:: yaml
   :caption: Sidecar metadata YAML file with a daily run schedule:

   title: "My Notebook"
   description: "This notebook runs every day at 8:00 AM UTC."
   parameters: []

   schedule:
     - freq: "daily"
       hour: 8

Other recipes for the ``schedule`` field include:

.. code-block:: yaml
   :caption: Schedule a notebook to run the first day of every month at 8:15 AM UTC:

   schedule:
     - freq: "monthly"
       day_of_month: 1
       hour: 8
       minute: 15

.. code-block:: yaml
   :caption: Schedule a notebook to the last day of every month at 11:55 PM UTC:

   schedule:
     - freq: "monthly"
       day_of_month: -1
       hour: 23
       minute: 55

.. code-block:: yaml
   :caption: Schedule a notebook to run every weekday at 8:00 AM UTC:

    schedule:
      - freq: "daily"
         hour: 8
         weekday:
            - monday
            - tuesday
            - wednesday
            - thursday
            - friday

How to create schedules is described below.

Adding a schedule (in more detail)
==================================

Schedules are set in the notebook's :doc:`sidecar metadata file <sidecar-schema>` with two fields: ``schedule`` and ``schedule_enabled``.
The latter is a boolean that enables or disables the schedule and can take values of ``true`` or ``false``.
The former is an array of schedule *rules*.
A basic schedule that runs a notebook every day at 8:00 AM UTC looks like this:

.. code-block:: yaml
   :caption: Sidecar metadata YAML file that schedules a notebook to run every day at 8:00 AM UTC.

   title: "My Notebook"
   description: "This notebook runs every day at 8:00 AM UTC."
   parameters: []
   schedule_enabled: true
   schedule:
     - freq: "daily"
       hour: 8

Because the schedule is an array of rules, you can combine multiple recipes.
For example, you can run a notebook daily on weekdays, but also at the end of the month:

.. code-block:: yaml
   :caption: Sidecar metadata YAML file that schedules a notebook to run every weekday at 8:00 AM UTC and at the end of the month.

   tile: "My Notebook"
   description: "This notebook runs every weekday at 8:00 AM UTC and at the end of the month."
   parameters: []
   schedule_enabled: true
   schedule:
     - freq: "daily"
       hour: 8
       weekday:
         - monday
         - tuesday
         - wednesday
         - thursday
         - friday
     - freq: "monthly"
       day_of_month: -1
       hour: 23
       minute: 55

.. seealso:: The :doc:`sidecar metadata schema <sidecar-schema>` provides details on the :ref:`schedule <ts-sidecar-schema-schedule>` and :ref:`schedule_enabled <ts-sidecar-schema-schedule-enabled>` fields.

Rules can skip events indicated by other rules
----------------------------------------------

Any schedule rule can have a ``exclude: true`` field that indicates any scheduled dates that match the rule should be skipped.
The exclusion rules are processed after the inclusion rules, so you can think of this as "schedule these times, but not these times."
This is useful to in combination with other rules that would otherwise run the notebook at unnecessary times.

For example, if you want to run a notebook every day at 8:00 AM UTC, but skip weekends, you can use the following schedule:

.. code-block:: yaml
   :caption: Sidecar metadata YAML file that schedules a notebook to run every day at 8:00 AM UTC, but skips weekends.

   tile: "My Notebook"
   description: "This notebook runs every day at 8:00 AM UTC, but skips weekends."
   parameters: []
   schedule_enabled: true
   schedule:
     - freq: "daily"
       hour: 8
     - freq: "daily"
       weekday:
         - saturday
         - sunday
       hour: 8
       exclude: true

Schedules are generally in the UTC time zone
--------------------------------------------

Times Square schedules are generally in the UTC time zone.
When you specify ``hour``, that hour is in UTC.

Schedules that :ref:`start from a specific date <ts-schedule-on-date>` can set their timezone in the reference ``start`` field if you want to use a different time zone without having to convert the time to UTC.

Three types of schedule rules
-----------------------------

Times Square supports three basic types of schedule rules:

- scheduling on a specific date (:ref:`example <ts-schedule-on-date>`)
- scheduling a recurrence from a specific date (:ref:`example <ts-schedule-from-date>`)
- complex rules based on days of the year, month, week, and hours and minutes in the day (:ref:`details <ts-complex-schedule-rules>`).

All of these schedule rules can be combined in the ``schedule`` array.
The remainder of this guide describes each of these types of rules in detail.

.. _ts-schedule-on-date:

Scheduling on a specific date
=============================

To schedule a notebook to run on a single specific date and time, use schedule rule with a ``date`` field that has an ISO 8601 date string:

.. code-block:: yaml
   :caption: Sidecar metadata YAML file that schedules a notebook to run on a specific date.

   tile: "My Notebook"
   description: "This notebook runs on a specific date."
   parameters: []
   schedule_enabled: true
   schedule:
     - date: "2024-10-10T08:00:00Z"

.. _ts-schedule-from-date:

Schedule a recurrence from a specific date
==========================================

To schedule a notebook from a given start date that repeats at a given frequency, use a schedule rule with a ``start`` field that takes an ISO 8601 date string and a ``freq`` field that indicates the frequency of the recurrence.
For simple schedules, this can be the simplest type of schedule rule to set up and understand.

.. code-block:: yaml
   :caption: Sidecar metadata YAML file that schedules a notebook to run every day starting from a specific date.

   tile: "My Notebook"
   description: "This notebook runs every day starting from a specific date."
   parameters: []
   schedule_enabled: true
   schedule:
     - start: "2024-10-10T08:00:00Z"
       freq: "daily"

The ``freq`` field can take the following values:

- ``daily``: runs every day at the specified time.
- ``weekly``: runs every week on the specified day of the week at the specified time.
- ``monthly``: runs every month on the specified day of the month at the specified time.
- ``yearly``: runs every year on the specified day of the year at the specified time.

You can also specify an ``interval`` field.
By default the interval is ``1``, but to run every other day, you can set the interval to ``2`` for example.

.. code-block:: yaml
   :caption: Sidecar metadata YAML file that schedules a notebook to run every other day starting from a specific date.

   tile: "My Notebook"
   description: "This notebook runs every other day starting from a specific date."
   parameters: []
   schedule_enabled: true
   schedule:
     - start: "2024-10-10T08:00:00Z"
       freq: "daily"
       interval: 2

The remainder of this documentation describes how to set up more complex schedules based on days of the year, month, week, and hours and minutes in the day.
The easiest way to understand these rules is through specific recipes.

.. _ts-complex-schedule-rules:

Complex schedule rules
======================

Schedule a notebook to run every Monday at specific time
--------------------------------------------------------

To schedule a notebook to run every Monday at a specific time, use the ``weekday`` field with the value ``monday`` and specify the hour and minute in UTC:

.. code-block:: yaml
   :caption: Sidecar metadata YAML file that schedules a notebook to run every Monday at 8:00 AM UTC.

   tile: "My Notebook"
   description: "This notebook runs every Monday at 8:00 AM UTC."
   parameters: []
   schedule_enabled: true
   schedule:
     - freq: "weekly"
       weekday: monday
       hour: 8
       minute: 0

Schedule a notebook to run on the first Monday of every month
-------------------------------------------------------------

To schedule a notebook to run on the first Monday of every month, set the ``freq`` to ``monthly``.
Then for ``weekday`` field supply an object where ``day`` is ``monday``, and the ``index`` is ``1``:

.. code-block:: yaml
   :caption: Sidecar metadata YAML file that schedules a notebook to run on the first Monday of every month at 8:00 AM UTC.

   tile: "My Notebook"
   description: "This notebook runs on the first Monday of every month at 8:00 AM UTC."
   parameters: []
   schedule_enabled: true
   schedule:
     - freq: "monthly"
       weekday:
         - day: monday
           index: 1
       hour: 8
       minute: 0

The ``index`` field takes its meaning from the ``freq`` field.
With a monthly frequency, ``index`` refers to that monthly interval so ``1`` means the first Monday in each month.
If ``freq`` is ``yearly``, then ``index`` refers to the yearly interval, so ``1`` means the first Monday in the year.

Schedule a notebook to run on the last Friday of every month
------------------------------------------------------------

This schedule is similar to the previous one, but now the index is ``-1`` to indicate the last occurrence of the day in the month:

.. code-block:: yaml
   :caption: Sidecar metadata YAML file that schedules a notebook to run on the last Friday of every month at 8:00 AM UTC.

   tile: "My Notebook"
   description: "This notebook runs on the last Friday of every month at 8:00 AM UTC."
   parameters: []
   schedule_enabled: true
   schedule:
     - freq: "monthly"
       weekday:
         - day: friday
           index: -1
       hour: 8
       minute: 0

Use ``-2`` to indicate the second-to-last occurrence of the day in the interval, and so on.

Schedule a notebook to run on the last day of every month
---------------------------------------------------------

To schedule a notebook to run on the last day of every month, use the ``day_of_month`` field with the value ``-1``:

.. code-block:: yaml
   :caption: Sidecar metadata YAML file that schedules a notebook to run on the last day of every month at 8:00 AM UTC.

   tile: "My Notebook"
   description: "This notebook runs on the last day of every month at 8:00 AM UTC."
   parameters: []
   schedule_enabled: true
   schedule:
     - freq: "monthly"
       day_of_month: -1
       hour: 8
       minute: 0

Schedule a notebook to run on the first day of every month
----------------------------------------------------------

To schedule a notebook to run on the first day of every month, use the ``day_of_month`` field with the value ``1``:

.. code-block:: yaml
    :caption: Sidecar metadata YAML file that schedules a notebook to run on the first day of every month at 8:00 AM UTC.

    tile: "My Notebook"
    description: "This notebook runs on the first day of every month at 8:00 AM UTC."
    parameters: []
    schedule_enabled: true
    schedule:
      - freq: "monthly"
         day_of_month: 1
         hour: 8
         minute: 0

Schedule a notebook to run multiple times a day
-----------------------------------------------

Most examples use the ``hour`` and ``minute`` fields to specify a single time of day (in UTC) to run the notebook.
You can also provide a list of hours and minutes to run the notebook multiple times a day.
For example, to run the notebook both at 8:00 AM and at 5:00 PM UTC, you can use the following schedule:

.. code-block:: yaml
   :caption: Sidecar metadata YAML file that schedules a notebook to run at 8:00 AM and 5:00 PM UTC every day.

   tile: "My Notebook"
   description: "This notebook runs at 8:00 AM and 5:00 PM UTC every day."
   parameters: []
   schedule_enabled: true
   schedule:
     - freq: "daily"
       hour:
         - 8
         - 17

Schedule a notebook to run every hour
-------------------------------------

To schedule a notebook to run every hour, you can use the ``freq`` field with the value ``hourly``:

.. code-block:: yaml
   :caption: Sidecar metadata YAML file that schedules a notebook to run every hour.

   tile: "My Notebook"
   description: "This notebook runs every hour at 5 minutes past the hour."
   parameters: []
   schedule_enabled: true
   schedule:
     - freq: "hourly"
       minute: 5
       hour: null

.. tip::

   The ``hour`` field can be set to ``null`` to indicate that the notebook should run every hour at the specified minute rather than the default hour (which is 0).

Troubleshooting and tips
========================

Schedule rules can be complex, so here are some tips for troubleshooting and ensuring your schedules work as expected:

- **Times are in UTC**. The ``hour`` fields are in UTC, so make sure to convert your local time to UTC when setting the schedule. An alternative strategy is to set the ``start`` field in the schedule rule to a specific date and time in your local time zone, which will then be converted to UTC.
- **Hour is in the 24-hour clock.** The ``hour`` field uses a 24-hour clock, so 8 AM is ``8`` and 5 PM is ``17``.
- **Set freq to the interval the rule repeats over.** The ``freq`` field in schedule rules can be confusing. Is refers to the periodicity of the rule as a whole, rather than the rate that runs are scheduled. For example, a rule where weekday is ``[monday, tuesday, wednesday, thursday, friday]`` should have a ``freq`` of ``weekly`` rather than ``daily`` because that pattern as a whole repeats every week, not every day.
