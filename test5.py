num=int(input("enter one number between 1 to 20:"))
for i in range(num+1,101):
    if(i%7!=0):
        num*=i
        if(num>5000):
            print('big product')
print(num)
