from config import ENDPOINT, TOKEN

import json
import requests

"""
This is just a dummy lazy function for the requests get/post methods that
authenticates and runs whatever request you wish to supply to the API.

Requires that config.py contain ENDPOINT and TOKEN, you can configure those
by running `setup.py`.

Example usage for api lazy function:

Get all probes:
    api("probes", method="get")

Get the probe with serial 0x29384:
    api("probes", method="get", data={'serial': "0x29384"})

Get the probe named "ambient":
    api("probes", method="get", data={'name': "ambient"})

Send data for the probe with ID #1 in the django database:
    api("probedata", method="post", data={'id':'1', 'value':'22.22'})

There are probably other examples I could write for the switches and probedata
endpoints, but I'm probably going to continue to be lazy and not document
those here.

"""


def api(url, data={}, method="get"):
    if not url.endswith("/"):
        url += "/"
    api_url = "{}{}".format(ENDPOINT, url)

    headers = {'Authorization': 'Token {}'.format(TOKEN)}

    if method == "get":
        return json.loads(requests.get(api_url, headers=headers, params=data).text)
    elif method == "post":
        return json.loads(requests.post(api_url, headers=headers, data=data).text)
    #else
    #   other methods? bueller?