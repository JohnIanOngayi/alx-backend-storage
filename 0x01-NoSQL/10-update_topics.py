#!/usr/bin/env python3

"""
Module defines function that changes all topics of a school document based
        on the name
"""


def update_topics(mongo_collection, name, topics):
    """
    updates all topics of a school doc based on the name

    args:
    mongo_collection {pymongo.Collection} - collection object
    name {str} - name filtered for in collection
    topics {List[str]} - list of strings approached in the school

    returns:
    Never
    """
    query = {"name": name}
    newValues = {"$set": {"topics": topics}}
    mongo_collection.update_many(query, newValues)
