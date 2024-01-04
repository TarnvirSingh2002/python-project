num=int(input('Enter one number:'))
k=num
rev=0
while(num>0):
    a=num%10
    rev=(rev*10)+a
    num=num//10
if(rev==k):
    print("palindrome")
else:
    print("not palindrome")