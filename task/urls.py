from django.urls import path
from task.views import add_task, show_task, edit_task, delete_task

urlpatterns = [
    path('add/', add_task, name='add_task'),
    path('show/', show_task, name='show_task'),
    path('edit/<int:id>', edit_task, name='edit_task'),
    path('delete/<int:id>', delete_task, name='delete_task'),
]
