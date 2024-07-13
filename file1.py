filename="simple1.py"
mode="r"

file=open(filename,mode,1)

for line in file:
    print(line)

file.close()
