name=input("enter string:")
k=len(name)
k-=1
l=""
def reverse(name,k):
    global l
    if(k>=0):
        l+=(name[k])
        reverse(name,k-1)
    return l   
print(reverse(name,k))
