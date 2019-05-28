class PurchasedItem(object):

    counter = 0  #class variable

    def __init__(self, id, account, purchased_quantity, 
                item_name, item_quantity, item_unit, item_price, category):
        self.id = id
        self.account = account
        self.purchased_quantity = purchased_quantity
        self.name = item_name
        self.quantity = item_quantity
        self.unit = item_unit
        self.price = item_price
        self.category = category

        PurchasedItem.counter += 1

# example to initiate
#item = PurchasedItem("123", "itsadnan@gmail.com", 10, "Milk", 1, "qt", 2.0, "Dairy")

    def change_price(self, price):
        self.price = price

    def subtotal(self):
        return self.purchased_quantity * self.price
    
    def printItem(self):
        print(self.id, self.account, self.purchased_quantity, 
                self.name, self.quantity, self.unit, self.price, self.category)