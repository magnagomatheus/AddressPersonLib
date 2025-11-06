from Lib.model.models import *
from Lib.model.dto import *

import pytest


def createPerson():

    person = PersonCreate(name = "Matheus")

    assert person.name == "Matheus"

def createAddress():
    address = AddressCreate(
        logradouro = "Avenida Brasil",
        numero = 11,
        estado = "RJ",
        cidade = "Cabo Frio",
        bairro = "Arraial do Cabo"  
    )

    assert address.numero == 11
    assert address.cidade == "Cabo Frio"
    assert address.estado == "RJ"

def updateAddress():

    address = AddressUpdate(
        numero = 777,
        estado = "SP"
    )

    assert numero == 777
    assert estado == "SP"
    assert cidade is None
    assert logradouro is None

def test_person_with_address():
    
    address = AddressCreate(
        logradouro = "Rua santosfutebolclube",
        numero = 1010,
        estado = "SP",
        cidade = "Santos",
        bairro = "Baixada Santista" 
    )

    person = PersonCreate(name="Matheusss", address_id=1)

    assert address.cidade == "Santos"
    assert address.bairro == "Baixada Santista"
    
    assert person.name == "Matheusss"
    assert person.address_id == 1