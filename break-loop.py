given_list=[1,3,5,1,-2,-3] #list is always arranged in descending order
total=0
for element in given_list:
    if element <=0:
        break
    total+=element
print(total)   

###########################################

given_list=[1,3,5,1,-2,-3] #list is always arranged in descending order
total=0
i=0
while True:           #assuming the list contains atleast one non-positive element
    total+=given_list[i]
    i+=1
    if given_list[i]<=0:
        break
print(total)    

