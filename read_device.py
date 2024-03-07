#!/usr/bin/env python3
from appstoreconnect import createASCToken, get, post
import sys


def readDevice(id):
    url = f'https://api.appstoreconnect.apple.com/v1/devices/{id}'
    print(url)
    response = get(url)
    if response.status_code == 200:
        device_data = response.json()
        print(device_data)
    else:
        print(f'{id} Query Failed')


id = sys.argv[1]
readDevice(id)
