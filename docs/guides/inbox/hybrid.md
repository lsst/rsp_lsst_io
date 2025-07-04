# The Hybrid Model

Our flagship Rubin Science Platform deployment at data.lsst.cloud is what we call a hybrid deployment:

* Most of the services and some data are hosted on the Google Cloud Platform
* A few services and most of the data are hosted at our US Data Facility at SLAC

The good news is that this architecture gives us a lot of flexibility and performance while controlling the storage cost.

The bad news is that outages can be complicated to understand, since depending on the problem some services can be fine for some data products but not others.

At this stage of the RSP preview period, we don't have the capability of having hyper-specific error messages from our services in such eventuality.
Which is why you are probably reading this after having being directed to it from an outage message...

At the time of DP1, this is what works if data.lsst.cloud is operating while SLAC is offline:

|                 | DP1 | DP0.3 | DP0.2|
|-----------------|-----|-------|------|
| TAP (catalogs)  | ❌   | ❌    | ❌   |
| HIPS            | ✅   | ❌    | ❌   |
| SIA (images)    | ✅   | ❌    | ❌   |
| SODA (cutouts)  | ✅   | ❌    | ❌   |
| ObsTAP (images) | ❌   | ❌    | ❌   |

You can still use the notebook aspect to access your files, use the services indicated as green above, analyze previously retrieved data and to practice your Jupyter/python skills.

In the portal, the following image indicates which tabs will work with DP1 data.

![Working portal tabs](portal_nogo.png)

(if your portal does not look like the above image, you can configure the visible tabs by using the "hamburger" menu on the top left)

The location of data products may change as operations evolve.