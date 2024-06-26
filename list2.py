fruit=["apple","banana","mango","graps","watermelon"]
print(fruit)
fruit.append("chicoo")
print(fruit)

fruit1=["strawberry","pineapple","pineapple","orange"]

fruit.extend(fruit1)
print(fruit)

fruit.insert(8,"blackberry")
print(fruit)
'''fruit.remove("pineapple")
print(fruit)
fruit.remove("pineapple")
print(fruit)'''
print(fruit.pop(6))
print(fruit)
print(fruit.index("blackberry"))
print(fruit.count("pineapple"))
fruit.sort()
print(fruit)
fruit.reverse()
print(fruit)
fruit2=fruit.copy()
print(fruit2)
fruit2.clear()
print(fruit2)