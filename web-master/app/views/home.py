#__author__:Administrator
#date:2016/12/22

from django.shortcuts import render,HttpResponse,redirect
from app import models
from app.utils.pager import PagerHelper
import datetime,time
from django.db.models import F
import os
import json
from app.utils import response
from app.forms import home

def search(request):
    '''
    第一次访问时的主路径
    :param request:
    :return:
    '''
    now_time = datetime.datetime.now()

    current_page = request.GET.get('p', 1) # 默认值是一 p是传过来的值

    current_page = int(current_page)
    # 从数据库中取到所有数据的个数
    total_count = models.News.objects.all().count()

    obj = PagerHelper(total_count, current_page, '/search.html',8) # 每页显示的个数
    pager = obj.pager_str()
    cls_list = models.News.objects.all()[obj.db_start:obj.db_end]

    return render(request, "login_reg.html",
                  {'cls_list': cls_list, 'str_pager': pager})


# 发布提交后台数据
def release(request):
    '''
    发布向数据库中写入数据
    :param request:
    :return:
    '''

    dic_time = datetime.datetime.now()
    dic_url = request.POST.get('url')
    dic_title = request.POST.get('title')  # 新闻标题
    dic_connent = request.POST.get('connent') # 新闻内容
    dic_inner = (request.POST.get('to_where'))
    if dic_inner == "42区":
        dic_nt = 1
    if dic_inner == "段子":
        dic_nt = 2
    if dic_inner == "图片":
        dic_nt = 3
    if dic_inner == "挨踢1024":
        dic_nt = 4
    if dic_inner == "你问我答":
        dic_nt = 5

    dic_user_id = request.POST.get('user_id')
    print(dic_connent)

    models.News.objects.create(
        title=dic_title,
        summary=dic_connent,
        url=dic_url,
        ctime=dic_time,
        nt=dic_nt,
        user_id=dic_user_id
    )
    return HttpResponse('/login_reg.html')



def release_h2(request):
    '''
    发布向数据库中写入数据
    :param request:
    :return:
    '''
    print('OK')

    dic_time = datetime.datetime.now()
    # dic_url = request.POST.get('url')
    # dic_title = request.POST.get('title')  # 新闻标题
    dic_connent = request.POST.get('connent') # 新闻内容
    dic_inner = (request.POST.get('to_where'))
    if dic_inner == "42区":
        dic_nt = 1
    if dic_inner == "段子":
        dic_nt = 2
    if dic_inner == "图片":
        dic_nt = 3
    if dic_inner == "挨踢1024":
        dic_nt = 4
    if dic_inner == "你问我答":
        dic_nt = 5

    dic_user_id = request.POST.get('user_id')
    print(dic_connent,dic_inner)


    models.News.objects.create(
        # title=dic_title,
        summary=dic_connent,
        # url=dic_url,
        ctime=dic_time,
        nt=dic_nt,
        user_id=dic_user_id
    )
    return HttpResponse('/login_reg.html')









def dianzan(request):
    if request.method == 'POST':
        user_id = request.session.get('user_id') # 用户ID

        nid = request.POST.get('user')

        # 通过对对多关联表判断该用户是不是点过赞，如果点过就做减1操作，否则做加1操作
        obj = models.News.objects.get(id=nid)
        num = obj.favor.filter(nid=user_id).count()
        if num:
            models.News.objects.filter(id=nid).update(favor_count=F('favor_count') - 1)
            obj.favor.remove(user_id)
            minus_code = response.StatusCodeEnum.FavorMinus  # 做减1的状态码
            dic = {'status_code':minus_code,'status':False}
            return HttpResponse(json.dumps(dic))

        else:
            models.News.objects.filter(id=nid).update(favor_count=F('favor_count') + 1)
            obj.favor.add(user_id)
            plus_code = response.StatusCodeEnum.FavorPlus
            dic = {'status_code': plus_code, 'status': True}
            return HttpResponse(json.dumps(dic))


# 评论
def pinglun(request):

    new_id = request.GET.get('new_id') # 获得新闻ID

    comm = models.Comment.objects.filter(news_id=new_id).values('id','content','device','user_id','user__username','news_id','parent_comment_id')
    # count = models.Comment.objects.filter(news_id=new_id).count() # 评论个数
    comm_list = []  # 从数据库中去除存到的列表
    for i in comm:
        comm_list.append(i)

    comment_tree = []
    comment_list_dict = {}
    for row in comm_list:
        row.update({'children': []})  # 对每一个对象加上一个空的{'children': []}
        comment_list_dict[row['id']] = row  # 生成一个键值对，每个键即为每个对象的id

    for item in comm_list:
        parent_row = comment_list_dict.get(item['parent_comment_id'])  # 每个父级对象，没有没None
        if not parent_row:
            comment_tree.append(item)
        else:
            parent_row['children'].append(item)

    return HttpResponse(json.dumps(comment_tree))

