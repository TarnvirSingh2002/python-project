#Under review
# name=input("Enter your name:")
# address=input('Enter your address:')
a=input('Enter the item you want to buy:')
rate=int(input('Enter the price of your product:'))
discount=0
if(a=='L'):
    if(rate<=25000):
        discount=0
    elif(rate>25000 and rate<=35000):
        discount=(5*rate)/100
        print(discount)
elif(a=='D'):
    if(rate<=25000):
        discount=(5.0*rate)/100.0
    elif(rate>25000 and rate<=35000):
        discount=(7.5*rate)/100.0
print(rate-discount)