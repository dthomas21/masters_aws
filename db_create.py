from application import db
from application.models import Entry, Golfer

db.create_all()

print("DB created.")
