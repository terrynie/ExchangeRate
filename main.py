#coding: utf-8
__author__ = 'terry'
import time
from exchange import exchange

#数据库连接信息
host="localhost"
user="root"
passwd="root"
dbname="exchange"
charset="utf8"

ex = exchange()
conn = ex.makeConnectionToMySQL(host,user,passwd,dbname,charset)
while 1:
    contents = ex.readHtml()
    ex.splitAndStore(contents,conn)
    #每小时更新一次数据
    time.sleep(60*60)
