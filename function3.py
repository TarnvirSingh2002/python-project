p=int(input("enter one number: "))
lnum=0
def multi(p,lnum):
    if(lnum<=10):
        print(p,'*',lnum,"=",p*lnum)
        multi(p,lnum+1)
multi(p,lnum)
