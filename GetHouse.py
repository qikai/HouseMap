# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import requests
import csv
import importlib
import time
import random
import sys
importlib.reload(sys)

#url = 'https://bj.lianjia.com/ershoufang/pg{page}/'
url = 'https://bj.lianjia.com/ershoufang/pg{page}ea20000bp220ep250/'

page = 0

hds=[{'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'},\
    {'User-Agent':'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.12 Safari/535.11'},\
    {'User-Agent':'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Trident/6.0)'},\
    {'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:34.0) Gecko/20100101 Firefox/34.0'},\
    {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/44.0.2403.89 Chrome/44.0.2403.89 Safari/537.36'},\
    {'User-Agent':'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50'},\
    {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50'},\
    {'User-Agent':'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0'},\
    {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1'},\
    {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1'},\
    {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11'},\
    {'User-Agent':'Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11'},\
    {'User-Agent':'Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11'},\
    {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727; .NET CLR 3.0.30729; .NET CLR 3.5.30729; InfoPath.3; rv:11.0) like Gecko'},\
    {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.75 Safari/537.36'}
     ]
     
headers = {
'Host': "bj.lianjia.com",
'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
'Accept-Encoding': "gzip, deflate, sdch",
'Accept-Language': "zh-CN,zh;q=0.8",
'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.87 Safari/537.36",
'Connection': "keep-alive",
}


csv_file = open('fang.csv','a', encoding='utf8')
csv_write = csv.writer(csv_file, dialect='excel')

while page < 71:
    time.sleep(random.randint(3,8))
    page+=1
    print("正在下载网页：", url.format(page=page))
    response = requests.get(url.format(page=page), headers = headers)
    html = BeautifulSoup(response.content, "html5lib")
    house_list = html.find('ul', {'class', 'sellListContent'}).find_all('div',{'class','info clear'})
    #print(len(house_list))
    if not house_list:
    	break

    for house in house_list:
        house_title = house.find('div',{'class', 'houseInfo'}).get_text()
        house_url = house.find('div',{'class', 'title'}).a['href']
        #house_location = house.find('div',{'class','positionInfo'}).a.text
        house_location = house.find('div',{'class','houseInfo'}).a.text
        house_price = house.find('div',{'class','totalPrice'}).span.text
        csv_write.writerow([house_title,house_location,house_price,house_url])
        #print(house_price)
    
csv_file.close()
