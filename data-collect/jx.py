#!/usr/bin/env python
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
from urllib.request import urlopen
tablestr ="""
<table style="border-collapse:collapse;">
<caption class="tcaption">「0003」数字数理测算分析结果</caption>
<tr>
<td class="ttext"><b style="color:red;font-size:16px;">0003</b></td>
<td class="ttext">〖<b style="color:red;font-size:16px;">吉</b>〗</td>
</tr>
<tr>
<td class="ttext" colspan="2"><span style="font-size:14px;"><b>谒语</b>：根深蒂固，蒸蒸日上，如意吉祥，百事顺遂。</span>
</td>
</tr>
<tr>
<td class="ttext lft" colspan="2">
<div style="padding:0 20px 20px 20px">
<p></p>
<p><b>古代说法</b><br/>
	　◇说法一：立身出世，有贵人助，天赐吉祥，四海名扬，然过急则反。<br/>
	　◇说法二：（吉祥）进取如意的增进繁荣数。<br/>
	　◇说法三：进取如意的增进繁荣数，成功发达之兆，名利双全。<br/>
</p>
<p><b>现代诠释</b><br/>
	　◇释意一：进取如意又富贵，智达明敏扬名威，名利寿福皆此得前途光明好鸿图。<br/>
	　◇释意二：为进取之数，阴阳相合，万物成形确定之象。名利之表徵。有天赋之富贵。并得扬高名。且有子孙之福。智慧敏达。心广体胖。足有领导能力。能建伟大事业。实前途无限之大吉祥也 。<br/>
	　◇释意三：阴阳抱合，万物确定形成之象，有吉祥、 成功发达之兆。智达明敏，艺精工巧有首领之资， 自然之福。名利双全能成人事业，荣进有望，福祉无穷。<br/>
</p>
<p><b>暗示个性</b><br/>
	　◇因网上有关个性暗示的解释太荒唐，故不列出。
	</p></div>
</td>
</tr>
</table>
"""
def readpage(url):
    # if has Chinese, apply decode()
    html = urlopen(url).read().decode('utf-8')
    soup = BeautifulSoup(html, 'html.parser')
    col = {}
    tb = soup.select("#mainbg > div:nth-child(2) > table")[0]
    ttexts = soup.select(".ttext")
    print(ttexts)
    return tb

def parserall():
    jxurl = "https://www.123cha.com/jx/{:0>4d}"
    for i in range(1, 81):
        url = jxurl.format(i)
        # print(url)
        # readpage(url)
        break


def parserstr(soup):
    ttexts = soup.select(".ttext")
    col ={}
    col['num'] = int(ttexts[0].text)
    col['jx'] = ttexts[1].text
    col['jieyu'] = ttexts[2].text.strip().replace('谒语：','')
    shuafa = ttexts[3].div
    col['shuafa'] = ttexts[3].div
    
    print(col)

def main():
    parserstr(BeautifulSoup(tablestr, 'html.parser'))
    print("-end-")


def _time_analyze_(func):
    import time
    t1_start = time.perf_counter()
    func()
    t1_stop = time.perf_counter()
    print(func.__name__)
    print("Elapsed time: %s s" % (t1_stop - t1_start))


if __name__ == '__main__':
    _time_analyze_(main)
