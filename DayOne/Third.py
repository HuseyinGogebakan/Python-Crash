

str = "abcdefgh"


print(str)
print(str[2:])
print(str[2])

print(str[2:6])


print(str[2::2])


print(str[3::-1])

str = str[2]

#string is immuteable watch out!

# its a error str[1] = '1'

print(str)


#repeat method for py 

print(str*8)

# sum the strings
print('2'+'3') # 23

# uppper case and lower case
 
upper = str.upper()
lower = str.lower()

ira = "ira hominis non implet justitiam dei"
#split
print(ira.split())
# or with the regrex
print(ira.split('i'))

nam ="Hadrem {}'i cennet ve dugendim bi {}".format("revadai","furuht")

print(nam)
#or 
wrong_nam = "Hadrem {s}'i cennet ve dugendim bi {q}".format(q="revadai",s="furuht")

print(wrong_nam)

# Float formatting

result = 100/777 # something around 0.128

print("The result was {r:2.3f}".format(r=result))
#voila it doesnt give more zero because it has no value


name = "Kurban"

print(f"Hello, his name is {name}") # *.* damn 

name = "Habib"
age = 36
print(f"{name} is {age} yo")


print(set("Mississippi"))

print("parallel".split())


# split
str ="We must win this time"
str.split()

# list for every letter
list(str)

# upper lower
str.upper()
str.lower()

# format

print("this is  a test of {}".format(str))

print(f"this is  a test of {str}")

# strip == trim
print(len(" da sda ".strip()))

# replace 
print("pahadir".replace("p","b"))



# starts with 
print("da hata".startswith("da"))

# str int float input !!! 

# \n method !

# contains 
print("win" in str)

if "lose " not in str:
    print("no option to lose exists!")


# find and rfind
print("sadasd".rfind("s"))

print("sadasd".find("s"))