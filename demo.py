#!/usr/bin/env python
#-*- coding: UTF-8 -*-  
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
sys.path.append('/Users/dingyang/python/')
from geektool import fifthdate
from geektool import fifthdes
from geektool import fifthtemp
from geektool import fifthweek

if __name__ == '__main__':
	print(fifthdate.getDate())
	print(fifthdes.getDes())
	print(fifthtemp.getTemp())
	print(fifthweek.getWeek())