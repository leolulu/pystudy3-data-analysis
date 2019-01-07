import requests
from lxml import etree
from concurrent.futures import ThreadPoolExecutor
from retrying import retry
import pymysql
import threading
import pandas as pd

header = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",
    "cookie": r"locale=en; _pk_ref.2.42fa=%22%5B%5C%22%5C%22%2C%20%5C%22%5C%22%2C%201546843248%2C%20%5C%22https%3A%2F%2Fwww.sankakucomplex.com%2F%3Fpg%3DX%5C%22%5D%22; BetterJsPop0=1; _pk_ses.2.42fa=*; auto_page=1; _pk_id.2.42fa=74b05b6f7f58b1ca.1546843248.2.1546848178.1546847096."
}
proxies = {
    "http": "socks5://127.0.0.1:1080",
    'https': 'socks5://127.0.0.1:1080'
}
lock = threading.Lock()


@retry(wait_exponential_multiplier=1000, wait_exponential_max=60000)
def parse_mysql(i):
    try:
        url = 'https://chan.sankakucomplex.com/post/show/{}'.format(7446472-i)

        r = requests.get(url, headers=header, proxies=proxies)
        if r.status_code == 429:
            raise Exception('返回429')

        with lock:
            tag_list = etree.HTML(r.content).xpath("//ul[@id='tag-sidebar']/li/a/text()")
            tag_list = str(tag_list)
            rating = etree.HTML(r.content).xpath("//div[@id='stats']/ul/li[last()]/text()")
            rating = rating[0].split(':')[-1]

            sql = 'insert into sankaku(tag_list,rating) values(%s,%s)'

            try:
                cursor.execute(sql, (tag_list, rating))
                db.commit()
                print(i)
            except Exception as e:
                db.rollback()
    except Exception as e:
        print(i, e, 'WTF')
        raise


@retry(wait_exponential_multiplier=1000, wait_exponential_max=60000)
def parse_csv(i):
    img_id = 7446472-i
    try:
        url = 'https://chan.sankakucomplex.com/post/show/{}'.format(img_id)

        r = requests.get(url, headers=header, proxies=proxies)
        if r.status_code == 429:
            raise Exception('返回429')

        with lock:
            tag_list = etree.HTML(r.content).xpath("//ul[@id='tag-sidebar']/li/a/text()")
            tag_list = str(tag_list)
            rating = etree.HTML(r.content).xpath("//div[@id='stats']/ul/li[last()]/text()")
            rating = rating[0].split(':')[-1]

            df = pd.DataFrame({
                'img_id': [img_id],
                'tag_list': [tag_list],
                'rating': [rating]
            })
            df.to_csv('./sankaku数据.csv', encoding='utf-8', mode='a', index=False, header=False)
            print(i, '存入成功')
    except Exception as e:
        print(i, e, 'WTF')
        raise


# db = pymysql.connect('132.232.0.240', 'yxy', 'test', 'mydb')
# cursor = db.cursor()

with ThreadPoolExecutor(max_workers=12) as excutor:
    for i in range(1000):
        excutor.submit(parse_csv, i)


# db.close()
