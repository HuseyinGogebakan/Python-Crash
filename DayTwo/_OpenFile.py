myfile= open("myfile.txt")


print(myfile.read())
myfile.seek(0) # to read again !

print(myfile.read())
myfile.seek(0)

myfile.readlines(1).append(" or not? ")
myfile.seek(0)
print(myfile.read())


# after done close it


myfile.close()

# no  need to close file this way 
with open('myfile.txt') as my_new_file:
    contents = my_new_file.read()
    print(contents)


with open("myfile.txt",mode='r+' ) as myfile: # writing reading appedin
    contents = myfile.read()

with open('myfile.txt',mode='a') as f:
    f.write("\nFour on fourth")


with open('myfile.txt',mode='r') as f:
    print(f.read())

with open('myfile.txt',mode='w+') as f:
    f.write('I created this file!')


with open('myfile.txt',mode='r') as f:
    print(f.read())


# open
# read
# readlines index

# close

# with open x , mode ="r w a r+ w+ a+" as bilemem_ne:
