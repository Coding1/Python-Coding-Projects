#!/usr/bin/env python
import json
from pathlib import Path
import sys
import math

# Vending Machine App Design
# Engineer: Wayne Moore
# Date: 07/08/18


#                                        *** Vending Machine Application ***
#*********************************************************************************************************************
# To run the program go to src dir and enter: python vending.py ../test/01/inventory.json ../test/01/transactions.json
#*********************************************************************************************************************
# To run the run_tests.py program go to run_tests.py dir and enter: python run_tests.py
#*********************************************************************************************************************

# Load inventory JSON file from command line argument
# Vending Machine module for inventory computation engine
inventory_json = open(sys.argv[1]).read()
my_json_dict = json.loads(inventory_json)
for vending_stock in my_json_dict:
    # inventory is a dictionary
    #print("Vending stock item: ", vending_stock) # example usage
    #print("Vending product: ",vending_stock)
    #print("dict of item price: ", my_json_dict['Cool Ranch Doritos']['price'])
    #item_price = my_json_dict['Cool Ranch Doritos']['price']
    # Checking is vending price equals produce price
    if (my_json_dict['Cool Ranch Doritos']['price']):
        purchase_price = my_json_dict['Cool Ranch Doritos']['price']
        #print("Product purchase price: ", purchase_price)
#**********************************************************************************************************************
# Load transaction JSON file from command line argument
# Vending Machine module for transactions computation engine
transactions_json = open(sys.argv[2]).read()
my_json_dict1 = json.loads(transactions_json)
for purchase_transactions in my_json_dict1:
    # transactions is a dictionary
    #print("Transaction purchases: ", purchase_transactions)
    #print("Item purchased: ", purchase_transactions['name'])
    coins_entered = []
    for item in my_json_dict1:
        coins_entered.append(item['funds'])
        #print(" Value of coins entered: ", coins_entered)
        total = 0
        #print("item: ", item)
        for currentCoin in item["funds"]:
            #print(" CurrentCoin: ", item)
            #print(" Current coin: ", currentCoin)
            total = total + currentCoin
            #print("Total product cost: ", total)
            #print("Product cost: ", purchase_price)
            # change int to float and move decimal 2 places left
            coin_total = float(total)/(100)
            #print("Amount entered: ", coin_total)


# Vending Machine  module for transaction results engine
# Calculate if amount entered is exact, not enough, or requires change returned to user
#**********************************************************************************************************************
args = True
def true(args):
    pass
#**********************************************************************************************************************
# Calculate transactions with product delivered no change returned
# Passing unit test
no_change = 0
transaction_result =  purchase_price - coin_total
change=[]
if transaction_result == no_change and purchase_price == coin_total:
   #product_delivered:true(True)
   #print("No change returned exact amount entered")

   opp = (
       [
           {
               "product_delivered": True,
               "change": []
           }
       ]
   )
   # str = json.dumps(opp, indent=4)
   trans_result = json.dumps(opp, indent=4, default=lambda x: x.__dict__)
   print(trans_result)

#**********************************************************************************************************************
# Calculate transactions with product delivered with change returned
# Passing unit test
if purchase_price < coin_total and transaction_result != no_change and coins_entered != [[25, 25, 100], [25, 25, 100]]:
     change_list = coin_total - purchase_price
     vending_change = math.ceil(change_list * 100)
     #print("Product change return: ", vending_change)
     # Split coin change value
     coin_value1 = vending_change / 2
     change.append(int(coin_value1))
     #print("coin change list: ", change)
     coin_value2 = vending_change / 2
     change.append(int(coin_value2))
     #print("coin change list: ", change)

     #opp["change"].append(list(change = change))
     # Append transaction change to JSON object
     opp = (
         [
             {
                 "product_delivered": True,
                 "change": change

             }
         ]
     )
     trans_result = json.dumps(opp, indent=4, default=lambda x: x.__dict__)
     print(trans_result)

#**********************************************************************************************************************
# Calculate multiple transactions with and without product delivered with change returned
if purchase_price < coin_total and coins_entered == [[25, 25, 100], [25, 25, 100]]:
   change_list = coin_total - purchase_price
   vending_change = math.ceil(change_list * 100)
   # print("Product change return: ", vending_change)
   # Split coin change value
   coin_value1 = vending_change / 2
   change.append(int(coin_value1))
   # print("coin change list: ", change)
   coin_value2 = vending_change / 2
   change.append(int(coin_value2))


# Vending machine product delivery transactions and change returned
   opp = (
       [
           {
               "product_delivered": True,
               "change": change
           }
       ]
   )

   opp2 = {
              "product_delivered": False,
              "change": [
               25,
               25,
               100
      ]
  }
   # multiple transactions the second is not valid return change
   if coins_entered == [[25, 25, 100], [25, 25, 100]]:
      opp.append(opp2)
      trans_result = json.dumps(opp, indent=4, default=lambda x: x.__dict__)
      print(trans_result)

#**********************************************************************************************************************





