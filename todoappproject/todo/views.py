from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.utils import timezone

from .models import TODOModel

# Create your views here.

def home(request):
    if request.method=="POST":
        pub_date=timezone.now()
        content = request.POST["content"]
        created_obj = TODOModel.objects.create(date_pub=pub_date, text=content)
        return redirect('home')
    else:
        todolist=TODOModel.objects.all().order_by("-date_pub")
    context={
        'todolist':todolist
    }
    return render(request,"todo/index.html",context)
'''
def add_todo(request):
    if request.method=="POST":
        pub_date=timezone.now()
        content = request.POST["content"]
        created_obj = TODOModel.objects.create(date_pub=pub_date, text=content)
        return redirect('home')
'''
def delete_todo(request,todo_id):
    if request.method=="POST":
        TODOModel.objects.get(id=todo_id).delete()
        return redirect('home')

