file = open('test.txt')
#print(file.read(2))

#print(file.readline())
#print(file.readline())

#file.close()

#line = file.readline()

#while line != "":
#   print(line)
#    line = file.readline()

#file.close()


for line in file.readlines():
    print(line)

file.close()