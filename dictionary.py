student={"stu1":"Manpreet","stu2":"taranvir","stu3":"rajat","stu3":"Akriti"}
print(student.values())

print(student.get("stu1"))
print(student.items())
print(student.keys())
print(student.pop("stu2"))
print(student.popitem())
student.setdefault("stu4","kanika")
print(student)
for i in student:
    print(student[i])
student=student.clear()
print(student)