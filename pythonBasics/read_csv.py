
import sys
import csv

if len(sys.argv) != 2:
    raise SystemExit('Usage: read_csv.py filename')

filename = sys.argv[1]

account = None
total = 0.0
total_item = 0

with open(filename) as f:
    rows = csv.reader(f)
    header = next(f)

    print(header)

    for i, row in enumerate(rows):
        row[2] = int(row[2])
        row[6] = float(row[6])

        if account is None:
            account = row[1]
        
        total += row[2] * row[6]
        total_item += row[2]

print("Account Name: {}".format(account))
print("Total Items: {:<5}".format(total_item))
print("Total: {:<10.2f}".format(total))

print("Number of lines processed: {:<5}".format(i+1))