num=int(input("enter one number:"))
lnum=int(input("enter last number:"))
def multi(num,lnum):
    if(num<=lnum):
        print(num)
        multi(num+1,lnum)
multi(num,lnum)