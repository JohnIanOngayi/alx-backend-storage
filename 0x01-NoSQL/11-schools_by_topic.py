#!/usr/bin/env python3

"""
Module defines a Python function that returns the list of school having
        a specific topic
"""


def schools_by_topic(mongo_collection, topic):
    """
    returns list of school having a specific topic
    """
    return mongo_collection.find({"topics": topic})
