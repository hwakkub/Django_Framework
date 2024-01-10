from django.shortcuts import render
from django.http import HttpResponse
from myapp.models import Person

# def index(request):
#     return render(request, "index.html")

# def about(request):
#     return HttpResponse("<h1>เกี่ยวกับดรา</h1>")

# def my_view(request):
#     context = {}
#     return render(request,'index.html', context)

def my_view(request):
    all_persion = Person.objects.all()
    # all_persion = Person.objects.filter(age=23)
    return render(request,'index.html',{"all_persion":all_persion})

def about(request):
    return render(request,'about.html')
    
def form(request):
    return render(request,'form.html')

