# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-23 13:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20161221_1904'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=150)),
                ('device', models.CharField(max_length=16, null=True)),
                ('ctime', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64)),
                ('summary', models.CharField(max_length=128, null=True)),
                ('url', models.URLField(null=True)),
                ('ctime', models.DateTimeField(auto_now_add=True)),
                ('nt', models.IntegerField(choices=[(1, '42区'), (2, '段子'), (3, '图片'), (4, '挨踢1024'), (5, '你问我答')])),
                ('favor_count', models.IntegerField(default=0)),
                ('comment_count', models.IntegerField(default=0)),
                ('favor', models.ManyToManyField(to='app.UserInfo')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='n', to='app.UserInfo')),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='news',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.News'),
        ),
        migrations.AddField(
            model_name='comment',
            name='parent_comment',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cp', to='app.Comment'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.UserInfo'),
        ),
    ]