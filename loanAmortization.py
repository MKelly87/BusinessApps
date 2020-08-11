import locale
locale.setlocale( locale.LC_ALL, '' )
import argparse
from beautifultable import BeautifulTable

def amortize(value,rate,pmt_yrs):
    n = 0
    intrate = rate/12.0
    totalpmts = pmt_yrs *12
    payment = (intrate * value) / ( 1 - pow(1+intrate,-totalpmts))
    table = BeautifulTable()
    table.columns.header=["MONTH","LOAN VALUE","PAYMENT","INTEREST","PRINCIPLE","NEW VALUE"]
    while value > 0:
        n = n + 1

        interest = (value * intrate)
        principle = payment - interest
       
        if value - payment < 0:
            principle = value
        table.rows.append([n,locale.currency(value,grouping='yes'),
                             locale.currency(payment,grouping='yes'), 
                             locale.currency(interest,grouping='yes'),
                             locale.currency(principle,grouping='yes'), 
                             locale.currency(value-principle,grouping='yes')])
        
        value = value - principle
        
    print(table)
               
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("value",help="Loan Value")
    parser.add_argument("rate",help="Interest rate as a decimal (5% = .05)")
    parser.add_argument("years",help="Loan term in years")
    
    args = parser.parse_args()
    
    value = float(args.value)
    rate = float(args.rate)
    pmt_yrs = float(args.years)

    amortize(value,rate,pmt_yrs)

    

main()
