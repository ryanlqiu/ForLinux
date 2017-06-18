import urllib.request
import re
import chardet

def GetHtml(url):
    page=urllib.request.urlopen(url)
    html=page.read()
    return html

def GetImage(html):

    reg = r'src="(.+?\.jpg)"'#若不加（）则 结果中含有 src字母 后续读取会出现问题,  +?为Python的非贪婪模式，尽可能匹配少的字符串
    imgre=re.compile(reg)
    print("正则表达式:",imgre)
    encode_type = chardet.detect(html)
    html = html.decode(encode_type['encoding'])
    print("样本",html)
    imglist=re.findall(imgre,html)
    print("结果：",imglist)
    x = 0
    for imgurl in imglist:
        urllib.request.urlretrieve(imgurl,"%s.jpg"%x)
        x=x+1
    return  imglist
html=GetHtml("http://www.mm131.com/xinggan/2291.html")
GetImage(html)