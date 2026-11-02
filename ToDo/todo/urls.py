from django.urls import path
from todo import views

app_name='todo'

urlpatterns = [
    path('', views.home, name='home'),
    path('add_task/', views.add_task, name='add_task'),
    path('edit_task/<int:task_id>/', views.edit_task, name='edit_task'),
    path('delete_task/<int:task_id>/', views.delete_task, name='delete_task'),
    path('api/tasks/', views.ListCreateTask, name='list_create_task'),
    path('api/tasks_d/<int:pk>/', views.task_detail, name='task_detail'),]
