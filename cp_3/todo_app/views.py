from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from todo_app.models import TodoList, Todo
import json

@csrf_exempt
def todo_lists(request):
    if request.method == 'GET':
        todo_lists = TodoList.objects.all()
        data = []
        for todo_list in todo_lists:
            data.append({
                'id': todo_list.id,
                'name': todo_list.name,
                'created_at': todo_list.created_at,
                'updated_at': todo_list.updated_at,
            })
        return JsonResponse({'data': data})

    elif request.method == 'POST':
        data = json.loads(request.body)
        todo_list = TodoList(name=data['name'])
        todo_list.save()
        return JsonResponse({'id': todo_list.id})

