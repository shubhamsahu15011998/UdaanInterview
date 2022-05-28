from Models import db


class Item(db.Document):
    _id = db.IntField(required=True)
    name = db.StringField()
