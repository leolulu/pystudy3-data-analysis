import pymysql
import pandas as pd

def getData(sql):
    '''
    从数据库获取数据
    '''
    conn = pymysql.connect('132.232.0.240','yxy','test','mydb')
    data = pd.read_sql(sql,conn)
    return data