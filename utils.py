def check_deal_availed(deal, customer):
    if customer.deals_availed.contains(deal.id):
        return True
    else:
        return False


def update_customer_deal_list(customer, deal):
    customer.update(customer.deals_availed.append(deal.id))
