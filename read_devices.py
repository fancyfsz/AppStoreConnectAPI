# 调用示例：python3 read_devices.py > devices.csv
#!/usr/bin/env python3
from appstoreconnect import createASCToken, get, post


def readDevices():
    url = 'https://api.appstoreconnect.apple.com/v1/devices?limit=200'

    response = get(url)
    if response.status_code == 200:
        print('id,name,udid,model,status')
        device_data = response.json()
        # print(device_data)
        devices = device_data['data']
        for device in devices:
            device_attributes = device['attributes']
            device_id = device['id']
            device_name = device_attributes['name']
            device_udid = device_attributes['udid']
            device_model = device_attributes['model']
            device_status = device_attributes['status']
            print(
                f'{device_id},{device_name},{device_udid},{device_model},{device_status}')
    else:
        print(f'Query Device List Failed')


readDevices()
