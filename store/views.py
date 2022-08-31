from django.shortcuts import render

from store.models import Producto

def store(request):
    productos = Producto.objects.all()
    data= { 
           'productos':productos }  
    return render(request, 'store/store.html', data)

def cart(request):
	productos = Producto.objects.all()
	data= { 
           'productos':productos }  
	return render(request, 'store/cart.html', data)

def checkout(request):
	context = {}
	return render(request, 'store/checkout.html', context)

def contacto(request):
	context = {}
	return render(request, 'store/contacto.html', context)