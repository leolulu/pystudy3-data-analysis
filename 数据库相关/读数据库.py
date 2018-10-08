import pymysql
from matplotlib import pyplot as plt

db = pymysql.connect(host='132.232.0.240', port=3306, user='yxy', password='test', database='mydb')
cursor = db.cursor()
sql = 'SELECT * from weather_scrapy'
cursor.execute(sql)
result = [i[2] for i in cursor.fetchall()]
db.close()

x = range(1,2838)

# fig = plt.figure(figsize=(30,15),dpi=40)
plt.plot(x,result)
plt.xticks(range(1,2838,100))
plt.show()