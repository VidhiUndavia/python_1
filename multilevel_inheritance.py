class parent:
    def __init__(self,name) :
        self.name=name
        print("Parent class constructor")
    def display(self):
        print("Name = ",self.name)
        print("Parent class display method called")
class child(parent):
    def __init__(self,name,surname):
        super().__init__(name)
        self.surname=surname
        print("Child class constructor")
        print("Name = ",self.name)
    def display1(self):
       
        print("Surname = ",self.surname)
        print("Child class display method called")
class grandchild(child):
    def __init__(self,name,surname,city):
        super().__init__(name,surname)
        self.city=city
        print("Grandchild class constructor")
    def display2(self):
        
        print("City = ",self.city)
        print("Grand child class display method called")


g1=grandchild("Drashti","Mehta","Bhavnagar")
g1.display()
g1.display1()
g1.display2()

# output
# Parent class constructor
# Child class constructor
# Name =  Drashti
# Grandchild class constructor
# Name =  Drashti
# Parent class display method called
# Surname =  Mehta
# Child class display method called
# City =  Bhavnagar
# Grand child class display method called