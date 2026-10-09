from .orders_repository import OrdersRepository

class CollectionMock:
    def __init__(self) -> None:
        self.insert_one_atribute = {}
        self.find_atribute = {}

    def insert_one(self, input_data: any):
        self.insert_one_atribute["dict"] = input_data

    def find(self, *args):
        self.find_atribute["args"] = args

class DbCollectionMock:
    def __init__(self, collection) -> None:
        self.get_collection_atribute = {}
        self.collection = collection

    def get_collection(self, collection_name):
        self.get_collection_atribute["name"] = collection_name
        return self.collection


def test_insert_document_mock():
    collection = CollectionMock()
    db_collection = DbCollectionMock(collection)
    repo = OrdersRepository(db_collection)

    doc = {"Alguma": "coisa"}
    repo.insert_documents(doc)

    print()
    print(collection.insert_one_atribute)
    assert collection.insert_one_atribute["dict"] == doc

def test_select_many_with_properties():
    collection = CollectionMock()
    db_connection = DbCollectionMock(collection)
    repo = OrdersRepository(db_connection)

    doc = {"Alguma": "coisa"}
    repo.select_many_with_properties(doc)

    print()

    assert collection.find_atribute["args"][0] == doc
    assert collection.find_atribute["args"][1] == {"_id": 0, "cupom": 0}