
from flask import Flask
from flask_pymongo import PyMongo
from flask_jwt_extended import JWTManager 
import certifi



loan = Flask(__name__, template_folder='views', static_folder='static')
loan.config["MONGO_URI"] = "mongodb+srv://test:test@cluster0.uuxsg40.mongodb.net/loans?retryWrites=true&w=majority&appName=Cluster0"
loan.config['JWT_SECRET_KEY'] = "loanservices"


loan.secret_key = "mysecret"
ca = certifi.where()

mongo = PyMongo(loan, tlsCAFile=ca)
jwt = JWTManager(loan)