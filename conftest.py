from itertools import product
import pytest
from store.models import Producto
from django.contrib.auth.models import User
import datetime


@pytest.fixture
def crear_producto(db):
    mi_producto = Producto(producto = "Producto2" , fecha_publicacion=datetime.now())
    mi_producto.save()
    return mi_producto
