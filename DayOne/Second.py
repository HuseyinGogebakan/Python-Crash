
# input 


print("hey ")
times = input('kac kere massalah?')


print('kac kere massalah',times )# no + sign as you have on java11 dont forget it adds always a space
print(times,'kere massallah',sep='') # as you can see!

vote = input("oyunuz nereye? ")
if(vote == "chp"):
    print("you have one more chance")
elif (vote == "akp"):
    print("welcome to hell")
    if True:
        print("nothing")

#tab to enter elif !    
x = input("enter the value")


score = float(input("Enter Score: "))
if 1<score:
	print("the value is out of the range")
    
elif score>= 0.9:
	print("A")
elif score >= 0.8:
	print("B")
    
elif score >= 0.7:
	print("C")
elif score >=0.6:
	print("D")
else: 
	print("F")