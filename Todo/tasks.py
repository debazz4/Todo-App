# todo/tasks.py
from celery import shared_task
from django.utils.timezone import now
from .models import Todo

@shared_task
def send_reminder(todo_id):
    try:
        todo = Todo.objects.get(id=todo_id)
        print(f"Reminder: Task '{todo.content}' is due at {todo.due_date}")
        # You could replace this with sending an email or notification

        
    except Todo.DoesNotExist:
        print(f"Todo with ID {todo_id} does not exist.")

