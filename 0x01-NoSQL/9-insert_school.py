#!/usr/bin/env python3

"""
Module defines a Python function that inserts a new document
        in a collection based on kwargs
"""

from typing import Any, Dict
from pymongo.collection import Collection
from bson.objectid import ObjectId


def insert_school(mongo_collection: Collection, **kwargs: Dict[str, Any]) -> ObjectId:
    """
    Inserts a new document into the specified MongoDB collection.

    Parameters:
        mongo_collection (Collection): MongoDB collection to insert doc
        **kwargs (Dict[str, Any]): json repr of obj doc to be inserted

    Returns:
        ObjectId: The ID of the newly inserted document.
    """
    return mongo_collection.insert_one(kwargs).inserted_id
