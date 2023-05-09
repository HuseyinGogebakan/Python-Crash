

list01 = [1,2,3,4,5,6,7,8]

print(list01[2])


print(list01[2:4])
# just like strings but changable 

list01[2] = "changable"

print(list01) # [1, 2, 'changable', 4, 5, 6, 7, 8]

# to add 

list01.append("six")

print(list01) #[1, 2, 'changable', 4, 5, 6, 7, 8, 'six']

#to delete

list01.pop()

popped_item = list01.pop() # popped item is "six"

print(list01.pop(0)) # is  0


#sorting method
sorted_list = [5,2,1,4,21]
sorted_list.sort()
print(sorted_list)

# Reverse version

sorted_list.reverse()
print(sorted_list)
print(len(sorted_list))
