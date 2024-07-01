count=int(input("How many odd numbers u want to print from 1"))
num=1

while num<=count:
    if num%2!=0:
        print(num," number is odd")
    else:
        print(num, "number is even")
    num=num+1