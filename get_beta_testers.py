#!/usr/bin/env python3
from appstoreconnect import createASCToken, get, app_id
import csv

def write2CSV(data):
    # CSV 文件名
    csv_file = 'beta_testers.csv'

    # 提取数据并写入 CSV
    with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        # 写入表头
        writer.writerow(['ID', 'First Name', 'Last Name', 'Email', 'Invite Type'])
        
        # 写入每个 beta tester 的信息
        for tester in data['data']:
            attributes = tester['attributes']
            writer.writerow([
                tester['id'],
                attributes['firstName'],
                attributes['lastName'],
                attributes['email'],
                attributes['inviteType']
            ])

    print(f'Data has been written to {csv_file}.')

# 获取 Beta 测试者列表
def get_beta_testers():
    url = 'https://api.appstoreconnect.apple.com/v1/betaTesters'
    response = get(url)

    if response.status_code == 200:
        # print('Success:', response.json())
        write2CSV(response.json())
    else:
        print(f'Error: {response.status_code}, {response.text}')

if __name__ == '__main__':
    get_beta_testers()