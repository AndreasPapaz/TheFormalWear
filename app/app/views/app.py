# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from jinja2 import Environment, FileSystemLoader
from django.shortcuts import render_to_response

def index(request):
    import ipdb; ipdb.set_trace()
    render_to_response('test.html')
