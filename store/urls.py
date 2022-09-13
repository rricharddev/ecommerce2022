from django.urls import path

from .views import tienda, contacto

urlpatterns = [
	
	path('', tienda, name="tienda"),
    path('contacto/', contacto, name="contacto"),


]