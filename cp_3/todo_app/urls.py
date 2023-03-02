from django.urls import path
from todo_app.views import todo_lists, todo_list_detail, todo_list_todos, todos, todo_detail

urlpatterns = [
    path('api/todo-lists', todo_lists),
    path('api/todo-lists/<int:id>', todo_list_detail),
    path('api/todo-lists/<int:id>/todos', todo_list_todos),
    path('api/todos', todos),
    path('api/todos/<int:id>', todo_detail),
]
