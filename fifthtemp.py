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
def getTemp():

    addr = address.queryIpAddress(address.get_ip())
    code = city.queryCode(addr)
    url = "https://weather.com/zh-CN/weather/5day/l/"+code
    respFive=urllib.urlopen(url);
    
    soupFive=BeautifulSoup(respFive,'html.parser');
    
    # 最近五天
    fives=soupFive.find_all('tr',attrs={'class':'clickable'});
    tempToday=fives[4].find('td',attrs={'class':'temp'}).find_all('span');
    return tempToday[0].get_text()+" / "+tempToday[2].get_text();