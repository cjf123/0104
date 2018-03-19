from django.db import models

# Create your models here.


class SendMsg(models.Model):
    '''
    注册生成随机验证码表
    '''
    nid = models.AutoField(primary_key=True)
    code = models.CharField(max_length=6)
    email = models.CharField(max_length=32, db_index=True)
    times = models.IntegerField(default=0)
    ctime = models.DateTimeField()

    def __str__(self):
        return self.nid

    class Meta:
        verbose_name = '随机验证码表'


class UserInfo(models.Model):
    '''
    用户表
    '''
    nid = models.AutoField(primary_key=True)
    username = models.CharField(max_length=32, unique=True,verbose_name='用户名')
    password = models.CharField(max_length=32,verbose_name='密码')
    email = models.CharField(max_length=32, unique=True,verbose_name='邮箱')
    ctime = models.DateTimeField(verbose_name='创建时间')

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = '用户表'


# class NewsType(models.Model):
#     caption = models.CharField(max_length=16)

class News(models.Model):
    '''
    新闻表
    '''
    title = models.CharField(max_length=64, verbose_name='主题') # 新闻主题
    summary = models.CharField(max_length=128,null=True,verbose_name='内容') # 内容
    url = models.URLField(null=True, verbose_name='新闻URL') # 新闻路径
    ctime = models.DateTimeField(auto_now_add=True,verbose_name='创建时间') # 新闻创建时间
    user = models.ForeignKey(to="UserInfo",to_field='nid',related_name='n') # 关联的用户
    news_type_choices = [
        (1, '42区'),
        (2, '段子'),
        (3, '图片'),
        (4, '挨踢1024'),
        (5, '你问我答'),
    ]

    nt = models.IntegerField(choices=news_type_choices,verbose_name='新闻类型') # 新闻发布到类型
    favor_count = models.IntegerField(default=0, verbose_name='点赞数') # 点赞数
    comment_count = models.IntegerField(default=0,verbose_name='评论数') # 评论数
    favor = models.ManyToManyField(to='UserInfo') # 关联的点赞用户

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '新闻表'



# class Favor(models.Model):
#     user = models.ForeignKey(to='UserInfo', to_field='nid')
#     news = models.ForeignKey(to='News', to_field='id')

class Comment(models.Model):
    '''
    评论表
    '''
    news = models.ForeignKey(to='News',to_field='id',verbose_name='评论新闻ID') # 评论新闻ＩＤ
    user = models.ForeignKey(to='UserInfo', to_field='nid', verbose_name="用户") # 评论用户
    content = models.CharField(max_length=150) # 评论内容
    device = models.CharField(max_length=16,null=True) # 评论设备名称
    ctime = models.DateTimeField(auto_now_add=True) # 评论时间
    parent_comment = models.ForeignKey(to='self',null=True, related_name='cp') # 评论的关联ID
    # related_name 反向查询时候用到的字段

    def __str__(self):
        return self.news_id

    class Meta:
        verbose_name = '评论表'


class Collection(models.Model):
    '''收藏表'''
    news = models.ForeignKey(to='News', to_field='id', verbose_name="收藏新闻ID")
    user = models.ForeignKey(to='UserInfo', to_field='nid',verbose_name='用户') # 收藏用户
    ctime = models.DateTimeField(auto_now_add=True) # 收藏时间

    # def __str__(self):
    #     return self.news_id

    class Meta:
        verbose_name = '收藏表'





















