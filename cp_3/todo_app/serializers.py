from rest_framework import serializers
from todo_app.models import TodoList, Todo

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('id', 'name', 'todo_list')

class TodoListSerializer(serializers.ModelSerializer):
    todos = TodoSerializer(many=True, read_only=True)

    class Meta:
        model = TodoList
        fields = ('id', 'name', 'todos')