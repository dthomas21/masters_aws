from applications import db
from applications.models import Entry, Golfer

db.create_all()

print("DB created.")
