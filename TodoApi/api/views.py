from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import TodoSerializer
from postgresConnector.models import Todo
from django.core.cache import cache

@api_view(['GET'])
def get_data(request):
    result = cache.keys("*")
    if len(result) == 0:
        tasks = Todo.objects.all()
        serializer = TodoSerializer(tasks, many=True)
        redis_dict = {}
        for task in serializer.data:
            redis_dict['todo_id'] = task['todo_id']
            redis_dict['name'] = task['name']
            redis_dict['created_at'] = task['created_at']
            redis_dict['completed'] = task['completed']
            cache.set(str(task['todo_id']), redis_dict)
        return Response(serializer.data)
    else:
        all_tasks = []
        for key in result:
            item = cache.get(key)
            all_tasks.append(item)
        return Response(all_tasks)

@api_view(['POST'])
def add_data(request):
    serializer = TodoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        task_id = serializer.data['todo_id']
        cache.set(str(task_id), serializer.data)
    return Response(serializer.data)

@api_view(['POST'])
def update_data(request, pk):
    task = Todo.objects.get(todo_id=pk)
    print(request.data)
    serializer = TodoSerializer(instance=task, data=request.data)
    if serializer.is_valid():
        serializer.save()
        task_id = serializer.data['todo_id']
        cache.set(str(task_id), serializer.data)
    else:
        print("Data is not valid")
        return Response(status=405)
    return Response(serializer.data)

@api_view(['DELETE'])
def delete_data(request, pk):
    task = Todo.objects.get(todo_id=pk)
    cache.delete(str(pk))
    task.delete()
    return Response('Item Deleted Succesfully!')