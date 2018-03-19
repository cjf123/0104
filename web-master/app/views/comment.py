from django.shortcuts import render,HttpResponse,redirect

# Create your views here.
import io,datetime
from django import forms
import json,re
from django.db.models import Q
from app.utils.response import BaseResponse
from app.utils import check_code as CheckCode
from app.forms.account import SendMsgForm,RegisterForm,LoginForm
from app import commons
from app.utils import message
from app.utils.pager import PagerHelper

from app import models

def check_code(request):
    """
    获取验证码
    基于pillow模块生成的
    :param request:
    :return:
    """
    stream = io.BytesIO()
    # 创建随机字符 code
    # 创建一张图片格式的字符串，将随机字符串写到图片上
    img, code = CheckCode.create_validate_code()
    img.save(stream, "PNG")
    # 将字符串形式的验证码放在Session中
    request.session["CheckCode"] = code
    return HttpResponse(stream.getvalue())


def logout(request):
    '''
    退出函数
    :param request:
    :return:
    '''

    request.session.clear()
    return redirect('/search.html')


def login(request):
    """
    用户登陆
    :param request:
    :return:
    """
    rep = BaseResponse()
    form = LoginForm(request.POST)
    if form.is_valid():
        _value_dict = form.clean()

        if _value_dict['code'].lower() != request.session["CheckCode"].lower():
            rep.message = {'code': [{'message': '验证码错误'}]}
            return HttpResponse(json.dumps(rep.__dict__))
        # 验证码正确

        # Q查询判断只要邮箱和用户名输一种即可
        con = Q()
        q1 = Q()
        q1.connector = 'AND'
        q1.children.append(('email', _value_dict['user']))
        q1.children.append(('password', _value_dict['pwd']))

        q2 = Q()
        q2.connector = 'AND'
        q2.children.append(('username', _value_dict['user']))
        q2.children.append(('password', _value_dict['pwd']))

        con.add(q1, 'OR')
        con.add(q2, 'OR')

        obj = models.UserInfo.objects.filter(con).first()
        if not obj:
            rep.message = {'user': [{'message': '用户名邮箱或密码错误'}]}
            return HttpResponse(json.dumps(rep.__dict__))

        request.session['is_login'] = True
        request.session['user_id'] = obj.nid
        request.session['user_info'] = {'nid':obj.nid,'email': obj.email, 'username': obj.username}
        rep.status = True
    else:
        error_msg = form.errors.as_json()
        rep.message = json.loads(error_msg)

    return HttpResponse(json.dumps(rep.__dict__))


def register(request):
    '''
    注册
    :param request:
    :return:
    '''
    rep = BaseResponse()
    form = RegisterForm(request.POST)
    if form.is_valid():
        current_date = datetime.datetime.now()  # 获取当前时间
        limit_day = current_date - datetime.timedelta(minutes=1)  # 过期时间
        _value_dict = form.clean()  # 获取用户信息

        is_valid_code = models.SendMsg.objects.filter(email=_value_dict['email'],
                                                      code=_value_dict['email_code'],
                                                      ctime__gt=limit_day).count()
        if not is_valid_code:
            rep.message['email_code'] = '邮箱验证码不正确或过期'
            return HttpResponse(json.dumps(rep.__dict__))

        has_exists_email = models.UserInfo.objects.filter(email=_value_dict['email']).count()

        if has_exists_email:
            rep.message['email'] = '邮箱已经存在'
            return HttpResponse(json.dumps(rep.__dict__))

        has_exists_username = models.UserInfo.objects.filter(username=_value_dict['username']).count()
        if has_exists_username:
            rep.message['email'] = '用户名已经存在'
            return HttpResponse(json.dumps(rep.__dict__))

        _value_dict['ctime'] = current_date
        _value_dict.pop('email_code')
        # 当前用户的所有信息
        obj = models.UserInfo.objects.create(**_value_dict)

        user_info_dict = {'nid': obj.nid, 'email': obj.email, 'username': obj.username}

        models.SendMsg.objects.filter(email=_value_dict['email']).delete()

        request.session['is_login'] = True
        request.session['user_info'] = user_info_dict
        rep.status = True

    else:
        error_msg = form.errors.as_json()
        rep.message = json.loads(error_msg)
    return HttpResponse(json.dumps(rep.__dict__))


def send_msg(request):
    '''
    邮箱验证码函数块
    :param request:
    :return:
    '''
    rep = BaseResponse()
    form = SendMsgForm(request.POST)
    if form.is_valid():
        _value_dict = form.clean()
        email = _value_dict['email']

        has_exists_email = models.UserInfo.objects.filter(email=email).count()

        if has_exists_email:
            rep.summary = "此邮箱已经被注册"
            return HttpResponse(json.dumps(rep.__dict__))

        current_date = datetime.datetime.now()
        code = commons.random_code()

        count = models.SendMsg.objects.filter(email=email).count()

        message.email(email,code) # 调用该函数向邮箱发送验证码


        if not count:
            models.SendMsg.objects.create(code=code, email=email, ctime=current_date)
            rep.status = True
        else:
            limit_day = current_date - datetime.timedelta(hours=1)

            times = models.SendMsg.objects.filter(email=email, ctime__gt=limit_day, times__gt=9).count()
            if times:
                rep.summary = "'已超最大次数（1小时后重试）'"
            else:
                unfreeze = models.SendMsg.objects.filter(email=email, ctime__lt=limit_day).count()
                if unfreeze:
                    models.SendMsg.objects.filter(email=email).update(times=0)

                from django.db.models import F

                models.SendMsg.objects.filter(email=email).update(code=code,
                                                                  ctime=current_date,
                                                                  times=F('times') + 1)
                rep.status = True
    else:
        # error_dict = json.loads(form.errors.as_json())
        # rep.summary = error_dict['email'][0]['message']
        rep.summary = form.errors['email'][0]
    return HttpResponse(json.dumps(rep.__dict__))


def search_key(request):
    '''搜索新闻'''
    # now_time = datetime.datetime.now()
    #
    # current_page = request.GET.get('p', 1)  # 默认值是一 p是传过来的值
    #
    # current_page = int(current_page)
    # # 从数据库中取到所有数据的个数
    # total_count = models.News.objects.all().count()
    #
    # obj = PagerHelper(total_count, current_page, '/key.html', 2)  # 每页显示的个数
    # pager = obj.pager_str()

    if request.method == 'POST':
        key = request.POST.get('key') # 取得关键字进行正则匹配
        # cls_list = models.News.objects.filter(title__contains=key).all()[obj.db_start:obj.db_end]
        cls_list = models.News.objects.filter(title__contains=key).all()

        return render(request, "login_reg.html",
                      {'cls_list': cls_list})
