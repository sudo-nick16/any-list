from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import todoitem

def todoview(request):
    allitems = todoitem.objects.all()
    return render(request, 'todo.html',
        {'all' : allitems}
    )

def addtodo(request):
    c = request.POST['content']
    new_item = todoitem(content = c)
    new_item.save()
    return HttpResponseRedirect('/todo/')

def deltodo(request, todo_id):
    getitems = todoitem.objects.get(id=todo_id)
    getitems.delete()
    return HttpResponseRedirect('/todo/')
    #create a new todo item
    #save
    #redirect the browser to /todo/


# Create your views here.
