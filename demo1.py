from mymath import addition,subtraction
from fun2 import getcube
 
# import mymath, fun2

num1=int(input("Enter the first number"))
num2=int(input("Enter the second number"))
add=mymath.addition(num1,num2)
print("Addition = ",add)
print("----------------------------------------")
fun2.getcube()
print("----------------------------------------")
mymath.subtraction()
print("----------------------------------------")

num1=int(input("Enter the first number"))
num2=int(input("Enter the second number"))
mymath.multiplication(num1,num2)
print("----------------------------------------")
div=mymath.division() 
print("Division = ",div)

