##########################################
Rubin Science Platform Status and Roadmap
##########################################

What can you do with the Rubin Science Platform?
================================================

Below you will find a detailed (but not exhaustive) list of current and future RSP capabilities.

Please not the difference between Data Previews (DP0, DP1, DP2) which are early access programs before the start of the survey, and Data Releases (DR1, DR2 etc) which are the official data releases after the survey starts.
For the planned dates for those events please consult project documentation and announcements.

But before we get there, bear in mind there are three constraints to what you can do on the RSP:

1. Scope. The Rubin Science Platform is aimed at providing access to Rubin Data Products and next-to-the-data analytics; there are some things it is not scoped to provide, for example large-scale re-processing of raw data (there are other inititatives that might help with that, but it's not a function of the RSP and is not planned to be).

2. Affordability. There are limitations placed not by the capabilities of the RSP, but the budgeted cost to provide them to a very large userbase. For example, the storage per user is set by what the project can afford to provide. This could change with funding, change in the underlying cost of computing infrastructure or usage (for example if we have fewer users that we modeled there would be more resources for those users); but at any given time, it places a strong constraint on what can be provided by the project to everyone in the data-rights holding community.

3. Developmental stage. Because the Rubin project predated the Science Platform era and many of the technologies we have since built on, there are actually significantly more developer-years ahead of us than behind us. We have a vigorous development program for the duration of the survey that gives us room to respond to needs beyond our construction requirements. However at this time, the RSP is in preview mode; that means there are many capabilities that will be available by DR1 that are not available in Data Preview mode, either because they are still under development or because they have not yet been demonstrated to scale sufficiently well.

We deploy updates to the RSP every week (though many are behind-the-scenes improvements) and will continue to do so for the duration of operations.
In the list below, when something is indicated as being "on the roadmap" it means we have a conceptual design for providing it but it has not been scheduled for work and no ETA can be given at this time.
When a capability is listed as "planned" it means there is a high degree of certainty that it will be available by the start of operations, or if so indicated, sooner.



APIs
====

There are a large number of programmatic APIs to RSP capabilities that can be used both from within and externall to the RSP.
Wherever possible, these are based on Virtual Observatory protocols for interoperability with existing clients (such as TOPCAT and pyvo) and other science archives.
We have an active engagement with the IVOA community to extend those protocols for "big data" science and other needs that arise from the Rubin Community.

Catalog searches
----------------

Catalog searches are provided through the TAP protocol.

Current TAP capabilities include the ability to do synchronous and asynchronous queries against Data Preview 0.2 catalogs stored in Qserv (our high performance database for large spatially shardable catalogs) and Data Preview 0.3 catalogs stored in Postgres (solar system objects only).

Temporary table uploads, which allow users to provide, at query time, a catalog to be joined with the queried table (such as returning only sources that are in listed in user provided table) are currently available for Postgres-stored catalogs only (currently DP0.3 datasets).

Temporary table uploads for Qserv-stored catalogs are planned DP1 later this year.

Persistent user table uploads are planend to be available for DP2.

There are currently some ADQL compliant searches that cannot be serviced in Qserv (such as intersects). There are planned to be available by DP2.

Currently there is no environmental data (eg observing conditions) available for query in the RSP. This is planned to be available by the start of the survey.

TAP query results are now returned in TABLEDATA and BINARY2 serialisations.
Additional serialisations better suited to large datasets (such as parquet) are in the roadmap.

Currently there is no way for a user to inspect or interact with their query history. An early version of this capability is planned for DP1, with more to come.

Image searches
--------------

Currently image searches are possible through TAP (ObsCore) queries.

Queries using the IVOA SIA (v2) protocol were planned for DP1 but have been deployed early.

Within the RSP Notebook Aspect, images can also be retrieved directly from the Rubin middleware system (Butler).

A HIPS data service is available.

