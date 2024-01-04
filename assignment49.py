name=[]
name1=[]
n=[]
m=[]
i=0
n=""
while(i<5):
    name.append(input("enter name:"))
    i+=1
i=0
kk=1
'''while(i<5):
    k=len(name[i])
    while(kk<=k):
        n+=name[i][-kk]
        kk+=1
        name1.append(m)
    i+=1
i=0'''
while(i<5):
    name1.append(name[i][::-1])
    i+=1


for i in name1:
    print(i)

