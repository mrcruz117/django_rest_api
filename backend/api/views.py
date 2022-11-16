import json
from django.forms.models import model_to_dict
from django.http import JsonResponse

from products.models import Product
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(["GET"])
def api_home(request, *args, **kwargs):
    model_data = Product.objects.all().order_by("?").first()
    data = {}
    if model_data:
        data = model_to_dict(model_data, fields=['id', 'title'])
        # ^^^ does the same as below
        # data["id"] = model_data.id
        # data["title"] = model_data.title
        # data["content"] = model_data.content
        # data["price"] = model_data.price
    return Response(data)
