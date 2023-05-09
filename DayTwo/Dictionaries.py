# in list we have index method to store values 

# but know you are gonna see by key values storage thanks to 
# dictionaries

import sys

dic1 = {"key1":123,"key2":123,"key3":4}

print(dic1["key1"])

prices_Tr = {"et":200,"onion":20}

print(prices_Tr["et"])
# to add  
prices_Tr["patates"] = 40


print(len(prices_Tr)) # !!! 

for i  in prices_Tr.values():
    print(f"this is the value {i}")

# pop 
prices_Tr.pop("et")
print(prices_Tr)


