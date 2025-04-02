#########################################
Rubin Science Platform Status and Roadmap
#########################################

What can you do with the Rubin Science Platform?
================================================

Below you will find a detailed (but not exhaustive) list of current and future RSP capabilities.

Please note the difference between Data Previews (DP0, DP1, DP2), which are early access programs before the start of the survey, and Data Releases (DR1, DR2, etc.), which are the official data releases after the survey starts.
For the planned dates for those events please consult project documentation and `announcements <https://rubinobservatory.org/news>`__.

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
For example, we have been taking a leadership position in developing standards for the use of Parquet in IVOA protocols, for more efficient transfer of large query results.

Catalog searches
----------------

Catalog searches are provided through the IVOA TAP protocol, both for use inside the RSP's Notebook and Portal Aspects, and externally (with proper authentication).
TAP queries are expressed in the IVOA's "ADQL" language, a dialect of SQL92 with the addition of spherical-geometry constructs, and then translated to be executed on the back-end database.

Current TAP capabilities include the ability to do synchronous and asynchronous queries against Data Preview 0.2 catalogs stored in Qserv (our high performance database for large spatially sharded catalogs) and Data Preview 0.3 catalogs stored in Postgres (in DP0, for solar system objects only).

TAP's temporary table uploads, which allow users to provide, at query time, a catalog to be joined with the queried table, enabling efficient multi-object searches, are currently available for Postgres-stored catalogs only (currently DP0.3 datasets).

Temporary table uploads for Qserv-stored catalogs are planned to be available in time for DP1 later this year.

(Note that temporary-table uploads are only for the lifetime of individual queries and should not be confused with support for persistent user databases.  These are planned to be available in time for DP2.  An extension to TAP originated by CADC is expected to be used to provide API access to this capability.  This is discussed in more detail below.)

There are currently some elements of the ADQL language that are not supported by our Qserv back end.  Some of these limitations (e.g, sub-queries are not supported) are fairly fundamental.  Others are more superficial, such as the current lack of support for the spatial ``INTERSECTS()`` operation, and improvements in this category are planned to be available by DP2.

Currently there is no environmental data (e.g., observing conditions) available for query in the RSP. These data _are_ being recorded, and an RSP query capability is planned to be available by the start of the survey.

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

The RSP Portal Aspect provides query interfaces, image and catalog visualizations, and a set of basic tools for exploratory data analysis.
These capabilities are meant to facilitate exploration of the Rubin/LSST data and assist users in becoming more familiar with both the data and the RSP data services.

The Portal and the Notebook Aspects are intended to be complementary and serve a wide range of user levels of expertise and familiarity with the data, and individual preferences for programmatic or UI-based access to data.

Some users, for some use cases, may work entirely within the Portal; others may use it for initial data selection, with subsequent detailed analysis in notebooks; others may use it only for "quick-look" purposes, or simply to remind themselves of elements of the LSST data model which they will then code against in notebooks.

The Portal is *not* intended to replicate the full breadth of scientific visualization capabilities available in the wider scientific Python and JupyterLab ecosystem; however, the RSP aims at making the connections between the Aspects sufficiently easy to use that it is natural to begin work in the Portal and then segue to more in-depth analysis in a notebook, where such tools can be used.

The Portal will in general always provide access to all the API Aspect data services.
In its present state, it in particular supports:
* TAP queries for catalog data, both through UI forms that provide a visual means of constructing queries, and through an interface for writing explicit ADQL queries;
* ObsTAP and SIAv2 queries for images; and
* following annotations in the data that lead users to additional queries they can perform -- e.g., retrieving light curves for individual objects in an Object table query result.

The Portal supports multi-object queries based on the temporary-table-upload capabilities described above in the API Aspect section, and provides a simple interface for using the result of one query as an input to another.

These capabilities are based on the IVOA standards adopted by the project for its APIs, and so are also applicable to a wide range of other astronomical archives, including Gaia at ESAC, NASA's IRSA and MAST, the CADC's extensive holdings, and beyond.
Results from queries to other archives can be combined in a wide variety of ways with Rubin query results.

The Portal provides image visualization capabilities that exploit Rubin-specific details of the image data, such as per-pixel flag overlays displaying data quality and other per-pixel assessments by the Rubin pipelines.

As noted above, the Portal's visualization capabilities are easily accessed from notebooks in the RSP, and we will continue to improve those interfaces on the road to DR1.

As is the case for the other RSP Aspects and services, the Portal is regularly updated with additional features and performance improvements, not only in association with new data releases.
Since the original release of DP0.2, the Portal UI has been extensively refreshed and clarified, performance on large tabular query results has been significantly improved, and a wide variety of smaller-scale features added.

Road map
--------

The Portal road map includes the following major planned developments:

* An expanded and clarified query-status and query-history display capability, released together with the corresponding API services on the back end.  An initial version of this will be available for DP1 and it will continue to be developed with additional features.
* Context-sensitive access to documentation on the Rubin data model, pipelines, and data quality.  This capability also depends on future back-end data services and will begin to be deployed later in 2025 and reach maturity with DP2 and beyond, as additional content is developed by the project.
* An interface to the RSP API service for persistent user tables.  Portal users will be able to create and interact with such tables, and the Portal will support straightforward workflows for saving query results as persistent user tables.  This capability will be released in parallel with the underlying API service.
* An interface to a future RSP API service for storing and sharing file-oriented data with other users, likely based on VOSpace.

The user-facing capabilities of the Portal will also be expanded by taking more advantage of its existing ability to follow links embedded in the data to facilitate additional queries and data retrievals.  An example would be the ability to retrieve and display the specific input images associated with a coadd tile, based on provenance information in the data.

The Portal is based on the underlying, open-source "IPAC Firefly" tool, with customizations for the Rubin environment.  Firefly development is supported by a combination of, primarily, IRSA and Rubin resources, and is closely tied in to development of improvements and extensions to the IVOA's community standards for astronomical data access.


Full LSSTCam focal-plane visualizations
---------------------------------------

A separate capability from the Portal, but integrated with it and the rest of the RSP, is planned to be provided for the visualization of full LSSTCam focal-plane images by the DP2 era.  It may be released sooner in a version applicable to the DP1 (ComCam) data; development and scale testing is currently under way.

The integration with the Portal will allow focal-plane-level image searches to be performed using the same ObsTAP and SIAv2 interfaces, but with the results directed to the dedicated viewer, as well as allowing the user to return from the dedicated viewer to the Portal for detailed visualization of CCD-scale images with the Portal's more extensive feature set.

General
=======

During the DP0 small-cohort delegate program, some controls were not applied (such as disk quotas). Quotas will start being enforced starting with DP1.

A new system for submitting feedback, and to support help requests such as authentication issues that are not suited for our open community forum, will be available starting with DP1, replacing the GitHub Issues system we used during DP0.

There is a high demand for more performant computation, which we are committed to provide within our resources.
A Dask (parallel Python computing) service is on the roadmap, and we are investigating ways to competitively provide access to GPU and/or other resources friendly to machine learning.

Contextual help and more documentation will be an on-going project, with some new features coming for DP1.

