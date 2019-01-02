#!/usr/bin/env python
#-*- coding: UTF-8 -*-  
import sys
sys.setdefaultencoding('utf-8')
sys.path.append('/Users/dingyang/python/')
from geektool import address
from geektool import city
import urllib
import os
from bs4 import BeautifulSoup
import re

def getTemp():
    addr = address.queryIpAddress(address.get_ip())
    code = city.queryCode(addr)
    url = "https://weather.com/zh-CN/weather/today/l/"+code
    respFive=urllib.urlopen(url);
    soup=BeautifulSoup(respFive,'html.parser');
    tagToday=soup.find('div',attrs={'class':'today_nowcard-temp'})
    return tagToday.span.get_text()