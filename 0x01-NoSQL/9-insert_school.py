#!/usr/bin/env python3

"""
Module defines a Python function that inserts a new document
        in a collection based on kwargs
"""


def insert_school(mongo_collection, **kwargs):
    """
    inserts new doc in collection

    args:
    mongo_collection - db.collection names
    kwargs - json representation of obj

    returns:
    new inserted id
    """
    return mongo_collection.insert_one(kwargs).inserted_id
