#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
author:Ewen Lai
email:lwwens@gmail.com ; lai_wei_wen@qq.com ;
time:2019-04-27 week6 21:38:41
"""


import os

from django.apps import AppConfig


# 修改app在Admin后台显示名称
# default_app_config的值来自apps.py的类名
default_app_config = 'index.IndexConfig'


# 获取当前 app 的命名
def get_current_app_name(_file):
    return os.path.split(os.path.dirname(_file))[-1]


# 重写类 IndexConfig
class IndexConfig(AppConfig):
    name = get_current_app_name(__file__)
    verbose_name = '博客'
