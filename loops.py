a=["banana","apple","microsoft"]
for element in a:
    print(element)
     
############################

#to add all elements
     
b=[20,10,9]   
total=0
for e in b:
    total=total+e
print(total)
    
############################

#using range function
#1,2,3,4,...100

c=list(range(1,101))  #stating from 1 and end before 101(i.e)1 to 100
print(c)

for i in range(1,5):
    print(i)


total2=0
for i in range(1,101):
    total2+=i
print(total2)    
########################################
#adding only numbers which are multiples of three in list 1 to 7 

print(list(range(1,8)))
total3=0
for i in range(1,8):
    if i%3==0:
        total3+=i
print(total3)        
