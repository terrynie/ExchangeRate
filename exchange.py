#coding:utf-8
import urllib2
import re
import MySQLdb

class exchange:

    # 将string转换为float
    def strToFloat(self,str):
        mFloat = 0.0
        if(str != ''):
            mFloat = float(str)
        return mFloat

    # 进行数据存储操作
    def saveData(self,content,conn):
        cursor = conn.cursor()
        if(content[1] != ''):
            bank = content[0]
            currency = content[1]
            code = content[2]
            currencyUnit = content[3]
            cenPrice = self.strToFloat(content[4])
            remittanceBuyPrice = self.strToFloat(content[5])
            sellPrice = self.strToFloat(content[6])
            cashBuyPrice = self.strToFloat(content[7])
            sellPrice2 = self.strToFloat(content[8])
            releasedate = content[9]
            sql = "INSERT INTO exchange_rate(bank, currency, code, currencyUnit, cenPrice, remittanceBuyPrice, sellPrice, cashBuyPrice, sellPrice2, releasedate) VALUES('%s','%s','%s','%s','%f','%f','%f','%f','%f','%s') " % (bank,currency,code,currencyUnit,cenPrice,remittanceBuyPrice,sellPrice,cashBuyPrice,sellPrice2,releasedate)
            cursor.execute(sql)
            conn.commit()

    #查询指定银行指定货币汇率的更新时间
    def queryTime(self,bank,currency,conn):
        cursor = conn.cursor()
        sql = "SELECT * FROM updateTime WHERE bank='%s' AND currency='%s'" % (bank, currency)
        cursor.execute(sql)
        result = cursor.fetchall()
        releasedate = ''
        for row in result:
             releasedate = row[2]
        return releasedate

    #更新指定银行指定货币汇率的更新时间
    def updateTime(self,bank,currency,date,conn):
        cursor = conn.cursor()
        sql = "INSERT INTO updateTime(bank, currency, lastreleasedate) VALUES('%s','%s','%s') " % (bank,currency,date)
        cursor.execute(sql)
        conn.commit()

    #将获取的数组进行分条操作
    def splitAndStore(self,contents,conn):
        for content in contents:
            #查看是否是第一次执行程序
            try:
                date = self.queryTime(content[0],content[1],conn)
                if(date != content[9]):
                    self.updateTime(content[0],content[1],content[9],conn)
                    self.saveData(content,conn)
            except:
                self.updateTime(content[0],content[1],content[9],conn)
                self.saveData(content,conn)

    #读取网页内容并使用正则表达式进行提取,并返回数据
    def readHtml(self):
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
        condition = "{bank:'(.*?)',currency:'(.*?)',code:'(.*?)',currencyUnit:'(.*?)',cenPrice:'(.*?)',buyPrice1:'(.*?)',sellPrice1:'(.*?)',buyPrice2:'(.*?)',sellPrice2:'(.*?)',releasedate:'(.*?)'}"
        contents = re.findall(condition,html,re.S)
        return contents

    # 根据传入数据建立连接
    def makeConnectionToMySQL(self,host,user,passwd,dbname,charset):
        conn = MySQLdb.connect(host=host, user=user ,passwd=passwd, db=dbname, charset=charset)
        return conn
