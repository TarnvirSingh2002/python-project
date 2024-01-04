p=int(input("enter bigger number:"))
q=int(input("enter smaller number:"))
while(q<=p):
    if(q%10==7 or q%7==0):
        print(q,"is buzz number!")
    q+=1
