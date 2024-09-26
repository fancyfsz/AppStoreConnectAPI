#!/usr/bin/env python3
from appstoreconnect import createASCToken, get
import csv


def write_to_csv(data):
    # CSV 文件名
    csv_file = 'beta_groups.csv'

    # 提取数据并写入 CSV
    with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        # 写入表头
        writer.writerow(['ID', 'Name', 'Public Link', 'Created Date'])

        # 写入每个 beta group 的信息
        for group in data['data']:
            writer.writerow([
                group['id'],
                group['attributes'].get('name', ''),
                group['attributes'].get('publicLink', ''),
                group['attributes'].get('createdDate', ''),
            ])

    print(f'Data has been written to {csv_file}.')

# 获取 Beta 组列表


def get_beta_groups():
    url = 'https://api.appstoreconnect.apple.com/v1/betaGroups'
    response = get(url)

    if response.status_code == 200:
        # print('Success:', response.json())
        write_to_csv(response.json())
    else:
        print(f'Error: {response.status_code}, {response.text}')


if __name__ == '__main__':
    get_beta_groups()
