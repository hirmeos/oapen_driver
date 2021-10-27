#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json.decoder
import requests

BASE_URL = "https://irus.jisc.ac.uk/api/oapen"
PLATFORM = 215
ATTRIBUTES_TO_SHOW = "Country"
METRIC_TYPE = "Unique_Item_Requests"


class IrusClient(object):
    """Single entry point to the IRUS OAPEN API"""

    def __init__(self, requestor_id, api_key, base_url=BASE_URL,
                 platform=PLATFORM, attributes_to_show=ATTRIBUTES_TO_SHOW,
                 metrics_type=METRIC_TYPE):
        self.base_url = base_url
        self.requestor_id = requestor_id
        self.api_key = api_key
        self.platform = platform
        self.attributes_to_show = attributes_to_show
        self.metric_type = metrics_type

    def item_report(self, begin_date, end_date):
        path = "/reports/oapen_ir"
        params = {
            "begin_date": begin_date,
            "end_date": end_date
        }
        return self.make_request(path, params)

    def platform_report(self, begin_date, end_date):
        path = "/reports/oapen_pr"
        params = {
            "begin_date": begin_date,
            "end_date": end_date
        }
        return self.make_request(path, params)

    def make_request(self, path, params):
        params["requestor_id"] = self.requestor_id
        params["api_key"] = self.api_key
        params["platform"] = self.platform
        params["attributes_to_show"] = self.attributes_to_show
        params["metric_type"] = self.metric_type
        url = "{}{}".format(self.base_url, path)

        try:
            res = requests.get(url, params)
            if res.status_code != 200:
                raise ValueError
            data = res.json()
            res.close()
            return data
        except (KeyError, TypeError, ValueError,
                json.decoder.JSONDecodeError,
                requests.exceptions.RequestException):
            raise ValueError(res.content)
