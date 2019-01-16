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

lock = threading.Lock()

def getProxyId():
    return requests.get('http://123.207.35.36:5010/get').text

@retry(wait_fixed=2000, stop_max_attempt_number=10)
def parse_csv(i):
    img_id = 7450761-i
    try:
        url = 'https://chan.sankakucomplex.com/post/show/{}'.format(img_id)
        ip = getProxyId()
        proxies = {
            "http": ip,
            'https': ip
        }

        print(proxies)

        r = requests.get(url, headers=header, proxies=proxies)

        if r.status_code == 429:
            raise Exception('返回429')

        tag_list = etree.HTML(r.content).xpath("//ul[@id='tag-sidebar']/li/a/text()")
        tag_list = str(tag_list)
        rating = etree.HTML(r.content).xpath("//div[@id='stats']/ul/li[last()]/text()")
        rating = rating[0].split(':')[-1]

        df = pd.DataFrame({
            'img_id': [img_id],
            'tag_list': [tag_list],
            'rating': [rating]
        })
        with lock:
            df.to_csv('./sankaku数据.csv', encoding='utf-8', mode='a', index=False, header=False)
            print(i, '存入成功')
    except Exception as e:
        print(i, e, 'WTF')


for i in range(74):
    with ThreadPoolExecutor(max_workers=32) as excutor:
        excutor.map(parse_csv, [i for i in range(100000 * i, 100000 * (i+1))])
