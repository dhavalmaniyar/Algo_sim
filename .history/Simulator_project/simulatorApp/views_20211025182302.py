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
def producerconsumer(request):
    return render(request,'./process_sync/pc_wiki.html')
def (request):
    return render(request,'')
def (request):
    return render(request,'')





