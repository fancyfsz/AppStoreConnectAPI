#!/usr/bin/env python3
import requests
import jwt
import time
from urllib3.util.retry import Retry
from requests.adapters import HTTPAdapter


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
            # 60 minutes timestamp
            "exp": int(round(time.time() + (60.0 * 60.0))),
            # need your app bundle id here
            "bid": ""
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

token = createASCToken(p8, kid, iss)
header = {
    "Authorization": f"Bearer {token}"
}


def get(url):
    # 创建一个重试策略
    retry_strategy = Retry(
        total=3,  # 总共重试次数（包括第一次请求）
        backoff_factor=0.5,  # 重试间隔时间的因子（指数退避算法）
        status_forcelist=[500, 502, 503, 504],  # 遇到这些 HTTP 状态码时进行重试
        method_whitelist=["GET"]
    )

    # 创建一个会话并将重试策略应用于该会话
    session = requests.Session()
    adapter = HTTPAdapter(max_retries=retry_strategy)
    session.mount("http://", adapter)
    session.mount("https://", adapter)

    rs = session.get(url, headers=header)

    if rs.status_code != 200:
        print(rs.status_code)
        print(url)
        # print(rs.json())
    return rs


def post(url, body):
    # 创建一个重试策略
    retry_strategy = Retry(
        total=3,  # 总共重试次数（包括第一次请求）
        backoff_factor=0.5,  # 重试间隔时间的因子（指数退避算法）
        status_forcelist=[500, 502, 503, 504],  # 遇到这些 HTTP 状态码时进行重试
        method_whitelist=["POST"]
    )

    # 创建一个会话并将重试策略应用于该会话
    session = requests.Session()
    adapter = HTTPAdapter(max_retries=retry_strategy)
    session.mount("http://", adapter)
    session.mount("https://", adapter)

    rs = session.post(url, headers=header, json=body)

    if rs.status_code != 201:
        print(rs.status_code)
        print(url)
    return rs
