from django.shortcuts import render, redirect

# Create your views here.
from myapp.forms import TaskForm
from myapp.models import Task


def index(request):
    form = TaskForm()
    tasks=Task.objects.all()
    if request.method == "POST":
        form = TaskForm(request.POST)
        try:
            if form.is_valid():
                form.save()
                return redirect('/')
            else:
                print('is not valid')
        except:
            print('error')
    context={'form':form,'tasks':tasks}
    return render(request,'index.html',context)


def update(reuest,pk):
    task=Task.objects.get(id=pk)
    form=TaskForm(instance=task)

    if reuest.method == 'POST':
        form=TaskForm(reuest.POST,instance=task)
        try:
            if form.is_valid():
                form.save()
                return redirect('/')
        except:
            print('error')
    context={'task':task,'form':form}
    return render(reuest,'update.html',context)











