# OAPEN Driver
[![Release](https://img.shields.io/github/release/hirmeos/oapen_driver.svg?colorB=58839b)](https://github.com/hirmeos/oapen_driver/releases) [![License](https://img.shields.io/github/license/hirmeos/oapen_driver.svg?colorB=ff0000)](https://github.com/hirmeos/oapen_driver/blob/master/LICENSE)

This driver allows programmatic retrieval and normalisation of OAPEN usage data, obtained via IRUS-UK API.

NB. Unlike other drivers developed within the HIRMEOS metrics project, OAPEN’s driver is **not meant to be used by the general public** (although it’s possible to do so). This software is used to programmatically collect and normalise data for all publications in the OAPEN library, which are then made publicly available through the [metrics API][1].

## Run via crontab
```
0 0 * * 0 docker run --rm --name "oapen_driver" --env-file /path/to/config.env -v oapen_cache:/usr/src/app/cache -v metrics:/usr/src/app/output openbookpublishers/oapen_driver
```

[1]: https://metrics.operas-eu.org/docs/metrics-api "Metrics API docs"
