li=[]
i=0
k=0
while(i<3):
    li1=[]
    k=0
    while(k<3):
        li1.append(int(input("enter one number:")))
        k+=1
    li.append(li1)
    i+=1
kk=0
print(sum(li[0]))
for i in range(3):
    for k in range(3):
        kk+=li[i][k]

print(kk)
