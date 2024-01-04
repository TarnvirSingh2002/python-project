num=[]
for i in range(5):
    num.append(int(input("enter one number:")))
n=input("enter string")
for i in range(5):
    num[i]=n+str(num[i])
for i in num:
    print(i)