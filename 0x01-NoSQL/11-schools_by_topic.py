#!/usr/bin/env python3

"""
Module defines a Python function that returns the list of school having
        a specific topic
"""

from pymongo.collection import Collection
from typing import Any, List, Dict


def schools_by_topic(mongo_collection: Collection, topic: str) -> List[Dict[str, Any]]:
    """
    Returns a list of schools having a specific topic.

    Args:
        mongo_collection (Collection): The MongoDB collection object.
        topic (str): The topic to search for in the schools' topics.

    Returns:
        List[Dict[str, Any]]: A list of dictionaries representing the schools
        that have the specified topic.
    """
    return mongo_collection.find({"topics": topic})
