id_proof=1
nationality=1
age=2
if id_proof==1:
    print("yes")
    if nationality==1:
        print("yes1")
        if age>=18:
            print(age)
        else:
            print("no2")
    else:
        print("no1")
else:
    print("no")