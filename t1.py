from bs4 import BeautifulSoup
import requests
import urllib
import os
'''
url='http://www.mzitu.com/71395/42'
html = urllib.request.urlopen(url) 
page=BeautifulSoup(html,'lxml')
src1=page.select('body > div.main > div.content > div.main-image > p > a > img')  
print(src1)
myimg=page.find_all(['img'])
for img in myimg:
'''
url='http://i.meizitu.net/2016/10/26b'
for x in range(80):
#    link = img.get('src')      #获得img地址
    if x < 9: 
        link = url+'0'+str(x+1)+'.jpg'
    else :
        link=url+str(x+1)+'.jpg'
    filepath = os.path.split(link)[1]      #地址分为路径和文件
    #test=os.path.split(link)[0]
    filename = os.path.splitext(filepath)[0]        #文件分为文件名
    fileext = os.path.splitext(filepath)[1]    #和文件扩展名
    print(link,'!',filename,'!',fileext)        #输出观察一下
    linkk = urllib.request.urlopen(link)        #打开img地址
    imgnr = linkk.read()        #读取内容
    with open(u'C://Users/li bo/Desktop/nowMM'+'/'+filename+fileext,'wb') as code:    #按照文件名+扩展名的格式保存内容到要保存的本机文件夹
        code.write(imgnr)
    