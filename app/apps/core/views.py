from django.shortcuts import render, redirect

from .models import *
from .forms import Productform

def crearproducto(request):
    if request.method=='POST':
        form =Productform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form= Productform()
    return render(request,'core/crear_producto.html',{'form':form})