class person:
    def __init__(self,name,idnum):
        self.name1=name
        self.idnum1=idnum
    def display(self):
        print("Name = ",self.name1)
        print("idnum = ",self.idnum1)
class employee(person):
    def __init__(self, name, idnum,salary,post):
        super().__init__(name, idnum)
        self.salary1=salary
        self.post1=post
    def display(self):
         super().display()
         print("Salary = ",self.salary1)
         print("Post = ",self.post1)
name="Drashti"
idnum=101
p1=person(name,idnum)
p1.display()

name=input("Enter your name")
idnum=idnum+1
e1=employee(name,idnum,5000,"manager")
e1.display()
