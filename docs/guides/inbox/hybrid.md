# The Hybrid Model

The flagship Rubin Science Platform (RSP) at [data.lsst.cloud](https://data.lsst.cloud) is a hybrid deployment, with services and data distributed across multiple data centers:

- Most of the services and some data are hosted on the Google Cloud Platform.
- A few services and most of the data are hosted at our US Data Facility (USDF) at SLAC.

This architecture provides flexibility and performance while controlling storage costs.

When an outage occurs, service and data availability can be affected differently depending on which data center is impacted.
During LSST Data Previews, the RSP does not yet provide detailed error messages from its services.
This page provides guidance on what to expect when USDF/SLAC is offline and how to continue using the RSP during such outages.

## Service availability during a USDF (SLAC) outage

The following table shows service availability when [data.lsst.cloud](https://data.lsst.cloud) is operational but USDF/SLAC is experiencing an outage:

| Service         | DP1 | DP0.3 | DP0.2 |
| --------------- | --- | ----- | ----- |
| TAP (catalogs)  | ❌  | ❌    | ❌    |
| HIPS            | ✅  | ❌    | ❌    |
| SIA (images)    | ✅  | ❌    | ❌    |
| SODA (cutouts)  | ✅  | ❌    | ❌    |
| ObsTAP (images) | ❌  | ❌    | ❌    |

### What you can do during a USDF/SLAC outage

- Access the Notebook aspect
- Use services marked with ✅ above
- Analyze previously retrieved data

### Portal functionality during a USDF/SLAC outage

The following image shows which Portal tabs remain functional during a USDF/SLAC outage:

![Working portal tabs](portal_nogo.png)

```{tip}
If your portal does not look like the above image, you can configure the visible tabs by using the "hamburger" menu on the top left.
```

### Getting updates during a USDF/SLAC outage

During a service outage, you can monitor updates from the [data.lsst.cloud homepage](https://data.lsst.cloud) or the [Community forum News category](https://community.lsst.org/c/news/data-services/64). See {doc}`/guides/life/updates`.
