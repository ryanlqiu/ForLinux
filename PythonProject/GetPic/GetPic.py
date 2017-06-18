#code utf-8
import sys,importlib
import urllib.request
import  re
import os
import chardet

os.chdir("F:\\PythonProject\\GetPic")
def GetHtml(url):
    page=urllib.request.urlopen(url)
    html=page.read()
    return html

def GetImage(html):

    reg = 'src="(.+?\.jpg)"'
    imgre=re.compile(reg)
    encode_type = chardet.detect(html)
    html = html.decode(encode_type['encoding'])

    imglist=re.findall(imgre,html)
    x = 0
    for imgurl in imglist:
        urllib.request.urlretrieve(imgurl,"%s.jpg"%x)
        x=x+1
    return  imglist
html=GetHtml("http://www.ivsky.com/bizhi/dream_of_three_ancient_kingdoms_2_v41855/")
print(GetImage(html))