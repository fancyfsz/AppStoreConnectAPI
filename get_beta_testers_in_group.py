#!/usr/bin/env python3
from appstoreconnect import createASCToken, get
import csv
import sys

# 获取指定 Beta 组的测试员列表


def get_beta_testers_in_group(group_id):
    url = f'https://api.appstoreconnect.apple.com/v1/betaGroups/{group_id}'
    response = get(url)

    if response.status_code == 200:
        # print('Success:', response.json())
        group_data = response.json().get('data', {})
        group_name = group_data.get(
            'attributes',
            {}).get(
            'name',
            'unknown_group').replace(
            ' ',
            '_')

        # 获取 beta testers 的链接
        beta_testers_link = group_data['relationships']['betaTesters']['links']['related']
        testers_response = get(beta_testers_link)

        if testers_response.status_code == 200:
            testers = testers_response.json().get('data', [])
            write_to_csv(testers, group_name)
        else:
            print(
                f'Error fetching testers: {testers_response.status_code}, {testers_response.text}')
    else:
        print(f'Error: {response.status_code}, {response.text}')


def write_to_csv(testers, group_name):
    # CSV 文件名
    csv_file = f'beta_group_{group_name}_testers.csv'

    # 提取数据并写入 CSV
    with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        # 写入表头，包括 Beta 组的额外信息
        writer.writerow(['Tester ID', 'First Name', 'Last Name', 'Email'])

        # 写入每个 beta tester 的信息
        for tester in testers:
            attributes = tester.get('attributes', {})
            writer.writerow([
                tester['id'],
                attributes.get('firstName', ''),
                attributes.get('lastName', ''),
                attributes.get('email', ''),
            ])

    print(f'Data has been written to {csv_file}.')


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python script.py <betaGroupId>")
        sys.exit(1)

    beta_group_id = sys.argv[1]
    get_beta_testers_in_group(beta_group_id)
