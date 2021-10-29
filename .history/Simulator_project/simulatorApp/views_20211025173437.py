from django.shortcuts import render

# Create your views here.
def index(requset):
    return render(requset,'index.html')
def sjf(requset):
    return render(requset,'/pro/sjf.html')