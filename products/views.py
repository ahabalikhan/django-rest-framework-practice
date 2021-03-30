from django.shortcuts import render, get_object_or_404
from .models import Product
from .serializers import ProductSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse


def productDetailView(request, id=0):
    # in case no id is provided
    if id == 0:
        prod = Product.objects.all()  # get all the products
    # if id is provided
    else:
        # get products by id if not exist then get 404 error instead
        prod = get_object_or_404(Product, id=id)
    # serialize data to be read by json renderer
    serializer = ProductSerializer(prod, many=id == 0)
    # make json data to be delivered
    json_data = JSONRenderer().render(serializer.data)
    # BOOM
    # return JsonResponse(json_data, safe=False)
    return HttpResponse(json_data, content_type='application/json')
