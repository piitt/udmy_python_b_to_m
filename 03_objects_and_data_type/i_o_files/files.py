myfile = open('myfile.txt')
myfile.read()
myfile.seek(0)
content = myfile.read()
print(repr(content))
myfile.seek(0)
content = myfile.readlines()
print(repr(content))
myfile.close()

# mode=|'r'|'w'|'a'|'w+'|'r+'|
with open('myfile.txt', mode='r') as my_file:
    content = my_file.read()
print(repr(content))

with open('new_myfile.txt', mode='a') as f:
    f.write('Четыре на четвертой строке')
