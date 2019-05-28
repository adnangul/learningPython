
# the fnction will not be executable by default run it like - pyhton -i read_class_from_csv.py and then call function with file name to test

import csv
from purchased_item_class import PurchasedItem
from output_list import print_list

def read_file(filename):
    """
     Build a list of rows  rom a CSV file - 

     Usage example - python -i data_class_from_csv.py
        data = read_file("Book1.csv")

        for item in data:
            item.printItem()

        names = [item.name for item in data]
        names

        names = {item.name for item in data}
        names

         PurchasedItem.counter  #access class variable

         # all the example we did without class n data structures can be done with class

         #the display can be used as 
         display(data, ['name', 'price'])
         display(data, ['name', 'category','price'])   # whatever combination needed, as far as the attribute exists in the list's object
    """
    data = []
    with open(filename) as f:
        rows = csv.reader(f)
        header = next(f)

        for row in rows:
            row[2] = int(row[2])
            row[6] = float(row[6])
            
            item = PurchasedItem(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
            data.append(item)  
            
    return data

def display(list, attributes):
    print_list(list, attributes)
