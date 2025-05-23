from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.list_todo_item),
    path('insert_todo/', views.insert_todo_item, name='insert_todo_item'),
    path('delete_todo/<int:todo_id>/', views.delete_todo_item, name='delete_todo_item'),
    path('update_todo/<int:todo_id>/', views.update_todo_item, name='update_todo_item'),
    path('toggle/<int:todo_id>/', views.toggle_completed, name='toggle_complete'),
]