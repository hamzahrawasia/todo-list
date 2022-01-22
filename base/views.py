from django.shortcuts import render, redirect
from .models import List, Task
from .forms import ListForm
# Create your views here.

# lists = [
#     {'id':1, 'title':'Learn Python'},
#     {'id':2, 'title':'Get Opal Iverson'},
# ]

def home(request):
    lists = List.objects.all()
    return render(request, 'base/home.html', {'lists': lists})


def list(request, id):
    list = List.objects.get(id=id)
    tasks = list.task_set.all()  #to get children, just need to specify model name

    if request.method == 'POST':
        task = Task.objects.create(
            list=list,
            body=request.POST.get('body'),  # 'body' is from keyword given in list.html
        )
        return redirect('list', id=list.id)  #want to fully reload page to make sure we're back on page with get request


    context = {'list': list, 'tasks':tasks}
    return render(request, 'base/list.html', context)

def createList(request):
    form = ListForm()
    if request.method == 'POST':
        form = ListForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'base/list_form.html', {'form':form})

def updateList(request, id):
    list = List.objects.get(id=id)
    form = ListForm(instance=list) #form will be pre-filled with the list value above

    if request.method == 'POST':
        form = ListForm(request.POST, instance=list) #need to tell it which list to update
        if form.is_valid():
            form.save()

    return render(request, 'base/list_form.html', {'form': form})

def deleteList(request, id):
    list = List.objects.get(id=id)
    if request.method == 'POST':
        list.delete() 
        return redirect('home')   #deleted list from database
    return render(request, 'base/delete.html', {'obj':list}) 

def deleteTask(request, id):
    task = Task.objects.get(id=id)
    if request.method == 'POST':
        task.delete() 
        return redirect('home')   #deleted list from database
    return render(request, 'base/delete.html', {'obj':task}) 

# def updateTask(request, id):
#     task = Task.objects.get(id=id)
#     form = ListForm(instance=list) #form will be pre-filled with the list value above

#     # if request.method == 'POST':
#     #     task = ListForm(request.POST, instance=task) #need to tell it which list to update
#     #     if form.is_valid():
#     #         form.save()

#     return render(request, 'base/list.html', {'form': form})