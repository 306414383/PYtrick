from bs4 import BeautifulSoup
import requests
import urllib
import os

def get_mei_channel(url):
    web_data=requests.get(url)
    soup=BeautifulSoup(web_data.text,'lxml')
    channel=soup.select('body > div.main-content > div.postlist > ul >  li > a')
    for list in channel:
        print(list.get('href'))
#获取妹子图首页热门专题的链接
start_url="http://www.mzitu.com/"
get_mei_channel(start_url)