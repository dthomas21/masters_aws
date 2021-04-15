from flask import Flask
from flask_sqlalchemy import SQLAlchemy



print("init")
application = Flask(__name__)
application.config.from_object('config')
application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# application.config["SQLALCHEMY_DATABASE_URI"] = 'mysql+pymysql://admin:masters123@masters-10-15.ccegwawiyjmw.us-west-2.rds.amazonaws.com:3306/masters1015'
# application.config["SQLALCHEMY_DATABASE_URI"] = 'mysql+pymysql://admin:masters123@masters-live.ccegwawiyjmw.us-west-2.rds.amazonaws.com:3306/masterslive'
# application.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
# this is working locally:
# application.config["SQLALCHEMY_DATABASE_URI"] = 'mysql+pymysql://admin:masters123@masters-take-2.c3av2ojnfrwy.us-east-1.rds.amazonaws.com:3306/masters2'
# retesting:
application.config["SQLALCHEMY_DATABASE_URI"] = 'mysql+pymysql://admin:masters123@masters-take-3.ccegwawiyjmw.us-west-2.rds.amazonaws.com:3306/masters3'

# application.config["SQLALCHEMY_DATABASE_URI"] = 'mysql+pymysql://admin:masters123@database-1.ccegwawiyjmw.us-west-2.rds.amazonaws.com:3306/masters4'

application.secret_key = 'noclue'
db = SQLAlchemy(application)

db.init_app(application)
