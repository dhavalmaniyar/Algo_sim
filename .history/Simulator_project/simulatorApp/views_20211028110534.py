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




