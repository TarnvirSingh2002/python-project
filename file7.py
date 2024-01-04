import os
k=input("enter the file name:")
if(os.path.exists(k)):
    t=os.listdir(k)
    for i in t:
        print(i)
        if(os.path.exists(i)):
            tt=os.listdir(i)
            for ii in tt:
                print(ii)
        

    
    
