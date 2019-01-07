#!/usr/bin/env python
#-*- coding: UTF-8 -*-  
import sys
reload(sys)
import os
sys.setdefaultencoding('utf-8')
sys.path.append('/Users/dingyang/python/')
import requests
import zipfile
import shutil
from geektool import fifthdate
from geektool import fifthdes
from geektool import fifthtemp
from geektool import fifthweek


def unzip_file(zip_src, dst_dir):
    r = zipfile.is_zipfile(zip_src)
    if r:     
        fz = zipfile.ZipFile(zip_src, 'r')
        # for file in fz.namelist():
        fz.extractall(dst_dir)       
    else:
		print('This is not zip')

if __name__ == '__main__':
	# print(fifthdate.getDate())
	# print(fifthdes.getDes())
	# print(fifthtemp.getTemp())
	# print(fifthweek.getWeek())
	res = requests.get('https://github.com/lovexinforever/geektool/archive/master.zip')
	res.raise_for_status()
	# print(res)
	playFile = open('/tmp/geektool.zip', 'wb')
	for chunk in res.iter_content(100000):
		playFile.write(chunk)
	playFile.close()
	os.system('rm -rf /tmp/geektool-master')
	os.system('rm -rf /tmp/geektool')
	unzip_file('/tmp/geektool.zip', '/tmp')
	
	shutil.move('/tmp/geektool-master', '/tmp/geektool')
