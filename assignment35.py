name=input("enter string:")
i=0
upper=0
digit=0
small=0
for i in name:
    if(i.islower()):
        small+=1
    if(i.isupper()):
        upper+=1
    if(i.isdigit()):
        digit+=1
    
print('upper=',upper)
print('smaller=',small)
print('digits=',digit)
