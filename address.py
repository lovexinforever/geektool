#!/usr/bin/env python
# encoding: utf-8
from bs4 import BeautifulSoup
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import urllib2

def queryIpAddress(ipaddress):
    url='https://ip.cn/index.php?ip='+ipaddress
    head={}
    head['User-Agent']='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
    req=urllib2.Request(url,headers=head)
    reaponse = urllib2.urlopen(req);
    soup=BeautifulSoup(reaponse,'html.parser');
    a = soup.find('div', attrs={'class': 'well'})
    b = a.find_all('p')[1].find('code').get_text();
    address = b.split(' ')[0]
    return address

def get_ip():
    url='http://ip.42.pl/raw'
    head={}
    head['User-Agent']='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
    req=urllib2.Request(url,headers=head)
    ip = urllib2.urlopen(req).read();
    return ip