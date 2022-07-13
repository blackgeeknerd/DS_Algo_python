f = open('files/files.txt')
# print(f.read)
for i in f:
    print(i)
# print(f.encoding)
# print(f.readline())
# print(f.readline())
f.close()

#appending text to the end of the file
f = open('files/files.txt', 'a')
f.write("\t My regards to the family")
f = open('files/files.txt', 'r')
# print(f.read())
f.close()

#overwriting the content of the file
f = open('files/files.txt', 'w')
f.write("Damn i deleted the contents")
# f.close()
f = open('files/files.txt', 'r')
print(f.read())