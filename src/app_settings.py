from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from database_connection import DB_URL

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = DB_URL
db = SQLAlchemy(app)
