import os
import sys
import numpy as np
import pandas as pd

"""
This module contains constants and configurations for the Network Security training pipeline.
It includes constants for file paths, database configurations, and other parameters used throughout the pipeline."""
TARGET_COLUMN ="Result"
PIPELINE_NAME = "NetworkSecurity"
ARTIFACT_DIR:str = "Artifacts"
FILE_NAME:str="phishingData.csv"
TRAIN_FILE_NAME:str="train.csv"
TEST_FILE_NAME:str="test.csv"


""" MongoDB configurations for data ingestion"""

DATA_INGESTION_COLLECTION_NAME = "NetwrkData"
DATA_INGESTION_DATABASE_NAME = "SOURAV"
DATA_INGESTION_DIR_NAME:str="data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR:str="feature_store"
DATA_INGESTION_INGESTION_DIR:str="ingested"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO:float=0.2