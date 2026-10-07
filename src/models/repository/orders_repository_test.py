from src.models.connection.connection_handler import DBConnectionHandler
from src.models.repository.orders_repository import OrdersRepository
import pytest

db_connection_handler = DBConnectionHandler()
db_connection_handler.connect_to_db()
conn = db_connection_handler.get_db_connection()

@pytest.mark.skip(reason="Interacao com o banco")
def test_insert_document():
    orders_repository = OrdersRepository(conn)
    my_doc = {"Alguma": "coisa"}
    orders_repository.insert_documents(my_doc)

@pytest.mark.skip(reason="Interacao com o banco")
def test_list_of_documents():
    orders_repository = OrdersRepository(conn)
    my_doc = [{"elem1": "Ola"}, {"elem2": "Ola2"}, {"elem3": "Ola3"}]
    orders_repository.insert_list_of_documents(my_doc)

@pytest.mark.skip(reason="Interacao com o banco")
def test_select_many():
    orders_repository = OrdersRepository(conn)
    doc_filter = {"cupom": True}
    response = orders_repository.select_many(doc_filter)
    print()
    print(response)
    for doc in response:
        print(doc)
        print(doc["itens"])
        print()

@pytest.mark.skip(reason="Interacao com o banco")
def test_select_one():
    orders_repository = OrdersRepository(conn)
    doc_filter = {"cupom": True}
    response = orders_repository.select_one(doc_filter)
    print()
    print(response)

@pytest.mark.skip(reason="Interacao com o banco")
def test_select_many_with_properties():
    orders_repository = OrdersRepository(conn)
    doc_filter = {"cupom": True}
    response = orders_repository.select_many_with_properties(doc_filter)
    print()
    for doc in response:
        print(doc)
        print()

@pytest.mark.skip(reason="Interacao com o banco")
def test_select_if_property_exists():
    orders_repository = OrdersRepository(conn)
    response = orders_repository.select_if_property_exists()
    print()
    print(response)
    for doc in response:
        print(doc)
        print()

@pytest.mark.skip(reason="Interacao com o banco")
def test_select_many_with_multiple_filters(): #Selecionar documentos do banco de dados com base em múltiplos filtros
    orders_repository = OrdersRepository(conn)
    doc_filter = {
        "cupom": True,
        "itens.doce": {"$exists": True}
    }
    response = orders_repository.select_many(doc_filter)
    for doc in response:
        print(doc)
        print()

@pytest.mark.skip(reason="Interacao com o banco")
def test_select_many_with_or_filters(): 
    orders_repository = OrdersRepository(conn)
    doc_filter = {
        "$or": [
            {"address": {"$exists": True}},
            {"itens.doce": {"$exists": True}}
        ]
    }
    response = orders_repository.select_many(doc_filter)
    for doc in response:
        print(doc)
        print()

@pytest.mark.skip(reason="Interacao com o banco")
def test_select_by_id():
    orders_repository = OrdersRepository(conn)
    object_id = "6abda7a4bbbde9f743f50148"  # Substitua pelo ObjectId real que você deseja consultar
    response = orders_repository.select_by_id(object_id)
    print()
    print(response)

@pytest.mark.skip(reason="Interacao com o banco")
def test_edit_registry():
    orders_repository = OrdersRepository(conn)
    orders_repository.edit_registry()

@pytest.mark.skip(reason="Interacao com o banco")
def test_edit_many_registries():
    orders_repository = OrdersRepository(conn)
    orders_repository.edit_many_registries()

@pytest.mark.skip(reason="Interacao com o banco")
def test_edit_with_increment():
    orders_repository = OrdersRepository(conn)
    orders_repository.edit__with_increment()