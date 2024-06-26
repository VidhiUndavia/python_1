python={"name":"Python","price":4500,"duration":90}
print(python)

student=["name","surname","subject","rollno"]
student1=dict.fromkeys(student)
print(student1)

student1['name']="Drashti"
student1['surname']="Mehta"
student1['subject']="Python"
student1['rollno']=10

print(student1)

print(student1.items())

student1['name']="Vatsal"
print(student1.items())

print(student1.get('nam',"NOT AVAILABLE"))

stud_info=python.pop(('duration'))
print(stud_info)
print("-----------------------------------------------\
      ------------------------------------------------------\
      -----------------------------------")
print(python)
print(student1.popitem())
print(student1)
student1.update({"ROLLNO":9})
print(student1)
student1.update({"ROLLNO":10})
print(student1)
student1.clear()
print(student1)

num1=input("Enter the number")
print(num1)