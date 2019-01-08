#!/usr/bin/env python
#-*- coding: UTF-8 -*-  
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
sys.path.append('/tmp/')
from geektool import address
from geektool import city
from geektool import icon
import urllib
import os
from bs4 import BeautifulSoup
import re
def getDes():
    addr = address.queryIpAddress(address.get_ip())
    code = city.queryCode(addr)
    url = "https://weather.com/zh-CN/weather/today/l/"+code
    respFive=urllib.urlopen(url);
    soup=BeautifulSoup(respFive,'html.parser');
    tagToday=soup.find('div',attrs={'class':'today_nowcard-phrase'})
    urllib.urlretrieve(icon.queryIcon(tagToday.get_text()), '/tmp/weather.png')
    return tagToday.get_text()