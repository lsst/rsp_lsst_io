##########################################
Rubin Science Platform Status and Roadmap
##########################################

What can you do with the Rubin Science Platform?
================================================

Below you will find a detailed (but not exhaustive) list of current and future RSP capabilities.

Please note the difference between Data Previews (DP0, DP1, DP2), which are early access programs before the start of the survey, and Data Releases (DR1, DR2, etc.), which are the official data releases after the survey starts.
For the planned dates for those events please consult project documentation and announcements.

But before we get there, bear in mind there are three constraints to what you can do on the RSP:

1. Scope. The Rubin Science Platform is aimed at providing access to Rubin Data Products and next-to-the-data analytics.  There are some things it is not scoped to provide, for example: large-scale re-processing of raw data, or re-creation of coadds across the sky (there are other initiatives that might help with that, but it's not a function of the RSP and is not planned to be given current expectations for the available physical resources).

2. Affordability. There are limitations placed not by the capabilities of the RSP (its architecture and code), but by the budgeted cost to provide them to a very large user base. For example, the storage per user is set by what the project can afford to provide. This could change with funding, change in the underlying cost of computing infrastructure or usage (for example if we have fewer users than we modeled there would be more resources for those users); but at any given time, it places a strong constraint on what can be provided by the project to everyone in the data-rights holding community.

3. Developmental stage. At this time, the RSP is in preview mode; that means there are many capabilities that will be available by DR1 that are not yet available, either because they are still under development or because they have not yet been demonstrated to scale sufficiently well.
In fact, we expect that there are significantly more developer-years ahead of us than behind us. We have a vigorous development program for the duration of the survey that gives us room to respond to needs beyond our construction requirements.

We deploy updates to the RSP every week (though many are behind-the-scenes improvements) and will continue to do so for the duration of operations.
In the list below, when something is indicated as being "on the roadmap" it means we have a conceptual design for providing it but it has not been scheduled for work and no ETA can be given at this time.
When a capability is listed as "planned" it means there is a high degree of certainty that it will be available by the start of operations, or if so indicated, sooner.



APIs
====

There are a large number of programmatic APIs to RSP capabilities that can be used both from within and externally to the RSP.
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

TAP query results are now returned in the IVOA VOTable ``TABLEDATA`` and ``BINARY2`` serialisations.  The latter, which is significantly more efficient, will shortly become the default.
Additional serialisations better suited to large datasets (such as Apache Parquet) are in the roadmap.

We plan very extensive annotation of tables and tabular query results with high-quality metadata, including mechanisms to link data to associated documentation.
A fraction of this capability was deployed for DP0.2 to support ongoing development, and additional metadata are being supplied progressively.
We expect DP1 to reflect a substantial advance on the original state of DP0.2 in this respect.
Currently there is no way for a user to inspect or interact with their query history. An early version of this capability is planned for DP1, with more to come.

Image searches
--------------

Currently image searches are possible through ObsTAP queries -- queries against the IVOA ObsCore data model for observation metadata.
In DP0.2 the variety of spatial queries supported was limited by the ADQL issues mentioned above; by DP2 we expect this to be significantly improved.

Queries using the IVOA SIA (v2) protocol, which also operate against the ObsCore data model but with a simplified query protocol, were planned for DP1 but have been deployed early.
The region-intersection type of query that was not supported in ObsTAP for DP0.2 (and won't be available in ObsTAP until DP2) _are_ supported in SIAv2 and will be available via that protocol for DP1.

Within the RSP Notebook Aspect, images can also be retrieved directly from the Rubin middleware system (Butler).

A HIPS data service is available.

Compute APIs
------------

A SODA-compliant image cutout service is available.

A bulk cut-out service is planned by DP2.

A PSF retrieval service is planned by DP2.

Notebooks
=========

The Notebook service is based on JupyterLab (which is itself under active development) with a number of RSP enhancements with more to come.

There is a growing suite of tutorial notebooks available directly in the Notebook demonstrating the capabilities of the RSP as well as helping users understand the LSST data products and pipelines. Many more are to come. A more user-friendly way of accessing the increasing number of tutorials will be available for DP1.

A number of visualisation options are available, including Firefly, the same visualisation engine available via the RSP Portal.

Starting with DP1, expect to see Portal integration features such as the ability to seed a notebook with a query that was one in the Portal. More such features are in the roadmap.

While a very powerful in-browser environment, working exclusively through the browse can feel limiting. We have a number of features planned to improve user experience, such as a WebDAV service that would allow users to edit files on their RSP home space from their preferred device. An early version of this could be available for DP1.

Portal
======

General
=======

During the DP0 small-cohort delegate program, some controls were not applied (such as disk quotas). Quotas will start being enforced starting with DP1.

A new system for submitting feedback and needing with help such as authentication issues that are not suited for our open community forum will be available starting with DP1, replacing the Github Issues system we used during DP0.

There is a high demand for more performant computation, which we are committed to provide within our resources. A dask service is on the roadmap, and we are investigating ways to competitively provide access to GPU and/or other resources friendly to machine learning.

Context help and more documentation will be an on-going project, with some new features coming for DP1.

