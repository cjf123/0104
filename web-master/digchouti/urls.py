"""digchouti URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from app.views import comment,home,background

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^search', home.search), # 主页面URL
    url(r'^login', comment.login),  # 登陆URL
    url(r'^register', comment.register),  # 注册URL
    url(r'^send_msg', comment.send_msg),  # 邮箱验证URL
    url(r'^logout', comment.logout), # 退出URL
    url(r'^check_code', comment.check_code), # 验证码URL
    url(r'^key', comment.search_key), # 搜索新闻
    url(r'^test', home.test), # 测试

    url(r'^release', home.release), # 发布分享链接
    url(r'^h2', home.release_h2), # 发布文字

    url(r'^tb2', home.tb2), # 42区
    url(r'^tb3', home.tb3), # 段子
    url(r'^tb4', home.tb4), # 图片
    url(r'^tb5', home.tb5), # 挨踢
    url(r'^tb6', home.tb6), # 你问我答

    url(r'^dianzan', home.dianzan), # 点赞
    url(r'^pinglun', home.pinglun), # 评论
    url(r'^shoucang', home.shoucang), # 收藏
    url(r'^huifu_p', home.huifu_p), # 回复评论
    url(r'^upload_image', home.upload_image), # 上传图片
    url(r'^getTitle', home.getTitle),  # 获取标题信息，爬虫
    url(r'^user/(\d+)', background.user), # 用户信息
    url(r'^banji', background.banji), # 用户编辑个人信息页面
    url(r'^btn_user', background.btn_user), # 修改用户基本信息进入后台数据库修改
    url(r'^btn_pwd', background.btn_pwd), # 修改个人密码

    url(r'^content/menu/(\d+)', background.check_content), # 查看详细内容





]
