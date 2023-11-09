#!/usr/bin/env python3
from appstoreserverconnect import createASCToken, get, post


def check_transactions_status(transcation_id):
    # sandbox环境的订单用这个url查询
    url = f'https://api.storekit-sandbox.itunes.apple.com/inApps/v1/transactions/{transcation_id}'
    # url = f'https://api.storekit-sandbox.itunes.apple.com/inApps/v1/history/{transcation_id}'
    # url = f'https://api.storekit-sandbox.itunes.apple.com/inApps/v1/subscriptions/{transcation_id}'
    response = get(url)
    if response.status_code == 200:
        transcation_data = response.json()
        signedTransactionInfo = transcation_data['signedTransactionInfo']
        print(signedTransactionInfo)
    else:
        return None

# check_transactions_status(2000000401549447)
