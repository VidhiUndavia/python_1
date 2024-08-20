import random as r1

print("Random number=",r1.random())
print("Random number=",r1.uniform(99,999))
print("Random number=",r1.randint(99,999))
print("Random number=",r1.randrange(0,999,7))

fruit1=["strawberry","pineapple","pineapple","orange"]
print("Random fruit = ",r1.choice(fruit1))
print("Random fruit = ",r1.choices(fruit1,k=2))

list1=[3,3,7,8,3,9,56,89,9,1,2]
print("Original = ",list1)
r1.shuffle(list1)
print("After first shuffle = ",list1)
r1.shuffle(list1)
print("After second shuffle = ",list1)
list1=[3,3,7,8,3,9,56,89,9,1,2]
print("Sample shuffle = ",r1.sample(list1,4))


