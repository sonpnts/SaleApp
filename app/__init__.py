from flask import Flask
from urllib.parse import quote
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask (__name__)
app.secret_key='ahsbfhjkagsfugwgf9w7r26826r32'
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://sonpnts:% s@localhost/saleapp?charset=utf8mb4" % quote('Son1010@')
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

db = SQLAlchemy(app)
login = LoginManager(app=app)