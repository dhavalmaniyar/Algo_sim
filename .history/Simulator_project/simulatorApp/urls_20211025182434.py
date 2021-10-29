from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('sjf',views.sjf, name='sjf'),
    path('fcfs',views.fcfs,name='fcfs'),    
    path('rr',views.roundr,name='rr'),
    path('priority',views.priority,name='priority'),
    path('srtf',views.srtf,name='srtf'),
    path('producerconsumerproblem',views.producerconsumer,name='pc_wiki'),
    
]