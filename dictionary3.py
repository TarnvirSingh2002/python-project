student={}
student1=[]
for i in range(3):
    stu=input("enter student:")
    name=input('enter name:')
    student.setdefault(stu,name)
print(student)
for i in student:
    student1.append(list(student[i]))
print(student1)
student1.sort()
print(student1)

