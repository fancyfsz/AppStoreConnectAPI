#!/usr/bin/env python3
import requests
import jwt
import time


def createASCToken(p8KeyPath, kid, iss):
    try:
        header = {
            "alg": "ES256",
            "typ": "JWT",
            "kid": kid
        }
        payload = {
            "iss": iss,
            "aud": "appstoreconnect-v1",
            "iat": int(time.time()),
            # 20 minutes timestamp
            "exp": int(round(time.time() + (20.0 * 60.0)))
        }
        file = open(p8KeyPath)
        key_data = file.read()
        file.close()
        token = jwt.encode(
            headers=header,
            payload=payload,
            key=key_data,
            algorithm="ES256")
        return token
    except Exception as e:
        print(e)
        return ""


# Need your own configuration
p8 = ""
kid = ""
iss = ""
app_id = ""

token = createASCToken(p8, kid, iss)
header = {
    "Authorization": f"Bearer {token}"
}


def get(url):
    rs = requests.get(url, headers=header)

    if rs.status_code != 200:
        print(rs.status_code)
        print(url)
    return rs


def post(url, body):
    rs = requests.post(url, headers=header, json=body)

    if rs.status_code != 200:
        print(rs.status_code)
        print(url)
    return rs
