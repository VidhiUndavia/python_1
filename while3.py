num=int(input("Enter number u want to reverse "))
reverse=0
while num>0:
    reminder=num%10
    num=int(num/10)
    reverse=reminder+(reverse*10)
print("reverse = ",reverse)