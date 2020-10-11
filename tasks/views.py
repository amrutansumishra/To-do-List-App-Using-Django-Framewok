from django.shortcuts import render,redirect
from tasks.models import Task
from django.contrib import messages
# Create your views here.
def home(request):
    if request.method == 'POST':
        title = request.POST.get('todo')
        todo = Task(title = title)
        todo.save()
        messages.success(request,('Item Added to List'))
    data = Task.objects.all()
    content = { 'data':data}
    return render(request,'list.html',content)
def delete(request, pk):
    item = Task.objects.get(id = pk)
    item.delete()
    messages.success(request,('Item Deleted'))
    return redirect('home')
def cross_off(request, pk):
    item = Task.objects.get(id = pk)
    item.complete = False
    item.save()
    return redirect('home')
def cross_on(request, pk):
    item = Task.objects.get(id = pk)
    item.complete = True
    item.save()
    return redirect('home')
def edit(request, pk):
    if request.method == 'POST':
        title = request.POST.get('todo')
        item = Task.objects.get(id = pk)
        item.title = title
        item.save()
        messages.success(request,('Item Updated to List'))
        return redirect('home')
    else:
        data = Task.objects.get(id = pk)
        content = { 'data':data}
        return render(request,'update.html',content)