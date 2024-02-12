import pandas as pd
import pymongo as mongo

conection = "mongodb+srv://est21405:040902@cluster0.ns9jprh.mongodb.net/"
csvPath = './vgsales.csv'

client = mongo.MongoClient(conection)

db = client['lab3']

df = pd.read_csv(csvPath)

data = df.to_dict(orient='records')

collection = db['videojuegos']

collection.insert_many(data)

client.close()

