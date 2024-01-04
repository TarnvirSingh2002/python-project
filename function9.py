# name1=input("Enter one number:")
# name2=input("enter one more number")
# def check(name1,name2):
#     if(name2==name1):
#         print("same")
#     else:
#         print("not same")
# check(name2,name1)
    #    # new program
l=[]
for i in range(5):
    l.append(int(input("enter one number:")))
def larg(l):
    large=l[0]
    for i in l:
        if(i>large):
            large=i
    print("largest value=",large)
larg(l)    