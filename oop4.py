class student:
    
    def __init__(self):
        print("This is constructor")
        self.institute="The easy learn academy"
        self.rollno=0
        self.name=" "
    def getData(self):
        rollno=int(input("Enter rollno = "))
        name=input("Enter Name = ")
        self.rollno=rollno
        self.name=name
    def showData(self):
        print("This is member function")
        print("Institute = ",self.institute)
        print("Roll no.= ",self.rollno)
        print("Name = ",self.name)


stud1=student()
stud2=student()
stud1.getData()
stud2.getData()
stud1.showData()
stud2.showData()