from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpRequest, JsonResponse
from .models import Todo

#To list all tasks
def list_todo_item(request):
    todo_list = Todo.objects.all()
    context = {'todo_list': todo_list}
    return render(request, 'todos/todo_list.html', context)

#To create task
def insert_todo_item(request:HttpRequest):
    if request.method == 'POST':
        content = request.POST['content']
        due_date = request.POST['due_date'] or None
        #reminder = request.POST['reminder'] or None

        todo = Todo()
        todo.content = content 
        todo.due_date = due_date
        #todo.reminder = reminder
        todo.save() #save the object
        return redirect('/todo/list/')

#To delete task
def delete_todo_item(request, todo_id):
    todo_delete = Todo.objects.get(id=todo_id)
    todo_delete.delete()
    return redirect('/todo/list/')

#To update task content
def update_todo_item(request,todo_id):
    todo_update = get_object_or_404(Todo, id=todo_id)
    if request.method == 'POST':
        content = request.POST['content']
        if content:
            todo_update.content = content
            todo_update.save()
    return redirect('/todo/list/')
   
#To mark as completed
def toggle_completed(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id)
    if request.method == 'POST':
        todo.completed = not todo.completed
        todo.save()
    return redirect('/todo/list/')
    