from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/myDatabase"
# app.config["KEY"] =
client = PyMongo(app)

db = client.db


from application import views