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


    path('producerconsumerproblem',views.pc_wiki,name='pc_wiki'),
    path('producer_consumer',views.producer_consumer,name='producerconsumer'),
    path('readerwriterproblem',views.readerwriter,name='rw_wiki'),
    path('dining_wiki',views.dining_wiki,name='dining_wiki'),    
    path('cigarette_smokers',views.cigarette_smokers,name='cigarette_smokers'),
    path('sb_wiki',views.sb_wiki,name='sb_wiki'),    
]