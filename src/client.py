#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import json
import httplib2
import urllib.parse

URI_API_USER = os.environ['URI_API_USER']
URI_API_PASS = os.environ['URI_API_PASS']
AUTH_API_ENDP = os.environ['AUTH_API_ENDP']
URI_API_WORKS = os.environ['URI_API_WORKS']
COUNTRY_API_ENDP = os.environ['COUNTRY_API_ENDP']
COUNTRY_CACHE = {}


class Client(object):
    """Single entry point to the translation service API"""

    def __init__(self):
        self.token = self.get_token(AUTH_API_ENDP, URI_API_USER, URI_API_PASS)
        self.auth = 'Bearer ' + self.token
        self.auth_headers = {'Authorization': self.auth}

    def get_token(self, url, email, passwd):
        h = httplib2.Http()
        credentials = {'email': email, 'password': passwd}
        headers = {'content-type': 'application/json'}
        res, content = h.request(url, 'POST', json.dumps(credentials), headers)
        if res.status != 200:
            raise ValueError(content.decode('utf-8'))
        return json.loads(content.decode('utf-8'))['data'][0]['token']

    def request_identifiers(self, url):
        h = httplib2.Http()
        res, content = h.request(url, 'GET', headers=self.auth_headers)
        if res.status != 200:
            raise ValueError(content.decode('utf-8'))
        return json.loads(content.decode('utf-8'))['data']

    def get_all_works(self):
        url = (URI_API_WORKS
               + '?filter=uri_scheme:tag:oapen.org,2008,uri_scheme:info:doi'
               + '&strict=true')
        return self.request_identifiers(url)

    def get_country_code(self, country_name):
        country_name = urllib.parse.quote(country_name.encode('utf8'))
        if country_name in COUNTRY_CACHE:
            return COUNTRY_CACHE[country_name]
        req = "%s?country_name=%s" % (COUNTRY_API_ENDP, country_name)
        h = httplib2.Http()
        res, content = h.request(req, 'GET', headers=self.auth_headers)
        if res.status != 200:
            r = json.loads(content.decode('utf-8'))
            m = "%s: %s" % (r['message'], r['parameters']['country_name'])
            print(m, file=sys.stderr)
            return ""
        code = json.loads(content.decode('utf-8'))['data'][0]['country_id']
        COUNTRY_CACHE[country_name] = code
        return code
