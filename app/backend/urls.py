# from django.urls import path, re_path
# from django.views.generic import TemplateView
# from .views import main
#
# urlpatterns = [
#     # path('', main.index, name='index'),
#     re_path('.*', TemplateView.as_view(template_name='index.html')),
# ]
from django.conf.urls import url
from django.contrib import admin
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', TemplateView.as_view(template_name="index.html")),
]
