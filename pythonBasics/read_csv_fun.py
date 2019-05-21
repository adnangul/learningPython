
# the fnction will not be executable by default run it like - pyhton -i read_csv_fun.py and then call function with file name to test
import csv

def read_file(filename):
    """
     This is an example for reading csv file in function and returning mutiple values
    """

    account = None
    total = 0.0
    total_item = 0

    with open(filename) as f:
        rows = csv.reader(f)
        header = next(f)

        print(header)

        for i, row in enumerate(rows):
            try:
                row[2] = int(row[2])
                row[6] = float(row[6])
            except ValueError as err:
                print("Error occured while processing row# {}, reason:".format(i+1), err)
                continue
            #else:
            #finally:
               
            if account is None:
                account = row[1]
            
            total += row[2] * row[6]
            total_item += row[2]
    
    return account, total, total_item