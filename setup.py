#!/usr/bin/python

import getpass
import json
import requests


endpoint = raw_input("Endpoint URL: ")
username = raw_input("Username/Email: ")
password = getpass.getpass('Password: ')


if not endpoint.endswith("/"):
    endpoint += "/"
auth_url = "{}{}".format(endpoint, "api-token-auth/")

r = requests.post(
    auth_url,
    data = {
        'username': username,
        'password': password,
    }
)

print r.text

t = json.loads(r.text)
token = None

try:
    token = t['token']

    config = open('config.py', 'w')
    config.truncate()
    config.write("ENDPOINT = '{}'\n".format(endpoint))
    config.write("TOKEN = '{}'\n".format(token))
    config.close()

    print "Config dumped to config.py"
except AttributeError:
    print "Unable to login or no token found."
