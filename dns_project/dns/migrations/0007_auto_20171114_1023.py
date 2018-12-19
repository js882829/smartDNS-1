# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-14 10:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dns', '0006_auto_20170825_1057'),
    ]

    operations = [
        migrations.AddField(
            model_name='bindconfigacl',
            name='cluster_name',
            field=models.CharField(choices=[('cluster1', '测试集群1'), ('cluster2', '测试集群2')], default='', max_length=32, verbose_name='集群名称'),
        ),
        migrations.AddField(
            model_name='bindconfigview',
            name='cluster_name',
            field=models.CharField(choices=[('cluster1', '测试集群1'), ('cluster2', '测试集群2')], default='', max_length=32, verbose_name='集群名称'),
        ),
        migrations.AddField(
            model_name='bindnsrecord',
            name='cluster_name',
            field=models.CharField(choices=[('cluster1', '测试集群1'), ('cluster2', '测试集群2')], default='', max_length=32, verbose_name='集群名称'),
        ),
        migrations.AlterField(
            model_name='bindconfigacl',
            name='acl_name',
            field=models.CharField(choices=[('devsubnet', '研发环境网络'), ('sitsubnet', 'sit测试环境网络'), ('uatsubnet', 'uat测试环境网络'), ('prosubnet', '生产环境网络'), ('ptsubnet', '压测环境网络')], default='devsubnet', max_length=32, verbose_name='子网分组'),
        ),
        migrations.AlterField(
            model_name='bindconfigview',
            name='acl_name',
            field=models.CharField(choices=[('devsubnet', '研发环境网络'), ('sitsubnet', 'sit测试环境网络'), ('uatsubnet', 'uat测试环境网络'), ('prosubnet', '生产环境网络'), ('ptsubnet', '压测环境网络')], default='devsubnet', max_length=32, verbose_name='acl引用'),
        ),
        migrations.AlterField(
            model_name='bindnsrecord',
            name='record_type',
            field=models.CharField(choices=[('A', 'A记录'), ('AAAA', '4A记录'), ('CNAME', 'CNAME'), ('MX', 'MX记录')], default='devsubnet', max_length=32, verbose_name='记录类型'),
        ),
    ]