#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import json
import sys
from datetime import date

import requests
from requests.auth import HTTPBasicAuth


class MyRequest:
    # chrome.console : navigator.userAgent
    headers = {
        "UserAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36"
    }
    username = None
    passcode = None

    def __init__(self) -> None:
        pass

    def __str__(self) -> str:
        pass

    def __repr__(self) -> str:
        pass

    def setHeaders(self, headers):
        self.headers = headers

    def getHeaders(self):
        return self.headers

    def setAuth(self, username, passcode):
        self.username = username
        self.passcode = passcode

    def getAuth(self):
        auth = HTTPBasicAuth(self.username, self.passcode)
        return auth

    def get(self, url):
        r = requests.get(url, headers=self.getHeaders(), auth=self.getAuth())
        if r.status_code != 200:
            raise Exception("Error: " + str(r.status_code))
        return r

    def post(self, url):
        r = requests.post(url, headers=self.getHeaders(), auth=self.getAuth())
        if r.status_code != 200:
            raise Exception("Error: " + str(r.status_code))
        return r
