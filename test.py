#coding:utf-8
import urllib2
import cookielib
import re


url = 'http://data.bank.hexun.com/other/cms/foreignexchangejson.ashx?callback=ShowDatalist'
# url = 'https://www.baidu.com'
cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
opener.addheaders = [('User-Agent','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36')]
urllib2.install_opener(opener)
res = urllib2.urlopen(url)
cookie = ''

for index, co in enumerate(cj):
    cookie = co.name + '=' + co.value
    
request = urllib2.Request('http://data.bank.hexun.com/other/cms/foreignexchangejson.ashx?callback=ShowDatalist',data=None,headers = {
    'Connection': 'Keep-Alive',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4',
    'Cookie': cookie,
    # 'Cookie':'vjuids=-33daed2da.152fe7ce078.0.41c5eb1c; vjlast=1455968543.1456497069.13; HexunTrack=SID=2016022019423407476fdfcb307fe4b3abfa46be4d178e670&CITY=41&TOWN=410100',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36'
})

response = urllib2.urlopen(request)
html = response.read()
html = html.decode('gb2312','ignore').encode('utf-8')
condition = "{bank:'(.*?)',currency:'(.*?)',code:'(.*?)',currencyUnit:'(.*?)',cenPrice:'(.*?)',buyPrice1:'(.*?)',sellPrice1:'(.*?)',buyPrice2:'(.*?)',sellPrice2:'(.*?)',releasedate:'(.*?) (.*?)'}"
contents = re.findall(condition,html,re.S)
print contents