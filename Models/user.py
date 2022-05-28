from Models import db


class User(db.Document):
    _id = db.IntField(required=True)
    name = db.StringField()
    position = db.StringField() # Seller or Customer
    deals_availed = db.ListField()