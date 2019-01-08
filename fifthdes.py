#!/usr/bin/env python
# encoding=utf8
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
    url = "https://weather.com/zh-CN/weather/5day/l/"+code
    respFive=urllib.urlopen(url);
    
    soupFive=BeautifulSoup(respFive,'html.parser');
    
    # 最近五天
    fives=soupFive.find_all('tr',attrs={'class':'clickable'});
    tagToday=fives[4].find('td',attrs={'class':'description'});
        
    urllib.urlretrieve(icon.queryIcon(tagToday.get_text()), '/tmp/fiveFour.png')
    return tagToday.get_text();
