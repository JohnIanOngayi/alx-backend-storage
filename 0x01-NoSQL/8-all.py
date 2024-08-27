#!/usr/bin/env python3

"""
Module defines function that lists all documents in a collection
"""

from typing import List, Dict, Any
from pymongo.collection import Collection


def list_all(mongo_collection: Collection) -> List[Dict[str, Any]]:
    """
    Lists all documents in a MongoDB collection.

    Args:
        mongo_collection (Collection): MongoDB collection to list doc from.

    Returns:
        List[Dict[str, Any]]: list of documents, represented as dictionaries.
                              or empty list if no docs or Error occurs
    """
    try:
        doc_list = []
        for doc in mongo_collection.find():
            doc_list.append(doc)
        return doc_list
    except Exception:
        return []
