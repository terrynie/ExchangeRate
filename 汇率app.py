#coding:utf-8
import urllib2
import re
import MySQLdb

def strToFloat(str):
    mFloat = 0.0
    if(str != ''):
        mFloat = float(str)
    return mFloat

request = urllib2.Request('http://data.bank.hexun.com/other/cms/foreignexchangejson.ashx?callback=ShowDatalist',data=None,headers = {
    'Connection': 'Keep-Alive',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4',
    'Cookie':'vjuids=-33daed2da.152fe7ce078.0.41c5eb1c; vjlast=1455968543.1456497069.13; HexunTrack=SID=2016022019423407476fdfcb307fe4b3abfa46be4d178e670&CITY=41&TOWN=410100',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36'
})

response = urllib2.urlopen(request)
html = response.read()
html = html.decode('gb2312','ignore').encode('utf-8')
contents = re.findall("{bank:'(.*?)',currency:'(.*?)',code:'(.*?)',currencyUnit:'(.*?)',cenPrice:'(.*?)',buyPrice1:'(.*?)',sellPrice1:'(.*?)',buyPrice2:'(.*?)',sellPrice2:'(.*?)',releasedate:'(.*?)'}",html,re.S)
# connect to MySQL
conn=MySQLdb.connect(host="localhost",user="root",passwd="root",db="exchange",charset="utf8")
cursor = conn.cursor()

for content in contents:
    if(content[1] != ''):
        bank = content[0]
        currency = content[1]
        code = content[2]
        currencyUnit = content[3]
        cenPrice = strToFloat(content[4])
        remittanceBuyPrice = strToFloat(content[5])
        sellPrice = strToFloat(content[6])
        cashBuyPrice = strToFloat(content[7])
        sellPrice2 = strToFloat(content[8])
        releasedate = content[9]
        sql = "INSERT INTO exchange_rate(bank, currency, code, currencyUnit, cenPrice, remittanceBuyPrice, sellPrice, cashBuyPrice, sellPrice2, releasedate) VALUES('%s','%s','%s','%s','%f','%f','%f','%f','%f','%s') " % (bank,currency,code,currencyUnit,cenPrice,remittanceBuyPrice,sellPrice,cashBuyPrice,sellPrice2,releasedate)
        cursor.execute(sql)
        conn.commit()
