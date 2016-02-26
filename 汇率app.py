#coding:utf-8
import urllib2
# respose = urllib2.urlopen('http://forex.hexun.com/rmbhl/')
# html = respose.read()
# print(html)

# import urllib.request

# url = 'http://forex.hexun.com/rmbhl/#zkRate'
# req = urllib.request.Request(url, headers = {
#     'Connection': 'Keep-Alive',
#     'Accept': 'text/html, application/xhtml+xml, */*',
#     'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko'
# })
# oper = urllib.request.urlopen(req)
# data = oper.read()
# print(data.decode())


request = urllib2.Request('http://data.bank.hexun.com/other/cms/foreignexchangejson.ashx?callback=ShowDatalist',data=None,headers = {
    'Connection': 'Keep-Alive',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4',
    'Cookie':'vjuids=-33daed2da.152fe7ce078.0.41c5eb1c; vjlast=1455968543.1456497069.13; HexunTrack=SID=2016022019423407476fdfcb307fe4b3abfa46be4d178e670&CITY=41&TOWN=410100',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36'
})
# request.add_header('User-Agent','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36')
response = urllib2.urlopen(request)
html = response.read()
html = html.decode('gb2312','ignore').encode('utf-8')
print(html)
