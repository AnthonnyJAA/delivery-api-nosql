from .registry_order import RegistryOrder
from src.main.http_types.http_request import HttpRequest

class MockOrdersRepository:
    def __init__(self):
        self.insert_documents_att = {}

    def insert_documents(self, document: dict) -> None:
        self.insert_documents_att["document"] = document

def test_registry():
    repo = MockOrdersRepository()
    registry_order = RegistryOrder(repo)

    mock_registry = HttpRequest(
        body={
            "data": {
                "name": "Anthonny",
                "address": "Rua 2 de Julho, 22",
                "cupom": True,
                "items": [
                    {"item": "Refrigerante", "quantity": 2},
                    {"item": "Pizza", "quantity": 1}
                ]
            }
        }
    )

    response = registry_order.registry(mock_registry)

    assert "name" in repo.insert_documents_att["document"]
    assert "address" in repo.insert_documents_att["document"]
    assert "created_at" in repo.insert_documents_att["document"]
    print()
    print(response)
    print()
    print(repo.insert_documents_att)

    