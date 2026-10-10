import pytest
from .registry_order_validator import registry_order_validator


def test_registry_order_validator():
    body = {
        "data": {
            "name": "Anthonny",
            "address": "Rua 2 de Julho, 22",
            "cupom": False,
            "items": [
                {"item": "Refrigerante", "quantidade": 2},
                {"item": "Pizza", "quantidade": 1}
            ]
        }
    }

    registry_order_validator(body)

def test_registry_order_validator_error():
    body_error = {
            "data": {
                "name": "Anthonny",
                "address": "Rua 2 de Julho, 22",
                "cupom": "erro",
                "items": [
                    {"item": "Refrigerante", "quantidade": 2},
                    {"item": "Pizza", "quantidade": 1}
                ]
            }
        }

    with pytest.raises(Exception):
        registry_order_validator(body_error)