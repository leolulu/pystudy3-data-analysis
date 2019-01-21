import requests
from lxml import etree
from concurrent.futures import ThreadPoolExecutor
from retrying import retry
import pymysql
import threading
import pandas as pd
import time
import random

header = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",
    "cookie": r"locale=en; _pk_ref.2.42fa=%22%5B%5C%22%5C%22%2C%20%5C%22%5C%22%2C%201546843248%2C%20%5C%22https%3A%2F%2Fwww.sankakucomplex.com%2F%3Fpg%3DX%5C%22%5D%22; BetterJsPop0=1; _pk_ses.2.42fa=*; auto_page=1; _pk_id.2.42fa=74b05b6f7f58b1ca.1546843248.2.1546848178.1546847096."
}
proxies = {
    "http": "socks5://127.0.0.1:1080",
    'https': 'socks5://127.0.0.1:1080'
}

lock = threading.Lock()


def saveToCsv(df, i):
    df.to_csv('./sankaku数据.csv', encoding='utf-8', mode='a', index=False, header=False)
    print(i, '存入成功')


def saveToDb(img_id, tag_list, rating, i):
    sql = 'insert into gelbooru_anlaly(img_id,tag_list,rating) values(%s,%s,%s)'
    # print((img_id, tag_list, rating))
    try:
        cursor.execute(sql, (img_id, tag_list, rating))
        db.commit()
        print(i, '存入成功')
    except Exception as e:
        db.rollback()
        print(e, '存入失败')


@retry(wait_fixed=5000, stop_max_attempt_number=2)
def parse_csv(i):
    img_id = 4578487-i
    try:
        url = 'https://gelbooru.com/index.php?page=post&s=view&id={}'.format(img_id)

        r = requests.get(url, headers=header, proxies=proxies, timeout=9)

        tag_list = etree.HTML(r.content).xpath("//img/@alt")
        tag_list = ' '.join(tag_list)
        rating = etree.HTML(r.content).xpath("//li[contains(text(),'Rating')]/text()")
        rating = rating[0].split(':')[-1].strip()

        df = pd.DataFrame({
            'img_id': [img_id],
            'tag_list': [tag_list],
            'rating': [rating]
        })
        
        with lock:
        	# 存入csv
        #     saveToCsv(df, i)
        	# 存入数据库
        	saveToDb(img_id, tag_list, rating, i)

    except Exception as e:
        print(i, e, 'WTF')
        raise


db = pymysql.connect('132.232.0.240', 'yxy', 'test', 'mydb')
cursor = db.cursor()

for i in range(4578):
    with ThreadPoolExecutor(max_workers=128) as excutor:
        excutor.map(parse_csv, [i for i in range(1000 * i, 1000 * (i+1))])

db.close()
