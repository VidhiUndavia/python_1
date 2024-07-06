#with argument ,with return value

def getcube(num):
    num=num*num*num
    print(num)
    return num

num=int(input("Enter number"))
answer=getcube(num)
print(num)
print("answer = ",answer)