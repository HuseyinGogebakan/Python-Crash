
d = {"key":12,"key01":34}

for  each in d:
    print(each+": ",end='')
    print(d[each])


for key, value in d.items():
    print(key+" :",value)


x = 1 

while x<5:
    print(f'the {x}th value')
    x+=1

else: 
    print("x is at a point that more than 5 ")