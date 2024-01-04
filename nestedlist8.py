num=[]
num1=[]
word=[]
k=[]
for i in range(5):
    num.append(int(input("enter number:")))
for i in range(5):
    word.append(input("enter string:"))
for i in range(5):
    num1.append(int(input("enter number:")))
for i in range(5):
    k.append(str(num[i])+word[i]+str(num1[i]))
for i in range(5):
    print(k[i])

