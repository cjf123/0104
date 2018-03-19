#__author__:Administrator
#date:2016/12/22

import requests
from bs4 import BeautifulSoup
# from bs4.element import Tag

# 爬虫自动获取标题

def get_url(url):
    try:
        response = requests.get(url=url) # 访问获取url
        response.encoding = 'utf-8'
        soup = BeautifulSoup(response.text, features="lxml")
        tag = soup.find(name='title') # 获取title标签
        title = tag.text
        return title
    except Exception as e:
        pass


