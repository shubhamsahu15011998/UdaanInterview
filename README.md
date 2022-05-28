# UdaanInterview
Udaan Interview Question
Problem Statement
You happen to be a budding entrepreneur and you have come up with an idea to build an ecommerce giant like amazon, 
flipkart, walmart, etc.
As part of this ambition, you want to build a platform to duplicate the concept of Limited Time Deals.

Limited Time Deals:
1.A limited time deal implies that a seller will put up an item on sale for a limited time period, say, 2 hours and will keep a maximum limit on the number of items that would be sold as part of that deal. 
2.Users cannot buy the deal if the deal time is over 
3.Users cannot buy if the maximum allowed deal has already been bought by other users.
4.One user cannot buy more than one item as part of the deal.

Task is to create APIs to enable following operations:
1. Create a deal with price and number of items to be sold as part of the deal
2.End a deal 
3.Update a deal to increase the number of items or end time
4: Claim a deal

Guidelines
1:Document and communicate  your assumptions in README. 
2:Create a working solution with production quality code.
3:Use an external database like postgres/mysql or any noSQL database
4:Define and Create APIs to support the operations mentioned above
5:Define the associated entities related to inventory by creating relevant tables in Database. You do not need to create APIs to manage inventory
6.Write few unit tests for the most important code

What are we looking for?
1:Your approach towards the solution
2:How you write code in terms of readability and maintainability
3:Designing Database Schema 
4:Usage of best practices
5:Testing skills



Create Deals => price, item_id, number_of_items, end_time, status
End Deals => id_for_the_deal
update deal => id_for_the_deal, new_number_of_items, new_end_time 
# Apply the check for the greater number of items
# Apply the check for the greater new_end_time
claim the deal => deal_id, item_id
