#!/usr/bin/env python
#-*- coding: UTF-8 -*-  
import sys
reload(sys)
import os
sys.setdefaultencoding('utf-8')
# sys.path.append('/Users/dingyang/python/')
import urllib2
import zipfile
import shutil
# from geektool import fifthdate
# from geektool import fifthdes
# from geektool import fifthtemp
# from geektool import fifthweek


def unzip_file(zip_src, dst_dir):
    r = zipfile.is_zipfile(zip_src)
    if r:     
        fz = zipfile.ZipFile(zip_src, 'r')
        fz.extractall(dst_dir)       
    else:
		print('This is not zip')

if __name__ == '__main__':
	# print(fifthdate.getDate())
	# print(fifthdes.getDes())
	# print(fifthtemp.getTemp())
	# print(fifthweek.getWeek())
	res = urllib2.urlopen('https://github.com/lovexinforever/geektool/archive/master.zip')
	data = res.read() 
	with open("geektool.zip", "wb") as code:
		code.write(data)
	os.system('rm -rf /tmp/geektool-master')
	os.system('rm -rf /tmp/geektool')
	unzip_file('/tmp/geektool.zip', '/tmp')
	
	shutil.move('/tmp/geektool-master', '/tmp/geektool')