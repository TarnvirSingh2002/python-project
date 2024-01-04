# dic={'name':{'mac':'os', 'kls':'ced'},
#     'kno':'jxn' 'ikfm'}
# print(dic)
dic={}
for i in range(3):
    dic1={}
    for ii in range(2):
        course=input("enter the course name:")
        fee=int(input("enter fee:"))
        dic1.setdefault(course,fee)
    name=input("enter name of the candidate:")
    dic.setdefault(name,dic1)
print(dic)
