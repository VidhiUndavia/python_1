filename="first.py"
mode="w"

file=open(filename,mode)
file.write("num=int(input('enter the number'))\n")
file.write("for i in range(1,11,1):\n")
file.write("    print(num,' * ',i,' = ',i*num)\n")

file.close()