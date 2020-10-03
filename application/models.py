from application import db


class Golfer(db.Model):
    __tablename__ = "golfers"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))

    def __init__(self, notes):
        self.notes = notes

    def __repr__(self):
        return self.notes


class Entry(db.Model):
    """"""
    __tablename__ = "entries"
    id = db.Column(db.Integer, primary_key=True)
    golfer_1 = db.Column(db.String(128))
    golfer_2 = db.Column(db.String(128))
    golfer_3 = db.Column(db.String(128))
    golfer_4 = db.Column(db.String(128))
    tie_breaker = db.Column(db.Integer)

    entry_email_id = db.Column(db.Integer, db.ForeignKey("golfers.id"))
    entry_email = db.relationship("Golfer", backref=db.backref(
        "entries", order_by=id), lazy=True)

# </artist:>
