# -*- coding:utf-8 -*-
from urllib2 import urlopen as uu
import re
# import tushare as ts

url=["http://fund.eastmoney.com/000051.html",
     "http://fund.eastmoney.com/213008.html",
     "http://fund.eastmoney.com/000173.html",
     "http://fund.eastmoney.com/000477.html"]

find_re = re.compile(r'<div id="statuspzgz" class="fundpz"><span class=".+?">(.+?)</span>',re.DOTALL)
html_re = re.compile(r'http://fund.eastmoney.com/(.+?).html',re.DOTALL) #code
time_re = re.compile(r'<p class="time">(.+?)</p>',re.DOTALL) #update time

for ul in url:
    html=uu(ul).read()
    print(html)
    print "基金代码：" + str(html_re.findall(ul))
    print "单位净值：" + str(find_re.findall(html))        
    print "最后更新时间：" + str(time_re.findall(html))  
    print ''
    break
# raw_input()

