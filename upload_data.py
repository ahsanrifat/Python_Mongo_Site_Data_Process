import pandas as pd
import pymongo
from os import listdir
from os.path import isfile, join


def save_record_mongo_collection(
    connection_string, db_name, collection_name, dataframe
):
    try:
        # inserting data into mongoDB
        client = pymongo.MongoClient(connection_string)
        # put database name
        database = client.db_name
        # put collections name
        collection1 = database.collection_name
        # inserting the data
        collection1.insert_many(dataframe.to_dict("records"))
    except:
        pass


def make_big_df(path):
    try:
        pass
    except:
        pass
