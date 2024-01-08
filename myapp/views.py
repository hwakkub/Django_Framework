from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("<h1>หน้าแรกของเวป</h1>")

def about(request):
    return HttpResponse("<h1>เกี่ยวกับดรา</h1>")

def form(request):
    return HttpResponse("<h1>แบบฟอร์มบันทึกข้อมูล</h1")
