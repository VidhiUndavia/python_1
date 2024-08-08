class parent:
    def walk(self):
        print("Person can walk")
    def talk(self):
        print("Person can talk")
class student(parent):
    def read(self):
        print("Person can read")
    def walk(self):
        print("Student can walk")
        print("--------------------------")
        super().walk()
p1=parent()
p1.walk()
p1.talk()
print("------------------------")
s1=student()
s1.walk()
s1.read()
s1.talk()