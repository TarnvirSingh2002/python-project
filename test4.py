l=[]
restaurant_name=''
while(restaurant_name!='done'):
    restaurant_name=input("enter restaurant name:")
    if(restaurant_name!='done'):
        l1=[]
        if(restaurant_name!='done'):
            price_range=int(input("enter price range from 1 to 5:"))
            m=''
            while(price_range>0):
                m+='$'
                price_range-=1
            l1.append(restaurant_name)
            l1.append(m)
        l.append(l1)
print(l)
    




