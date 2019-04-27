#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
author:Ewen Lai
email:lwwens@gmail.com ; lai_wei_wen@qq.com ;
time:2019-04-26 week5 21:19:56
"""


from django.contrib import admin

from .models import Category, Tag, Blog, Comment


# 修改 admin 页面的 title 和 header
# 即修改“Django管理”字样为“我的博客”
admin.site.site_title = '我的博客后台管理系统'
admin.site.site_header = '我的博客'


# 注册模型
@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    # 设置模型字段，用于 Admin 后台数据的表头设置
    list_display = ('title', 'category', 'tag', 'click_nums', 'create_time', 'modify_time', )
    # 设置可搜索的字段并在 Admin 后台数据生成搜索框，如有外键应使用双下划线连接两个模型的字段
    search_fields = ('title', 'category__name', 'tag__name', )
    # 设置排序方式（逆序）
    ordering = ('-create_time', )


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    # 设置模型字段，用于 Admin 后台数据的表头设置
    list_display = ('name', 'number', )
    # 设置可搜索的字段并在 Admin 后台数据生成搜索框
    search_fields = ('name', )
    # 设置排序方式（逆序）
    ordering = ('name', )


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    # 设置模型字段，用于 Admin 后台数据的表头设置
    list_display = ('name', 'number', )
    # 设置可搜索的字段并在 Admin 后台数据生成搜索框
    search_fields = ('name', )
    # 设置排序方式（逆序）
    ordering = ('name', )


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    # 设置模型字段，用于 Admin 后台数据的表头设置
    list_display = ('content', 'name', 'blog', 'create_time', )
