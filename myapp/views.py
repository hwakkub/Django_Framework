from django.shortcuts import render,redirect
from django.http import HttpResponse
from myapp.models import Person
from django.contrib import messages

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
    if request.method == "POST":
        name = request.POST["name"]
        age = request.POST["age"]
        person = Person.objects.create(
            name=name,
            age=age
        )
        person.save()
        messages.success(request,"บันทึกข้อมูลเรียบร้อย")
        return redirect("/")
    else :
        return render(request,'form.html')

def edit(request,person_id):
  if request.method == "POST":
      person = Person.objects.get(id=person_id)
      person.name = request.POST["name"]
      person.age = request.POST["age"]
      person.save()
      messages.success(request,"อัพเดทข้อมูลเรียบร้อย")
      return redirect("/")
  else:
    person = Person.objects.get(id=person_id)
    return render(request,"edit.html",{"person":person})
  
def delete(request,person_id):
    person = Person.objects.get(id=person_id)
    person.delete()
    messages.success(request,"ลบข้อมูลเรียบร้อย")
    return redirect("/")