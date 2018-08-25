#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
created on 2018/8/22
@user: Keekuun
功能描述
自定义form表单
"""
from myweb.models import Article
from django import forms



class AddArticleForm(forms.ModelForm):

    class Meta:
        model = Article
        exclude = ('category',)

