# Conexión con MongoDB

from pymongo import MongoClient

# Conexión con la BBDD remota
db_client = MongoClient(
    "mongodb+srv://roibaldomir:pass@pingu.zel7rqk.mongodb.net/?retryWrites=true&w=majority")