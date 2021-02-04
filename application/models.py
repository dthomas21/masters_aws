from application import db


class Golfer(db.Model):
    __tablename__ = "golfers"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))#, index=True, unique=False)

    # def __init__(self, name):
    #     self.name = name

    def __repr__(self):
        return self.name


class Entry(db.Model):
    """"""
    __tablename__ = "entries"
    id = db.Column(db.Integer, primary_key=True)
    entrant_full_name = db.Column(db.String(128))
    team_name = db.Column(db.String(128))
    golfer_1 = db.Column(db.String(128))
    golfer_2 = db.Column(db.String(128))
    golfer_3 = db.Column(db.String(128))
    golfer_4 = db.Column(db.String(128))
    tie_breaker = db.Column(db.Integer)
    has_paid = db.Column(db.String(128), default='No')

    entry_email_id = db.Column(db.Integer, db.ForeignKey("golfers.id"))
    entry_email = db.relationship("Golfer", backref=db.backref(
        "entries", order_by=id), lazy=True)


# </artist:>
