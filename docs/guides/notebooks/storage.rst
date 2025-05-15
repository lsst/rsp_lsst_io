:orphan:

============
User Storage
============



.. jinja:: rsp

    {% if env.is_primary %}

    {% else %}

   .. important::

      Documentation for |rsp-at| storage is pending.

      This section does not apply to the selected deployment at this time

    {% endif %}

There are a number of options planned for user storage in the RSP.

In this preview, only unix filesystem (POSIX) storage is available.
This storage behaves like the disk you have on your laptop.

From the notebook aspect there are two user-writeable filesystems at this time:

* /home (permanent space)
* /cleared-weekly (scratch space)

Additionally, users have read-only access to /rubin, a filesystem in which project staff may make available additional files for general use.

Home
-----

/home is the filesystem that contains files that you wish to retain.

There is a quota applied to ensure fairness.
At this time, your quota is 20 GB.
We plan to increase by Data Preview 2.
Additional increases during the lifetime of the survey are also likely.

By default, your home space contents are only viewable by you and Rubin staff.
You can create sub-directories in your home space that are viewable and writeable by your collaburators (or even viewable by all users; writeable by all is technically permitted but inadvisable)
See [] on how to do this.
Any sub-directories write-able by others are still counted towards your quota.

In the future, and depending on demand, other ways to share data may be available.

Files in your home directory are backed up for disaster recovery.

Scratch space
-------------

Scratch space is available on a partition called /cleared-weekly to ensure that nobody forgets that it is cleared out on a weekly basis on Sundays.

The intent is that this space can serve as a temporary "relief valve" on your home space by allowing you to perform operations with large intermediate files.
Do not forget to copy any results back to your home space for space keeping.

Space is ample (currently a 20 TB partition) with no quotas applied that is shared by all users.
This means that technically it can fill up.

Policies on scratch space size and clearance may change and are likely to be made more lenient if we determine it is being used responsibly.

Scratch space is *not backed up* and deleted files cannot be retrieved.
It is also possible for files to be lost in the event of a major disaster.


