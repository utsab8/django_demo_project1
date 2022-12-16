from django.http import HttpResponse
from django.shortcuts import render
from utsab.models import Product


def home(request):

    # return HttpResponse("welcome Django")
    products = Product.objects.all()
    data = {"products": products}
    return render(request, "home.html", data)
    