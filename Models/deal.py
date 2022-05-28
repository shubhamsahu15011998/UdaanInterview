from datetime import datetime

from Models.item import Item
from Models.user import User
from Models import db


class Deal:
    id = db.IntField(required=True)
    item = Item
    seller = User
    number_of_items = db.IntField()
    end_time = db.DateTimeField(default=datetime.utcnow)
    status = db.StringField() # Active or Deatcivate
