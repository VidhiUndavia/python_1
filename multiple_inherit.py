class base1:
    def __init__(self,name):
        self.name=name
        print("Base1 class constructor called")
    def display(self):
         print("Name = ",self.name)

class base2:
    def __init__(self,surname):
        self.surname=surname
        print("Base2 class constructor called")
    def display(self):
         print("Surname = ",self.surname)

class base3:
    def __init__(self,course):
        self.course=course
        print("Base3 class constructor called")
    def display(self):
         print("Course = ",self.course)
    
class derived(base1,base2,base3):
    def __init__(self,name,surname,institute,course):
        base1.__init__(self,name)
        base2.__init__(self,surname)
        base3.__init__(self,course)
        self.institute=institute
        print("Derived class constructor called")

    
    def printfun(self):
       base1.display(self)
       base2.display(self)
       base3.display(self)
       print("Institute = ",self.institute)
       print("Display method called")

b1=base1("drashti")
b1.display()
d1=derived("Drashti","Mehta","The easy learn academy","python")
d1.printfun()

# output
# Base1 class constructor called
# Name =  drashti
#Base1 class constructor called
# Base2 class constructor called
# Base3 class constructor called
# Derived class constructor called
# Name =  Drashti
# Surname =  Mehta
# Course =  python
# Institute =  The easy learn academy
# Display method called
