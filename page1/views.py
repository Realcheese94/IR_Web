# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http.response import HttpResponse


def index(request):
    return render(request,'index.html')
    #return HttpResponse('주연아 사랑해 ㅎㅎㅎ')