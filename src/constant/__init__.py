import os

from urllib.parse import quote_plus
AWS_S3_BUCKET_NAME = "wafer-fault"
MONGO_DATABASE_NAME = "PW"
MONGO_COLLECTION_NAME = "sensor"

TARGET_COLUMN = "quality"


username = 'Vishal'
password = 'Vishal@2003'
cluster_uri = 'cluster0.vnfzods.mongodb.net'  # Your MongoDB cluster URI

# Properly escape the username and password
escaped_username = quote_plus(username)
escaped_password = quote_plus(password)

# Construct the connection string with the escaped credentials
MONGO_DB_URL = f"mongodb+srv://{escaped_username}:{escaped_password}@{cluster_uri}/?retryWrites=true&w=majority"
# MONGO_DB_URL="mongodb+srv://Vishal:Vishal@2003>@cluster0.vnfzods.mongodb.net/?retryWrites=true&w=majority"

MODEL_FILE_NAME = "model"
MODEL_FILE_EXTENSION = ".pkl"

artifact_folder =  "artifacts"