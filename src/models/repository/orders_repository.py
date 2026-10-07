from bson.objectid import ObjectId

class OrdersRepository:
    def __init__(self, db_connection) -> None:
        self.__collection_name = "orders"
        self.__db_connection = db_connection

    def insert_documents(self, document: dict) -> None: #Inserir um documento no banco de dados
        collection = self.__db_connection.get_collection(self.__collection_name)
        collection.insert_one(document)

    def insert_list_of_documents(self, list_of_documents: list) -> None: #Inserir uma lista de documentos no banco de dados
        collection = self.__db_connection.get_collection(self.__collection_name)
        collection.insert_many(list_of_documents)

    def select_many(self, doc_filter: dict) -> list: #Selecionar vários documentos do banco de dados com base em um filtro
        collection = self.__db_connection.get_collection(self.__collection_name)
        data = collection.find(doc_filter)
        return data

    def select_one(self, doc_filter: dict) -> dict: #Selecionar um documento do banco de dados com base em um filtro
        collection = self.__db_connection.get_collection(self.__collection_name)
        response = collection.find_one(doc_filter)
        return response

    def select_many_with_properties(self, doc_filter: dict) -> list: #Selecionar vários documentos com propriedades específicas

        collection = self.__db_connection.get_collection(self.__collection_name)
        data = collection.find(
            doc_filter, #filtro de busca
            {"_id": 0, "cupom": 0}
        )
        return data

    def select_if_property_exists(self) -> dict: #Selecionar documentos que possuem a propriedade "address" e retornar apenas os campos que não são "_id" e "cupom"
        collection = self.__db_connection.get_collection(self.__collection_name)
        response = collection.find(
            {"address":{"$exists": True}},
            {"_id": 0, "cupom": 0}
        )
        return response

    def select_by_id(self, object_id: str) -> dict: #Selecionar um documento do banco de dados com base no ID
        collection = self.__db_connection.get_collection(self.__collection_name)
        data = collection.find_one({"_id": ObjectId(object_id)})
        return data

    def edit_registry(self) -> None:
        collection = self.__db_connection.get_collection(self.__collection_name)
        collection.update_one(
            {"_id": ObjectId("6abda7a4bbbde9f743f50148")}, #filtro
            {"$set": {"cupom": True}} #edição do documento
        )

    def edit_many_registries(self) -> None:
        collection = self.__db_connection.get_collection(self.__collection_name)
        collection.update_many(
            {"itens.refrigerante": {"$exists": True}}, #filtro
            {"$set": {"itens.refrigerante.quantidade": 30}} #edição do documento
        )

    def edit__with_increment(self) -> None:
            collection = self.__db_connection.get_collection(self.__collection_name)
            collection.update_one(
                {"_id": ObjectId("6abda7a4bbbde9f743f50148")}, #filtro
                {"$inc": {"itens.pizza.quantidade": 2}} #edição do documento
            )