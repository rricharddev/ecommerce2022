from django.shortcuts import render ,redirect
from .forms import CustomUserCreationForm
from store.models import Producto
from django.contrib.auth import authenticate , login
from django.contrib import messages

def tienda(request):
    productos = Producto.objects.all()
    data= { 
           'productos':productos }  
    return render(request, 'tienda.html', data)


def contacto(request):
	context = {}
	return render(request, 'contacto.html', context)


def registro(request):
    data={
		'form': CustomUserCreationForm
	}
    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request ,user)
            messages.success(request,"registro correcto")
            return redirect(to="tienda")
        data['form']= formulario
    return render(request,'registration/registro.html',data)
  