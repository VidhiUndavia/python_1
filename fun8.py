def calculation(a,b):
    add=a+b
    sub=a-b
    return add,sub
answer=calculation(60,50)
print(answer)
for i in answer:
    print(i," = ",end=' ')
    print(answer.index(i),end=' ')
    print("square of ",i," = ",i*i)
    answer[i]=10
    