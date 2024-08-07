from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_login, name='login'),
    path('signout', views.signout, name='signout'),
    path('register', views.signup, name='register'),
    path('home', views.home, name='home'),
    path('create-task', views.create_task, name='create-task'),
    path('delete-task/<int:task_id>', views.delete_task, name='delete-task'),
    path('edit-task/<int:task_id>', views.edit_task, name='edit-task'),
    path('task-complete/<int:task_id>', views.mark_complete, name='task-complete'),
]