# 回复评论
def huifu_p(request):

    if request.method == "POST":

        content = request.POST.get('val') # 获取自己写的内容
        partnet_user = request.POST.get('partnet_user') # 评论的父级用户名，如果为空，则表示评论的是根评论
        partnet_comment = request.POST.get('partent_comment') # 父级评论的内容
        user_id = request.POST.get('user_id')  # 当前用户ID
        new_id = request.POST.get('new_id')  # 当前新闻ID
        if partnet_comment:
            partnet_comment_id = models.Comment.objects.filter(content=partnet_comment).values('id')[0]
            partnet_comment_id = partnet_comment_id['id']


        if partnet_user:
            models.Comment.objects.create(
                content=content,
                news_id=new_id,
                user_id=user_id,
                parent_comment_id=partnet_comment_id
            )

        else:

            models.Comment.objects.create(
                content=content,
                news_id=new_id,
                user_id=user_id
            )
    count = models.Comment.objects.all().count()

    return HttpResponse(json.dumps(count))

# 收藏
def shoucang(request):
    if request.method == 'POST':
        user_id = request.session.get('user_id')
        new_id = request.POST.get('nid')
        models.Collection.objects.create(user_id=user_id,news_id=new_id)
        return HttpResponse(json.dumps('收藏成功'))



def upload_image(request):
    '''
    上传图片
    :param request:
    :return:
    '''

    if request.method == "POST":
        img = request.POST.get('img') # 获取图片的名字
        # print(img)
        obj = request.FILES.get('img') # 获取图片的对象

        file_path = os.path.join('static', 'imgs', obj.name) # 将图片保存到本地
        f = open(file_path,'wb')
        for i in obj.chunks():
            f.write(i)
        f.close()   # 将图片存放到本地
        ret = {'status': True, 'path': file_path}  # 返回给iform，前端就接收到了path和status
        return HttpResponse(json.dumps(ret))


# 获取标题
def getTitle(request):
    '''
    自动获取标题返回前端
    :param request:
    :return:
    '''
    if request.method == "POST":

        url = request.POST.get('URL')
        # print(url)
        title = home.get_url(url)
        # print(title)
        ret = {'title':title}
        return HttpResponse(json.dumps(ret))


def tb(dic_inner):
    if dic_inner == "42区":
        dic_nt = 1
    if dic_inner == "段子":
        dic_nt = 2
    if dic_inner == "图片":
        dic_nt = 3
    if dic_inner == "挨踢1024":
        dic_nt = 4
    if dic_inner == "你问我答":
        dic_nt = 5
    return dic_nt

# 标头搜索
def tb2(request):

    if request.method =='GET':
        Tb = request.GET.get('42','42区')
        dic_nt = tb(Tb)

        current_page = request.GET.get('p', 1)  # 默认值是一 p是传过来的值
        current_page = int(current_page)
        # 从数据库中取到所有数据的个数
        total_count = models.News.objects.all().count()
        obj = PagerHelper(total_count, current_page, '/search.html',8)  # 每页显示的个数
        pager = obj.pager_str()

        cls_list = models.News.objects.filter(nt=dic_nt).all()
        return render(request, "login_reg.html",
                      {'cls_list': cls_list,'str_pager': pager}
                      )

def tb3(request):
    if request.method =='GET':
        Tb = request.GET.get('duanzi','段子')
        dic_nt = tb(Tb)
        cls_list = models.News.objects.filter(nt=dic_nt).all()
        return render(request, "login_reg.html",
                      {'cls_list': cls_list}
                      )
def tb4(request):
    if request.method =='GET':
        Tb = request.GET.get('tupian','图片')
        dic_nt = tb(Tb)
        cls_list = models.News.objects.filter(nt=dic_nt).all()
        return render(request, "login_reg.html",
                      {'cls_list': cls_list}
                      )
def tb5(request):
    if request.method == 'GET':
        Tb = request.GET.get('aiti', '挨踢1024')
        dic_nt = tb(Tb)
        cls_list = models.News.objects.filter(nt=dic_nt).all()
        return render(request, "login_reg.html",
                      {'cls_list': cls_list}
                      )
def tb6(request):
    if request.method == 'GET':
        Tb = request.GET.get('niwen', '你问我答')
        dic_nt = tb(Tb)
        cls_list = models.News.objects.filter(nt=dic_nt).all()
        return render(request, "login_reg.html",
                      {'cls_list': cls_list}
                      )






def test(request):
    '''
    测试点赞的效果
    :param request:
    :return:
    '''
    return render(request,'test.html')