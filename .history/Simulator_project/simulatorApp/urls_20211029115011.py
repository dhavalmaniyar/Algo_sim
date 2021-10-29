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
    path('producer_consumer',views.producerconsumer,name='producerconsumer'),

    path('rw_wiki',views.rw_wiki,name='rw_wiki'),
    path('readerwriter',views.readerwriter,name='readerwriter'),

    path('dining_wiki',views.dining_wiki,name='dining_wiki'),
    path('dining',views.dining,name='dining'),

    path('cigarette_smoke_wiki',views.cigarette_smoke_wiki,name='cigarette_smoke_wiki'),
    path('cigarette_smokers',views.cigarette_smokers,name='cigarette_smokers'),

    path('sb_wiki',views.sb_wiki,name='sb_wiki'),    
    path('sleepingBarber',views.sleepingBarber, name='sleepingBarber'),

    path('banker',views.banker,name='banker'),
    path('mft',views.mft,name='mft'),

    path('lru',views.lru,name='lru'),
    path('lruwiki',views.lruwiki,name='lruwiki'),

    path('disk',views.disk,name='disk'),

    path('contiguous',views.contiguous,name='contiguous'),
    path('linked',views.linked,name='linked'),

    path('single_level_directory',views.single_level_directory,name='single_level_directory'),
    path('two_level_directory',views.two_level_directory,name='two_level_directory'),
]