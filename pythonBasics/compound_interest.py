
import sys
#import pdb  #python debugger

if len(sys.argv) != 4:
    raise SystemExit('Usage: compound_interest.py principal rate time')

principal = float(sys.argv[1])
rate = float(sys.argv[2])
time = int(sys.argv[3])

interest = 0.0
loan_at_start = principal
loan_at_end = principal

out = open("loandetail.txt", "w")

print("{} {} {} {}".format("Year", "Loan at start", "Interest", "Loan at End"))

for year in range(time):
    loan_at_start = loan_at_end
    interest = loan_at_end * (rate/100)
    loan_at_end += interest
    print("{:>5d} {:>10.2f} {:>10.2f} {:>10.2f}".format(year, loan_at_start, interest, loan_at_end))
    print("{:>5d} {:>10.2f} {:>10.2f} {:>10.2f}".format(year, loan_at_start, interest, loan_at_end), file=out)

print("You payback for the principal amount ${:<10.2f} is ${:<10.2f}".format(principal, loan_at_end))
print("You payback for the principal amount ${:<10.2f} is ${:<10.2f}".format(principal, loan_at_end), file=out)

out.close()