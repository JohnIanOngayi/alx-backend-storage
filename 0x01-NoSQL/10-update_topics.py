#!/usr/bin/env python3

"""
Module defines function that changes all topics of a school document based
on the name.
"""

from typing import List
from pymongo.collection import Collection


def update_topics(mongo_collection: Collection, name: str, topics: List[str]) -> None:
    """
    Updates all topics of a school document based on the name.

    Args:
    mongo_collection (Collection): The collection object.
    name (str): The name to filter for in the collection.
    topics (List[str]): List of strings representing the new topics.

    Returns:
    None
    """
    query = {"name": name}
    new_values = {"$set": {"topics": topics}}
    mongo_collection.update_many(query, new_values)
