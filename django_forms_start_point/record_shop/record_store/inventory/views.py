from django.shortcuts import render
from django.http import HttpResponse
from inventory.models import *
from .forms import AlbumForm

def index(request):
    artists = Artist.objects.all()
    return render(request, "inventory/index.html", locals())
def album_new(request):
    form = AlbumForm()
    return render(request, "inventory/album_form.html", {'form': form})