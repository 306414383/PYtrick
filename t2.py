from bs4 import BeautifulSoup
import requests
import urllib
import os
def get_mei_channel(url):
    web_data=requests.get(url)
    soup=BeautifulSoup(web_data.text,'lxml')
    channel=soup.select('body > div.main > div.sidebar > div.widgets_hot > span > a')
    for list in channel:
        print(list.get('href'))
#获取妹子图首页热门专题的链接
start_url="http://www.mzitu.com/"
get_mei_channel(start_url)

def get_list_info(url,page,mmpath):
    # url='http://www.mzitu.com/69075'
    web_data=requests.get(url)
    soup=BeautifulSoup(web_data.text,'lxml')
    src=soup.select("body > div.main > div.content > div.main-image > p > a > img")
    for src in src:
        image_url=src.get('src').split('net')[1].split('01.')[0]
    if page < 10:
        pages='0'+str(page)
    else:
        pages =str(page)
    url_split='http://i.meizitu.net'+image_url+'{}.jpg'.format(pages)
    try:
        html = urllib.request.urlopen(url_split)
        name = url_split.split('/')[5].split('.')[0]
        data = html.read()
        fileName ='{}\meizi'.format(mmpath) + name + '.jpg'
        fph = open(fileName, "wb")
        fph.write(data)
        fph.flush()
        fph.close()
    except Exception:
         print('[!]Address Error!!!!!!!!!!!!!!!!!!!!!')


def get_page_from(channel,pages):
    channel=channel+'/page/{}'.format(pages)
    web_data=requests.get(channel)
    soup=BeautifulSoup(web_data.text,'lxml')
    if soup.find('body > div.main > div.main-content > div.currentpath'):
        pass
    else:
        lists = soup.select('#pins > li > span > a')
        for lists in lists:
            #path='E:\MM\{}'.format(lists.get_text())  #源码
            path='C://Users/li bo/Desktop/nowMM/{}'.format(lists.get_text())
            isExists = os.path.exists(path)
            if not isExists:
                print("[*]偷偷新建了名字叫做" + path + "的文件夹")
                os.mkdir(path)
            else:
                # 如果目录存在则不创建，并提示目录已存在
                print("[+]名为" + path + '的文件夹已经创建成功')
            
            for i in range(1,60):
                get_list_info(lists.get('href'),i,path)
            # page_list.insert_one({'url': lists.get('href'), 'title': lists.get_text()})
get_page_from('http://www.mzitu.com/tag/bololi',1)


#获取列表页的详细信息

