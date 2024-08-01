class person:
    def walk(self):
        print("Person can walk")
    def talk(self):
        print("Person can talk")
    def eat(self):
        print("Person can eat")
class student(person):
    def read(self):
        print("student can read")
    def write(self):
        print("student can write")
    def whatIcanDo(self):
        self.read()
        self.write()
        super().walk()
        super().talk()
        super().eat()

p1=person()
p1.walk()
p1.talk()
p1.eat()
print("--------------------------------------")
s1=student()
s1.read()
s1.write()
s1.whatIcanDo()
print("---------------------------------------")
s1.eat()
s1.walk()
s1.talk()