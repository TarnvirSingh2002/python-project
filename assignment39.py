n=input("Enter any name")
n=n.upper()
i=len(n)-1
k=0
kk=1
while(k<len(n)):
    print(n[k],end="\t")
    k+=1
print()
d=1
end=len(n)-2
while(kk<len(n)-1):
    print(n[d],end="\t")
    d+=1
    for y in range(0,len(n)-2):
        print(" ",end='\t')
    kk+=1
    print(n[end],end='')
    end-=1
    print()
while(i>=0):
    print(n[i],end="\t")
    i-=1