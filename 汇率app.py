__author__ = 'terry'
#code = utf8#
import urllib2
respose = urllib2.urlopen('http://forex.hexun.com/rmbhl/#zkRate')
html = respose.read()
print(html)
