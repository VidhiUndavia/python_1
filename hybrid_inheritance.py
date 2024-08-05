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
        print("Grandchild1 class constructor")
    def display2(self):
        
        print("City = ",self.city)
        print("Grand child class display method called")


class child2(parent):
     def __init__(self,name,state):
        super().__init__(name)
        self.state=state
        print("Child2 class constructor")
     def display3(self):
        
        print("State = ",self.state)
        print("Child2 class display method called")

g1=grandchild("Drashti","Mehta","Bhavnagar")
g1.display()
g1.display1()
g1.display2()

print("---------------------------------------------")
c1=child2("vidhi","Gujarat")
c1.display3()
c1.display()