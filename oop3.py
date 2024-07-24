class student:
    institute="The easy learn academy"
    rollno=0
    name=" "
    def __init__(self,no,name1):
        print("This is constructor")
        print("rollno = ",self.rollno)
        print("Name = ",self.name)
        self.rollno=no
        self.name=name1
    def showData(self):
        print("This is member function")
        print("Institute = ",self.institute)
        print("Roll no.= ",self.rollno)
        print("Name = ",self.name)
rollno=int(input("Enter rollno = "))
name=input("Enter Name = ")

stud1=student(rollno,name)
stud2=student(102,"Vidhi")
stud1.showData()
stud2.showData()