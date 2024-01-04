def multi(num,lnum):
    if(num<=lnum):
        print(num)
        multi(num+1,lnum)
def find(num,k):
    l=0
    for i in range(5):
        if(num[i]==k):
            l=1
            print(k,"found in list")
    if(l==0):
        print("no")
