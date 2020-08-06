from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    #return HttpResponse("Hello world! Inventory Index!")
    return render(request, "inventory/index.html")
# Create your views here.