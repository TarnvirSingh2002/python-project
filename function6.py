# i=0
# while(i<10):
#     a=int(input("enter 10 numbers:"))
#     i+=1
# i=0
# while(i<10):
#     print(a[i])
#     i+=1
# # print(type(a))
n=""
name=input("enter a name:")
k=len(name)
k-=1
t=0
def rev(name,k):
    global t
    if(k>=0):
        if(name[k]=='a' or name[k]=='e'or name[k]=='i' or name[k]=='o' or name[k]=='u'):
            t+=1
        rev(name,k-1)
    if(t==0):
        return ("not vowel")
    else:
        return ('vowel')
print(rev(name,k))
    