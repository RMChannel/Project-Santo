file=open("input.txt",'r',encoding="utf8")
for line in file.readlines():
    print(line)
file.close()