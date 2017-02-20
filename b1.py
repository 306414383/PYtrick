from bs4 import BeautifulSoup
import requests
import urllib
import os
kwz=0
fk=0
for x in range(83791,83792):
	x = 61473
	web_data=requests.get('http://www.mzitu.com/'+str(x))
	print(x,fk)
	#web_data=requests.get("http://jecvay.com")
	soup = BeautifulSoup(web_data.text,'lxml')
	my_girl = soup.select('body > div.main > div.content > div.main-image > p > a > img')
	print(my_girl)
	for my_girl in my_girl:
		image_url=my_girl.get('src').split('net')[1].split('01.')[0]
		print(image_url)
	lists=my_girl.get('alt')
	if lists[0]<='9' and lists[0]>='0' :
		continue
	fk=fk+1
	path_name='C://Users/li bo/Desktop/nowMM/{}'.format(lists)
	isExists = os.path.exists(path_name)
	if not isExists:
	    print("[*]偷偷新建了名字叫做" + path_name + "的文件夹")
	    os.mkdir(path_name)
	else:
	    # 如果目录存在则不创建，并提示目录已存在
	    print("[+]名为" + path_name + '的文件夹已经创建成功')
	url='http://i.meizitu.net/'+image_url
	try:
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
			imgnr = linkk.read() 

			with open(path_name+'/'+filename+fileext,'wb') as code:    #按照文件名+扩展名的格式保存内容到要保存的本机文件夹
				code.write(imgnr)
	except Exception:
		print('[!]')
