from django.urls import path

from . import views

urlpatterns = [
    path('index/', views.index),
    path('test/', views.test_func),
    path('sample/', views.samp),
    path('sample2/', views.sample)
]