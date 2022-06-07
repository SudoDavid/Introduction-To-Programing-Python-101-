#David Piro
#6/6/2022
#Module 5 Assignments - In Class Part 5
#Write a program that calls a function that computes and returns a homeowner's profit from the home's sale. 
result = 0

def salePrice():
    result = input("Please enter a price for the house sale: \n")
    return result

def mortage_payoff(price):
    mortgage = int(input("Please enter the remaining house mortgage: \n"))
    result = price - mortgage
    return result

def realtors_commission(post_mortgage):
    commission = int(input("Please enter the sale's commission: \n"))
    result = post_mortgage - commission
    return result

def insurance_fee(post_commission):
    fee = int(input("Please enter the title insurance fee: \n"))
    result = post_commission - fee
    return result

#Arguments passed to the method include the sale price and the following which must be deducted from the sale price: mortgage payoff, realtor's commission, title insurance fee.
def main():
   price = int(salePrice())
   #mortgage payoff
   post_mortgage = mortage_payoff(price)
   #realtor's commission
   post_commission = realtors_commission(post_mortgage)
   #InsuranceFee
   final_profit = insurance_fee(post_commission)
   print(final_profit)
main()