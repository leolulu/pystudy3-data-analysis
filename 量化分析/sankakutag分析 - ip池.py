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
ip_pool = ["106.14.162.110:8080","60.255.186.169:8888","111.230.140.197:3128","120.78.131.10:3128","222.135.24.250:8060","221.6.201.18:9999","123.139.56.238:9999","41.222.226.45:80","119.28.249.39:8080","119.28.203.242:8000","218.60.8.99:3129","39.137.46.72:8080","121.69.37.6:9797","140.143.237.109:808","112.115.57.20:3128","27.208.70.173:8060","180.141.90.172:53281","222.132.145.122:53281","112.246.232.129:8060","120.24.156.230:3128","27.203.161.68:8060","112.17.65.133:8060","119.179.128.55:8060","47.104.213.220:8080","114.245.195.40:8060","47.104.166.2:8080","124.250.70.76:8123","114.95.161.59:8060","114.245.214.14:8060","218.241.219.226:9999","59.37.18.243:3128","123.117.172.197:8060","116.226.159.159:8060","103.199.12.12:8080","115.233.210.218:808","119.179.142.219:8060","112.66.77.178:8060","125.46.0.62:53281","122.6.121.233:8888","124.42.7.103:80","124.207.82.166:8008","115.206.101.231:8060","116.226.57.70:8060","110.167.204.78:8060","89.218.22.178:8080","61.128.208.94:3128","103.94.7.254:53281","177.38.66.237:44963","116.226.61.243:8060","51.38.71.101:8080","119.101.116.131:9999","222.173.90.162:8060","180.175.140.26:8060","119.101.114.243:9999","41.222.226.47:80","46.63.44.170:8080","39.137.69.7:8080","213.58.202.70:54214","123.232.200.241:8118","85.192.184.133:80","119.101.114.103:9999","120.92.174.37:1080","37.200.224.179:8080","212.200.27.134:8080","119.101.114.119:9999","103.42.195.70:53281","39.137.77.66:8080","115.199.53.114:8060"]

@retry(wait_fixed=2000, stop_max_attempt_number=30)
def parse_csv(i):
    img_id = 7450761-i
    try:
        url = 'https://chan.sankakucomplex.com/post/show/{}'.format(img_id)

        proxies = {
            "http": random.sample(ip_pool,1)[0],
            'https': random.sample(ip_pool,1)[0]
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



with ThreadPoolExecutor(max_workers=8) as excutor:
    excutor.map(parse_csv, [i for i in range(3000000)])

