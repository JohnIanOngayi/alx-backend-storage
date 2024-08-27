#!/usr/bin/env python3

"""
Module defines function that lists all documents in a collection
"""


def list_all(mongo_collection):
    """
    lists all documents in a collection

    args:
    mongo_collection {pymongo.Collection} - db collection of documents

    returns:
    list of documents or empty list
    """
    try:
        doc_list = []
        for doc in mongo_collection.find():
            doc_list.append(doc)
        return doc_list
    except Exception:
        return []
