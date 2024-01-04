ii=0
while(ii<10):
    i=int(input('enter one number'))
    if(i%5==0):
        print("divisible")
        if(i%10==0):
            print("ending number is 0!")
        else:
            print("ending number is 5!")
    else:
        print("not divisible")
    ii+=1



