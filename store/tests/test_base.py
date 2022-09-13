from itertools import product
import pytest
from store.models import Producto
from django.contrib.auth.models import User
import datetime



@pytest.mark.django_db
def test_cambiar_estado(crear_producto):
    print("cambio de estado de producto")
    assert crear_producto.producto == "producto4"
    


@pytest.mark.django_db
def test_crear_producto():
    mi_producto = Producto(producto = "Producto3" , fecha_publicacion=datetime.now())
    mi_producto.save()
    print(mi_producto.producto)
    assert mi_producto.producto == "Producto3"