from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.


def hello(request):
    return render(request, 'hello.html')


def views_template_page(request, template_name):
    if request.method == 'GET':
        return render(request, template_name)


def get_table(request):
    data = {
        "total": 11,
        "rows": [
            {"id": 1, "name": "xds", "address": "深圳市福田区", 'age': 18},
            {"id": 2, "name": "xds", "address": "深圳市南山区", 'age': 22},
            {"id": 3, "name": "xds", "address": "深圳市罗湖区", 'age': 24},
            {"id": 4, "name": "xds", "address": "深圳市福田区", 'age': 18},
            {"id": 5, "name": "xds", "address": "深圳市南山区", 'age': 22},
            {"id": 6, "name": "xds", "address": "深圳市罗湖区", 'age': 24},
            {"id": 7, "name": "xds", "address": "深圳市福田区", 'age': 18},
            {"id": 8, "name": "xds", "address": "深圳市南山区", 'age': 22},
            {"id": 9, "name": "xds", "address": "深圳市罗湖区", 'age': 24},
            {"id": 10, "name": "xds", "address": "深圳市福田区", 'age': 18},
            {"id": 11, "name": "xds", "address": "深圳市南山区", 'age': 22},
            {"id": 12, "name": "xds", "address": "深圳市罗湖区", 'age': 24}
        ]
    }
    return JsonResponse(data)
