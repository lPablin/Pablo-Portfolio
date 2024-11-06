from pymongo import MongoClient
import pandas as pd

# Conectar a MongoDB (cambiar la URL a la de tu servidor si es necesario)
client = MongoClient("mongodb://localhost:27017/")  # Para una base de datos local
# client = MongoClient("mongodb+srv://<username>:<password>@cluster0.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")  # Para MongoDB Atlas

# Seleccionar la base de datos
db = client["tweets_db"]

# Seleccionar la colección donde almacenar los datos
collection = db["tweets_collection"]
archivos=['nafti']

for i in archivos:
    # Cargar el CSV en un DataFrame de pandas
    df = pd.read_csv('nafti.csv')
    # Convertir el DataFrame a un diccionario para insertarlo en MongoDB
    data_dict = df.to_dict("records")
    # Insertar los datos en la colección
    collection.insert_many(data_dict)

print("Datos insertados en MongoDB correctamente")