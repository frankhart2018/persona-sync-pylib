import pymongo
from pymongo.collection import Collection
from pymongo.results import UpdateResult
from typing import Union, Optional, List, Dict, Any
from bson.objectid import ObjectId
import pydantic

from .singleton import singleton
from .environment import MONGO_HOST


@singleton
class MongoCollection:
    def __init__(self, db_name: str) -> None:
        client = pymongo.MongoClient(host=MONGO_HOST)
        self.__db = client[db_name]

    def get_collection(self, collection: str) -> Collection:
        return self.__db[collection]
