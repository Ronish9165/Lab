#Price of a house is $1M. If buyer has good credit, they need to put down 10% other wise they need to put down 20%.
#Print the down payment.

price=1000000
credit_score=input("Enter if the buyer has good credit:")
if credit_score=='yes':
    credit_score=True
if credit_score==True:
    downpayment=(10/100)*price
else:
    downpayment=(20/100)*price
print("The price of the house is",downpayment)


#price=1000000
#credit_score=True
#if credit_score==True:
#   downpayment=(10/100)*price
#else:
#   downpayment=(20/100)*price
#print("The price of the house is",downpayment)
