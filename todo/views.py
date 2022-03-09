from turtle import title
from django.shortcuts import redirect, render

from todo.models import Todo

# Create your views here.

def index(request):
    todo_object = Todo.objects.all()


    if request.method == 'POST':
        new_todo = Todo (
            title = request.POST['title']
        )

        new_todo.save()
        return redirect('/')
    return render(request, 'todo/index.html', {'todos' : todo_object })


def delete(request, pk):
    obj = Todo.objects.get(id=pk)
    obj.delete()
    return redirect('/')
    
