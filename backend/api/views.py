import json
from django.http import JsonResponse


def api_home(request, *args, **kwargs):
    # request.body -> HttpRequest -> Django
    res = {"message": "Hello, this is your API response!"}

    body = request.body  # byte string of JSON data
    data = {}
    try:
        data = json.loads(body)
    except:
        pass
    print(data)
    return JsonResponse(res)
