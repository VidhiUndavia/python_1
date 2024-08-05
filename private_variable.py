class student:
    def __init__(self,name,password) :
        self.name=name
        self.__password=password
        print("Constructor called")
    def display(self):
        print("Name = ",self.name)
        print("Password = ",self.__password)

stud=student("drashti","123456")
stud.display()
print("------------------------------------")
print("Name ",stud.name)
try:

    print("Password ",stud.__password)
except AttributeError:
    print("Private variable password not accesible outside the class")
        