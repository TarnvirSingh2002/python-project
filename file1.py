import os
import pickle
name=input("enter name:")
if(os.path.isfile(name) and os.path.exists(name)):
    k=open(name)
    print(k.read())
else:
    k=open(name,"wb")
    kk=(input("what you want to write:"))
    #k.write(kk)
    pickle.dump(kk,k)
    k.close()