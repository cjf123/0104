#__author__:Administrator
#date:2017/2/26
from django.shortcuts import render,HttpResponse,redirect
from app import models
import json

def user(request,user_id):

    '''用户后台数据，默认后端显示收藏数据'''
    # userid = request.GET.get()
    # 通过user_id 即为用户ＩＤ去数据库中去匹配收藏的新闻
    # a = models.UserInfo.objects.filter(nid=user_id).values('username')
    user_name = models.UserInfo.objects.filter(nid=user_id).values('username')[0] # 用户名
    fabu_num = models.News.objects.filter(user=user_id).count() # 发布

    news_shoucang = models.News.objects.filter(user=user_id).all() # 一对多表查询通过用户id查询关联的所有新闻

    news_id = models.Collection.objects.filter(user=user_id).values('news_id') # 收藏的新闻
    shoucang_num = '0'
    for k in news_id:
        news_fb = models.News.objects.filter(id=k['news_id']).all()
        news_fb = news_fb
        shoucang_num = models.News.objects.filter(id=k['news_id']).count()
        shoucang_num = shoucang_num

    return render(request,'background/user.html', {'news_list': news_shoucang,
                                                   'shoucang_num':shoucang_num,
                                                   'news_shoucang': news_fb,
                                                   'fabu_num':fabu_num,
                                                   'user_name':user_name['username']
                                                   })

def banji(request):
    '''用户编辑信息返回页面'''

    return render(request,'background/banji.html')

def btn_user(request):
    '''修改用户信息'''

    if request.method =='POST':
        user_id = request.session.get('user_id') # 获取到用户的id
        user_name = request.POST.get('user_name')
        user_email = request.POST.get('user_email')
        if not user_name:
            models.UserInfo.objects.filter(nid=user_id).update(
                                                    email=user_email,
                                                    )
        if not user_email:
            models.UserInfo.objects.filter(nid=user_id).update(
                                                    username=user_name
                                                    )
        if not user_name and not user_email:
            return
        if user_email and user_name:
            models.UserInfo.objects.filter(nid=user_id).update(
                username=user_name,
                email=user_email,
            )

        return HttpResponse(json.dumps('修改成功'))

def btn_pwd(request):
    '''修改个人密码'''
    ret = {'status':False,'message':None}
    if request.method == 'POST':
        user_id = request.session.get('user_id')  # 获取到用户的id
        p1 = request.POST.get('p1') # 用户原先密码
        p2 = request.POST.get('p2') # 用户新密码
        p3 = request.POST.get('p3') # 用户确认新密码
        user_pwd = models.UserInfo.objects.filter(nid=user_id).values('password')[0]
        if p1 == user_pwd['password']:
            if p2 == p3:
                models.UserInfo.objects.filter(nid=user_id).update(password=p2)
                ret['status'] = True
                ret['message'] = '密码修改成功'
            else:
                ret['message'] = '两次输入密码不正确'
        else:
            ret['message'] = '用户密码和原先密码不匹配，请重新输入'

        return HttpResponse(json.dumps(ret))


# 返回一条信息的详细信息
def check_content(request, nid):
    cls_list = models.News.objects.filter(id=int(nid)).all()
    return render(request, "login_reg.html",
                  {'cls_list': cls_list}
                  )