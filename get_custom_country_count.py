#!/usr/bin/env python3
from appstoreconnect import createASCToken, get, app_id
import sys


def getCustomCountryCount(iap_id):
    url = f'https://api.appstoreconnect.apple.com/v1/inAppPurchasePriceSchedules/{iap_id}/manualPrices'
    response = get(url)

    if response.status_code == 200:
        data = response.json()
        prices = data['data']

        return len(prices) - 1
    else:
        print(f'failed to query {iap_id}')
        return 0


# iap_id = sys.argv[1]
# custom_country_count = get_custom_country_count(iap_id)
# print(f'inAppPurchase {iap_id} set {custom_country_count} custom countries')