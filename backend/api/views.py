from django.http import JsonResponse


def api_home(request, *args, **kwargs):
    res = {"message": "Hello, this is your API response!"}
    return JsonResponse(res)
