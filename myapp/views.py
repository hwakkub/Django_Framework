from django.shortcuts import render
from django.http import HttpResponse

# def index(request):
#     return render(request, "index.html")

# def about(request):
#     return HttpResponse("<h1>เกี่ยวกับดรา</h1>")

def about(request):
    return render(request,'about.html')
    
def form(request):
    return render(request,'form.html')

def my_view(request):
    context = {}
    return render(request,'index.html', context)