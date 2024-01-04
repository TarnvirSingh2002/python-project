a=input('Enter name of your movie:')
rating=float(input("Rate this movie from 0 to 5:"))
if(rating<=2.0):
    print(a,' movie is Flop')
elif(rating>=2.1 and rating<=3.4):
    print(a," movie is semi-hit")        
elif(rating>=3.5 and rating<=4.5):
    print(a," movie is hit") 
elif(rating>=4.6 and rating<=5.0):
    print(a," movie is superhit") 