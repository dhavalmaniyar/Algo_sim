from django.shortcuts import render

# Create your views here.
def index(requset):
    return render(requset,'index.html')
def sjf(requset):
    return render(requset,'./process_scheduling/src/sjf.html')
def fcfs(request):
    return render(request,'./process_scheduling/src/fcfs.html') 
def roundr(request):
    return render(request,'./process_scheduling/src/rr.html') 
def priority(request):
    return render(request,'./process_scheduling/src/priority.html') 
def srtf(request):
    return render(request,'./process_scheduling/src/srtf.html') 


def pc_wiki(request):
    return render(request,'./process_sync/pc_wiki.html')
def producerconsumer(request):
    return render(request,'./process_sync/producer_consumer.html')

def rw_wiki(request):
    return render(request,'./process_sync/rw_wiki.html')
def readerwriter(request):
    return render(request,'./process_sync/reader_writer.html')

def dining_wiki(request):
    return render(request,'./process_sync/dining_wiki.html')
def dining(request):
    return render(request,'./process_sync/dining.html')

def cigarette_smoke_wiki(request):
    return render(request,'./process_sync/cigrate_smoke_wiki.html')
def cigarette_smokers(request):
    return render(request,'./process_sync/cigarette_smokers.html')

def sb_wiki(request):
    return render(request,'./process_sync/sb_wiki.html')
def sleepingBarber(request):
    return render(request,'./process_sync/sleepingBarber.html')



def banker(request):
    return render(request,'./Bankers/banker.html')
    
def mft(request):
    return render(request,'./MFT/mft.html')

def lru(request):
    return render(request,'./page_replacement/lruindex.html')
def lruwiki(request):
    return render(request,'./page_replacement/lruwiki.html')

def disk(request):
    return render(request,'./disk/disk.html')

def contiguous(request):
    return render(request,'./FileAllocationAlgorithms/contiguous.html')
def linked(request):
    return render(request,'./FileAllocationAlgorithms/linked.html')

def single_level_directory(request):
    return render(request,'./File_System/single_level_directory.html')
def two_level_directory(request):
    return render(request,'./file_system/two_level_directory.html')





