lst = [1,23,124,1212,321,23,40,0,0,0,1,0]
new_lst = []
count = 0
for i in lst:
    if i !=0:
        new_lst.append(i)
    else:
        count+=1

print(new_lst)