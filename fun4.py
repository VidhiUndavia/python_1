#no argument,with return value
def getcube():
    num=int(input("Enter number"))
    answer=num*num*num
    return answer

  


answer=getcube()
print("answer = ",answer)