fileread=open("list1.py")
filewrite=open("second.py","w")

for line in fileread:
    print(line)
    filewrite.write(line)
filewrite.close()
fileread.close()