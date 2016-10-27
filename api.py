from config import ENDPOINT, TOKEN

import json
import requests


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