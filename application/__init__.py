from flask import Flask
from flask_sqlalchemy import SQLAlchemy



print("init")
application = Flask(__name__)
application.config.from_object('config')
application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
application.config["SQLALCHEMY_DATABASE_URI"] = 'mysql+pymysql://admin:masters123@masters-grant.ccegwawiyjmw.us-west-2.rds.amazonaws.com:3306/mastersoctober'
application.secret_key = 'noclue'
db = SQLAlchemy(application)

db.init_app(application)






