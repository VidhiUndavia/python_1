fruit1=["strawberry","pineapple","pineapple","orange"]
s=","

print(s.join(fruit1))

python={"name":"Python","price":4500,"duration":90}
print(s.join(python))

touple2=("99","MCA","99.99","gurukul")
print(s.join(touple2))

animal={"Dog","Cow","Cat","ret"}
print(s.join(animal))

sentance="Good morning, this morning is full of sunlight and happiness, haave a great morning"
print("Original = ",sentance)
print("New = ",sentance.replace("morning","night"))

print("New = ",sentance.replace("morning","night",2))

s='e'
name="Theeasylearnacademy"
list1=name.split(s)
print(list1)