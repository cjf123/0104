from django.test import TestCase

# Create your tests here.

# 测试模块

'''
import urllib.request
from bs4 import BeautifulSoup

# 爬取直播吧新闻
url = "http://news.zhibo8.cc/zuqiu/"


def __getPage(url):
    print("now crawler coming")
    page = urllib.request.urlopen(url)
    if page.getcode() != 200:
        return None
    data = page.read()
    return data


def __writeToFile(data):
    f = open("/static", "w")
    f.write(data)
    f.flush()
    f.close()


def __htmlParser(data):
    soup = BeautifulSoup(data, "html.parser")
    title = soup.find("div", attrs={'class': 'topleftbox'}).find_all("a")
    return title


def __showHtml(title):
    # print(title)
    if title is None:
        return 'Error'
    html = open("qiu.html", "w")
    html.write("<html>")
    html.write("<body>")
    html.write("<div>")
    for data in title:
        html.write("</br>%s" % data)
    html.write("</div>")
    html.write("</body>")
    html.write("</html>")
    html.close()


if __name__ == '__main__':
    pageHtml = __getPage(url)
    title = __htmlParser(pageHtml)
    __showHtml(title)




""""
from django import forms
from django.shortcuts import render
from django.forms import fields
from django.core.exceptions import ValidationError
from app import models

class UserForm(forms.Form):
    name = fields.CharField(label='用户名')
    email = fields.EmailField(label='邮箱')

    # 自定义form验证的规则
    def clean_username(self):

        value = self.changed_data['username']
        if value == 'root':
            return value

        else:
            raise ValidationError('名字错误')


    def clean(self):
        v1 = self.changed_data['username']
        v2 = self.changed_data['email']
        if v1 == 'root' and v2 == 'root@123.com':
            pass
        else:
            raise ValidationError('用户名或密码错误')

        return self.changed_data


def index(request):
    if request.method == "GET":
        obj = UserForm()
        return render(request,'fm.html',{'obj':obj})
    elif request.method == "POST":
        obj = UserForm(request.POST)
        obj.is_valid()
        obj.cleaned_data
        return render(request, 'fm.html', {'obj':obj})



# modelform模块

class UserModelForm(forms.ModelForm):
    class Meta:
        model = models.Comment # 关联的表
        fields = "__all__" # 默认选择所有数据

def mf(request):
    if request.method == "GET":
        obj = UserModelForm()
        return render(request,'mf.html',{'obj':obj})

    elif request.method == "POST":
        obj = UserModelForm(request.POST)
        if obj.is_valid():
            obj.save() # 向数据库中保存数据

        return render(request,'mf.html',{'obj':obj})
"""
'''



