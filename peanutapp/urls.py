#-*- coding:utf-8 -*-

from django.urls import path
from . import views
from django.urls import include
from django.views.static import serve


'''
urlpatterns = [
    path('', views.index, name = 'index'),
    path('career/', views.career, name = 'career'),
]
'''

urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('career/', views.CareerView.as_view(), name="career"),
    path('mypage/', views.MypageView.as_view(), name="mypage"),
    path('careerUpdate/', views.CareerUpdateView.as_view(), name="careerUpdate"),
    path('note/',views.NoteView.as_view(), name='note'),
    path('noteList/',views.NoteListView.as_view(), name='noteList'),
    path('noteListUpdate/',views.NoteListUpdate.as_view(), name='noteupdate'),
    path('noteDelete/',views.NoteDelete.as_view(), name='notedelete'),
    path('education/',views.EducationView.as_view(), name='education'),
    path('educationUpdate/',views.EducationUpdateView.as_view(), name='educationUpdate')
]
