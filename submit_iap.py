#!/usr/bin/env python3
from appstoreconnect import createASCToken, get, post
import sys


def check_iap_status(iap_id):
    url = f'https://api.appstoreconnect.apple.com/v2/inAppPurchases/{iap_id}'
    response = get(url)

    if response.status_code == 200:
        iap_data = response.json()
        return iap_data['data']['attributes']['state']
    else:
        return None


def submit_iap_for_review(iap_id):
    url = 'https://api.appstoreconnect.apple.com/v1/inAppPurchaseSubmissions'
    body = {
        "data": {
            "type": "inAppPurchaseSubmissions",
            "relationships": {
                "inAppPurchaseV2": {
                    "data": {
                        "id": f"{iap_id}",
                        "type": "inAppPurchases"
                    }
                }
            }
        }
    }

    response = post(url, body)
    if response.status_code == 201:
        print(f'InAppPurchase {iap_id} commit success.')
    else:
        print(f'InAppPurchase {iap_id} commit failed.')


def check_iap_status_before_submit(iap_id):
    status = check_iap_status(iap_id)
    if status is not None:
        if status == "READY_TO_SUBMIT":
            submit_iap_for_review(iap_id)
        else:
            print(f'{iap_id} now state: {status}')
    else:
        print(f'failed to fetch {iap_id} state')


iap_id = sys.argv[1]
check_iap_status_before_submit(iap_id)
