
# the fnction will not be executable by default run it like - pyhton -i read_csv_fun.py and then call function with file name to test

import csv

def read_file(filename):
    """
     Build a list of rows (tuples) rom a CSV file - 
     Examples : 

        > python -i data_structures_frm_csv.py
        data = read_file("Book1.csv")

        type(data)
        type(data[0])

        for r in data[0:1]:
            print(r)
        
        total = 0.0
        for id, account, purchased_quantity, item_name, item_quantity, item_unit, item_price, category in data:
            total += purchased_quantity * item_price

        print(total)

        --------------
        Data comprehensions
        ----------------
         items = [item for item in data if item[6] > 1 ]
         items = [ item[3] for item in data
         total = sum(item[6] for item in data)]

          sorted_name = sorted(data, key=lambda e: e[6])
          min(data, key=lambda e: e[6])

          group by
          -----------
        from itertools import groupby
        grouped_by_cat = groupby(sorted(data, key=lambda e: e[7]), key=lambda e: e[7])
        by_category = {category: list(items) for category, items in grouped_by_cat}
        
        by_category # will print

         [(key, len(value)) for key, value in by_category.items()]
          
        ---------
        filter
        --------
        filter_list = filter(lambda x: x[5] == 'medium', data)
        list(filter_list)

        -------------
        map
        -----
        numbers = [1,2,3,4,5,6,7,8,9,10]
        squared_numbers = map(lambda x: x*x, numbers)
        list(sqaured_numbers)

        def add_subtotal(item):
            item[8] = item[2] * item[6]
            return item

        list(map(add_subtotal, data))  # this will fail in below example, since tuple can't modify
    """
    data = []
    with open(filename) as f:
        rows = csv.reader(f)
        header = next(f)

        for row in rows:
            row[2] = int(row[2])
            row[6] = float(row[6])
            
            record = tuple(row)
            # we can also build dict instead of tuple but above example needs to modified
            #   record = {
            #       'id' : row[0],
            #       'account': row[1]
            #       ...
            #    }

            data.append(record)  
            
    return data