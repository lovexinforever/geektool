# encoding=utf8
def getUrl(des):
    url=''
    if "晴朗" == des or "大部地区晴朗" == des:
		url='https://raw.githubusercontent.com/lovexinforever/blog_back_up/master/blog_photos/20101027235021742.png';
    elif "局部多云" == des or "局部多云/有风" == des:
        url='https://raw.githubusercontent.com/lovexinforever/blog_back_up/master/blog_photos/20101027235020501.png';
    elif "大部多云" == des:
		url='https://raw.githubusercontent.com/lovexinforever/blog_back_up/master/blog_photos/20101027235019364.png';
    elif "小雨" == des:
		url='https://raw.githubusercontent.com/lovexinforever/blog_back_up/master/blog_photos/20101027235021677.png';
    elif "多云" == des or "大部分地区多云" == des:
		url="https://raw.githubusercontent.com/lovexinforever/blog_back_up/master/blog_photos/20101027235021422.png";
    elif "雨" == des:
		url="https://raw.githubusercontent.com/lovexinforever/blog_back_up/master/blog_photos/20101027235021502.png";
    elif "小阵雨" == des or "阵雨" == des or "大阵雨" == des or "雷雨" == des or "周围有阵雨" == des or "下午有阵雨" == des or "上午有阵雨" == des:
		url="https://raw.githubusercontent.com/lovexinforever/blog_back_up/master/blog_photos/20101027235021411.png";
    elif "小阵雪" == des or "下午有阵雪" == des or "阵雪" == des:
		url="https://raw.githubusercontent.com/lovexinforever/blog_back_up/master/blog_photos/20101027235021677.png";
    else:
		url='https://raw.githubusercontent.com/lovexinforever/blog_back_up/master/blog_photos/20101027235020136.png';
    return url