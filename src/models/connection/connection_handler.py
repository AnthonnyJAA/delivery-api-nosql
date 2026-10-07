from pymongo import MongoClient

class DBConnectionHandler:
    def __init__(self) -> None:
        self.__connection_string = "mongodb://127.0.0.1:27017"
        self.__database_name = "NoSQL"
        self.__client = None
        self.__db_connection = None

    def connect_to_db(self):
        self.__client = MongoClient(self.__connection_string)
        self.__db_connection = self.__client[self.__database_name]

    def get_db_connection(self):
        return self.__db_connection