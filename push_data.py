import os
import sys
import json
from dotenv import load_dotenv
load_dotenv()

from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
# from networksecurity.constants import MONGO_DB_URL

MONGO_URL = os.getenv("MONGO_DB_URL")
#print(MONGO_URL)
import certifi ## package that prvides certifi.where() to get the path of the CA bundle

ca=certifi.where()
import pandas as pd
import numpy as np
import pymongo

class NetworkDataExtract():
    def __init__(self):
        try:
          pass
        except Exception as e:
            raise NetworkSecurityException(e,sys)

    def cv_to_json(self,file_path):
        try:
            data = pd.read_csv(file_path)
            data.reset_index(drop=True, inplace=True)
            records= list(json.loads(data.T.to_json()).values())
            logging.info(f"Converted CSV data to JSON format with {len(records)} records")
            return records
        except Exception as e:
            raise NetworkSecurityException(e,sys)
    def insert_data_to_mongodb(self,records,database,collection):
       try:
           self.databse=database
           self.collection=collection
           self.records=records
           self.mongo_client=pymongo.MongoClient(MONGO_URL)
           self.databse=self.mongo_client[self.databse]
           self.collection=self.databse[self.collection]
           self.collection.insert_many(self.records)
           return(len(self.records))
       except Exception as e:
           raise NetworkSecurityException(e,sys)
       
if __name__=='__main__':
    FILE_PATH="Network_Data/phisingData.csv"       
    DATABASE="SOURAV"
    Collection="NetworkData"
    networkobj=NetworkDataExtract()
    records=networkobj.cv_to_json(file_path=FILE_PATH)
    no_of_records=networkobj.insert_data_to_mongodb(records,DATABASE,Collection)
    print(f"Inserted {no_of_records} records into MongoDB collection {Collection} in database {DATABASE}")
    logging.info(f"Inserted {no_of_records} records into MongoDB collection {Collection} in database {DATABASE}")
    print("Data pushed successfully to MongoDB")
