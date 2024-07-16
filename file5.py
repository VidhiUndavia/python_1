fileread=open("list1.py")
filewrite=open("second.py","a")

for line in fileread:
    print(line)
    filewrite.write(line)
filewrite.write("\n")
filewrite.close()
fileread.close()