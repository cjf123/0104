#__author__:Administrator
#date:2016/12/22


from django import forms
import re
from django.core.exceptions import ValidationError


def mobile_validate(value):
    '''
    自定义验证手机号的样式
    :param value:
    :return:
    '''
    mobile_re = re.compile(r'^(13[0-9]|15[012356789]|17[678]|18[0-9]|14[57])[0-9]{8}$')
    if not mobile_re.match(value):
        raise ValidationError('手机号码格式错误')

class SendMsgForm(forms.Form):

    email = forms.EmailField(error_messages={'required': '邮箱不能为空','invalid': '邮箱格式不正确'})


class RegisterForm(forms.Form):
    username = forms.CharField(error_messages={'required': '用户名不能为空'})
    email = forms.EmailField(error_messages={'required': '邮箱不能为空', 'invalid': '邮箱格式不正确'})
    password = forms.CharField(error_messages={'required': '密码不能为空'})
    email_code = forms.CharField(error_messages={'required': '验证码不能为空'})


class LoginForm(forms.Form):
    user = forms.CharField(error_messages={'required': '用户名不能为空'})
    pwd = forms.CharField(error_messages={'required': '密码不能为空'})
    code = forms.CharField(error_messages={'required': '验证码不能为空'})
