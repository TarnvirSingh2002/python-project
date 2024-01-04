num=[]
for i in range(10):
    num.append(int(input("enter one number:")))
for i in range(10):
    if(i%2==0):
        num[i],num[i+1]=num[i+1],num[i]
    print(num[i])

