num=[]
for i in range(5):
    num.append(int(input("enter one number")))
k=int(input("enter one u want to find number"))
i=len(num)
i-=1
kk=0
def find(num,k,i):
    global kk
    if(i>=0):
        if(num[i]==k):
            kk+=1
        find(num,k,i-1)
    if(kk>0):
        return ('yes')
    else:
        return ('no')
print(find(num,k,i))