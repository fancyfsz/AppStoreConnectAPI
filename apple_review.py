import requests
import csv
import time

# 获取应用评论的函数


def get_reviews(app_id, country='us', max_pages=10):
    reviews = []
    page = 1
    while page <= max_pages:
        # 构造API请求URL
        url = f"https://itunes.apple.com/rss/customerreviews/page={page}/id={app_id}/sortby=mostrecent/json?l=en&cc={country}"
        response = requests.get(url)

        if response.status_code != 200:
            print(
                f"Error fetching data from page {page}. Status code: {response.status_code}")
            break

        data = response.json()

        if 'feed' in data and 'entry' in data['feed']:
            for entry in data['feed']['entry']:
                author = entry['author']['name']['label']
                title = entry.get('title', {}).get('label', 'No Title')
                content = entry['content']['label']
                rating = entry['im:rating']['label']
                updated = entry['updated']['label']

                # 收集每条评论的信息
                reviews.append({
                    'author': author,
                    'title': title,
                    'rating': rating,
                    'content': content,
                    'date': updated
                })
        else:
            print(f"No reviews found on page {page}.")
            break

        page += 1
        time.sleep(1)  # 防止过于频繁的请求，休眠一秒

    return reviews

# 将评论保存到CSV文件


def save_reviews_to_csv(reviews, filename="app_reviews.csv"):
    # 定义CSV文件的列名
    fieldnames = ['author', 'title', 'rating', 'content', 'date']

    # 写入CSV文件
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for review in reviews:
            writer.writerow(review)

    print(f"Saved {len(reviews)} reviews to {filename}")


# 示例：替换为你想要抓取评论的应用 ID
app_id = '1540557475'  # 比如Last Fortress的App ID
reviews = get_reviews(app_id)

# 保存评论数据到CSV文件
save_reviews_to_csv(reviews)
