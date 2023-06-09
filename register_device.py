#!/usr/bin/env python3
from appstoreconnect import createASCToken, get, post
import sys

def registerDevice(udid, name):
    url = 'https://api.appstoreconnect.apple.com/v1/devices'
    body = {
        "data": {
            "attributes": {
                "name": f'{name}',
                "platform": "IOS",
                "udid": f'{udid}'
            },
            "type": "devices"
        }
    }

    response = post(url, body)
    if response.status_code == 201:
        print(f'Register {name} success.')
    else:
        print(f'Register {name} failed.')


# Unique Device Identifier
udid = sys.argv[1]
# Customized Device Name
name = sys.argv[2]

registerDevice(udid, name)
