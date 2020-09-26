from application import db


class Golfer(db.Model):
    __tablename__ = "golfers"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

    def __init__(selfself, notes):
        self.notes = notes

    def __repr__(self):
        return self.notes


class Entry(db.Model):
    """"""
    __tablename__ = "entries"
    id = db.Column(db.Integer, primary_key=True)
    golfer_1 = db.Column(db.String)
    golfer_2 = db.Column(db.String)
    golfer_3 = db.Column(db.String)
    golfer_4 = db.Column(db.String)
    tie_breaker = db.Column(db.Integer)

    entry_email_id = db.Column(db.Integer, db.ForeignKey("golfers.id"))
    entry_email = db.relationship("Golfer", backref=db.backref(
        "entries", order_by=id), lazy=True)

# </artist:>
