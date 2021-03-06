#!/usr/bin/env python
#-*- coding: UTF-8 -*-  
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
sys.path.append('/tmp/')
from geektool import address
from geektool import city
import urllib
import os
from bs4 import BeautifulSoup
import re

def getDate():
    addr = address.queryIpAddress(address.get_ip())
    code = city.queryCode(addr)
    url = "https://weather.com/zh-CN/weather/5day/l/"+code
    respFive=urllib.urlopen(url);
    
    soupFive=BeautifulSoup(respFive,'html.parser');
    
    # 最近五天
    fives=soupFive.find_all('tr',attrs={'class':'clickable'});
    week=fives[4].find_all('td',attrs={'class':'twc-sticky-col'})[1];

    weekDate=week.find('span',attrs={'class':'day-detail'});
    return weekDate.get_text();