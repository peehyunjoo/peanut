#-*- coding:utf-8 -*-

from django.urls import path
from . import views

'''
urlpatterns = [
    path('', views.index, name = 'index'),
    path('career/', views.career, name = 'career'),
]
'''

urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('career/', views.CareerView.as_view(), name="career"),
]