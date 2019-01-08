#!/usr/bin/env python
# encoding=utf8
import json
import sys

def queryIcon(key):
    f = open("/tmp/geektool/icon.json")
    origin = json.load(f);
    if(key in origin):
        # 获取 icon url
        icon = origin[key];
    # 如果获取不到,直接给默认
    else:
        icon = "https://raw.githubusercontent.com/lovexinforever/blog_back_up/master/blog_photos/20101027235020136.png"
    print(icon)
    return icon;