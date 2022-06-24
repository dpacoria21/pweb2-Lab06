from imp import reload
from unicodedata import name
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
        return redirect('/listarDestinos')
    else:
        print("No se ha guardado")
        form = DestinationForm()
    
    context = {
        'form' : form
    }
    return render(request, 'addDestination.html',context)

def listarDestinos(request):
    dests = Destination.objects.all()
    return render(request, 'listarDestinos.html', {'Destin': dests})

def index(request):

    dests = Destination.objects.all()

    return render(request, 'index.html',{'Destin': dests})

def modDestino(request, myID):
    print(myID)
    obj = Destination.objects.get(id = myID)
    form = DestinationForm(request.POST or None, instance = obj)
    
    if form.is_valid():
        print('Aqui estuvo')
        form.save()
        form = DestinationForm()
        return redirect('/listarDestinos')
    else:
        print('here!!')
    context = {
        'form': form,
    }
    return render(request, 'modDestino.html',context)

def eliminarDestino(request, myID):
    return render(request, 'eliminarDestino.html')
