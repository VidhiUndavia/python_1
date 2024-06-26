#create dictionary 
python = {"name":"python","duration":90,"fees":7500.99,"isCertified":True,"random":"random"}
print(python)
python["name"]="c++"
print(python)
del python["random"]
print(python)


book={}
print(book)
book["name"]="python"
book["weight"]=2.0
book["price"]=500
book["year"]=2024
print(book)

python1=python.copy()
print(python1)
print("--------------------------------------------")
print(python.keys())

print(python.values())

student = ['name','surname','age','gender']

vidhi = dict.fromkeys(student)

print(vidhi)
vidhi['name'] = "Vidhi"
vidhi['gender'] = False
print(vidhi)

print(python.items())

print(python.get("duration"))
print(python['duration'])


print(python.get("trainer","not available"))
print(python)
# print(python['trainer']) #error

print(python.pop("duration"))
print(python)
print(python.popitem())
print(python)
python.update({"duration":90})
python.update({"duration":70})
print(python)
python.clear()
print(python)
