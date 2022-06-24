from imp import reload
from django.shortcuts import render, redirect
from .models import Destination
from .forms import DestinationForm
# Create your views here.

def addDestination(request):
    form = DestinationForm(request.POST, request.FILES)
    if form.is_valid():
        print("Se ha guardado")
        form.save()
        form = DestinationForm()
        return redirect('/')
    else:
        print("No se ha guardado")
        form = DestinationForm()
    
    context = {
        'form' : form
    }
    return render(request, 'addDestination.html',context)

def index(request):

    dests = Destination.objects.all()

    return render(request, 'index.html',{'Destin': dests})