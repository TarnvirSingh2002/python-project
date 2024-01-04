a=1
while(a<101):
    if(a%5==0 and a%3==0):
        print("Fizzbuzz")
    elif(a%3==0):
        print("Fizz")
    elif(a%5==0):
        print("buzz")
    else:
        print(a)
    a+=1