from datetime import datetime
from flask import Flask, request

from Models import db
from Models.deal import Deal
from Models.item import Item
from Models.user import User
from utils import check_deal_availed, update_customer_deal_list


app = Flask(__name__)

app.config['MONGODB_SETTINGS'] = {
    'db': 'your_database',
    'host': 'localhost',
    'port': 27017
}

db.init_app(app)


@app.route("/")
def welcome():
    item = Item(_id=1, name="Item1").save()
    user = User(_id=1, name="Shubham", position="Seller", deals_availed=[]).save()
    print(item,user)
    return "Welcome"


@app.route("/deals/create/", methods = ['POST'])
def create_deals():
    price = request.args.get('price', default=0, type=int)
    item_id = request.args.get('item_id', default='', type=str)
    seller_id = request.args.get('item_id', default='', type=str)
    number_of_items = request.args.get('number_of_items', default=0, type=int)
    end_time = request.args.get('price', default=0, type=str)
    # end_time need to be parsed
    item = Item.objects(id=item_id).first()
    seller = User.objects(id=seller_id).first()
    deal = Deal(id= item_id, price= price, item = item, seller = seller, number_of_items = number_of_items,
                end_time = datetime.now(), status= "Active").save()
    return deal


@app.route("/deals/end/", methods = ['POST'])
def end_deals():
    deal_id = request.args.get('deal_id', default=0, type=str)
    deal = Deal.objects(id=deal_id).first()
    deal.update(status="Deactivate")
    return deal


@app.route("/deals/update/", methods = ['POST'])
def update_deals():
    deal_id = request.args.get('deal_id', default='', type=str)
    new_number_of_items = request.args.get('new_number_of_items', default=0, type=int)
    new_end_time = request.args.get('new_end_time', default=0, type=str)
    deal = Deal.objects(id=deal_id).first()
    if deal.number_of_items<new_number_of_items and deal.end_time<new_end_time:
        deal.update(number_of_items=new_number_of_items, end_time=new_end_time)
    else:
        return "Wrong input given"


@app.route("/deals/claim/", methods = ['POST'])
def claim_deal():
    deal_id = request.args.get('deal_id', default='', type=str)
    item_id = request.args.get('item_id', default='', type=str)
    customer_id = request.args.get('customer_id', default='', type=str)
    deal = Deal.objects(id=deal_id).first()
    item = Item.objects(id=item_id).first()
    customer = User.objects(id=customer_id).first()
    if deal.number_of_items>0 and deal.end_time>datetime.now() and not(check_deal_availed(deal, customer)) and deal.status=="Active":
        update_customer_deal_list(customer, deal)
        return "Deal availed"
    else:
        return "Deal can't be availed"

