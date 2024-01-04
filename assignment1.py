items=int(input('Enter the number of items you want to buy:'))
d=0
if(items<10):
    d=120
if(items>=10 and items<=99):
    d=100
if(items>=100):
    d=70
print('Your total cost is:',items*d)
                             