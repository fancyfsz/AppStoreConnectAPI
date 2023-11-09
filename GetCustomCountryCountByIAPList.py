# 调用举例：python3 GetCustomCountryCountByIAPList.py product_ids.txt > result.csv
#!/usr/bin/env python3
from appstoreconnect import createASCToken, get, post
import sys
import json
import pandas as pd
from get_custom_country_count import getCustomCountryCount


def createProductId2IapIdMapper():
    index_col = "productId"
    usecols = ["productId", "AppleID"]
    return pd.read_csv(
        "lf.csv",  # 如果测日本包，替换成lf_jp.csv
        index_col=index_col,
        usecols=usecols).to_dict()['AppleID']


# 先存mapper
mapper = createProductId2IapIdMapper()


def read_product_ids_from_file(file_path):
    product_ids = []
    with open(file_path, 'r') as file:
        for line in file:
            product_id = line.strip()
            if product_id:
                product_ids.append(product_id)
    return product_ids


# 替换为包含内购产品ID的文本文件路径
product_ids_file_path = sys.argv[1]  # '/path/to/your/product_ids.txt'

# 从文件中读取内购产品ID列表
product_ids = read_product_ids_from_file(product_ids_file_path)
print('product_id,cnt')

for product_id in product_ids:
    if product_id in mapper:
        iap_id = mapper[product_id]
        if iap_id:
            cnt = getCustomCountryCount(iap_id)
            print(f'{product_id},{cnt}')
