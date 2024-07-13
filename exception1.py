num1=int(input("enter the number"))
num2=int(input("enter the number"))

try:
    print("hi")
    answer=num1/num2
    print(answer)
   
except ZeroDivisionError:
    print("enter grater number then 0")
