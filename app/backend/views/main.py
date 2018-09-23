# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from jinja2 import Environment, FileSystemLoader
from django.http import Http404
from django.shortcuts import render

def index(request):
    return render(request, 'test.html', {})
