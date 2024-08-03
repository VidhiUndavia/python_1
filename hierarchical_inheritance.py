class person:
    def __init__(self,name):
        self.name=name
        print("Base class constructor")
    def display(self):
        print("Name = ",self.name)
class student(person):
    def __init__(self,name,course):
        super().__init__(name)
        print("Student class constructor")
        self.course=course
    def display(self):
        super().display()
        print("Course = ",self.course)
class teacher(person):
    def __init__(self,name,subject):
        super().__init__(name)
        print("Teacher class constructor")
        self.subject=subject
    def display(self):
        super().display()
        print("Subject = ",self.subject)


s1=student("Drashti","MCA")
s1.display()

t1=teacher("Vidhi","Python")
t1.display()

# output
# Base class constructor
# Student class constructor
# Name =  Drashti
# Course =  MCA
# Base class constructor
# Teacher class constructor
# Name =  Vidhi
# Subject =  Python