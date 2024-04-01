total2=0
j=1
while j<5:
    total2+=j
    j+=1
print(total2)

#########################

#to print only the positive elements of the list

given_list=[5,4,4,3,1,-2,-3,-5]
total3=0
i=0
while given_list[i]>0:        
    #applies only when atleast one non-positive element present in the list.
    #give indexerror when all elements are positive.
     total3 +=given_list[i]
     i+=1
print(total3)  

#to rectify this,

given_list1=[5,4,4,3,1,2,3,5]
total4=0
i=0
while i<5 and given_list1[i]>0:
    total4 +=given_list1[i]
    i+=1
print(total4)

#whwn no.of elements is unknown

given_list1=[5,4,4,3,1,2,3,5]
total4=0
i=0
while i<len(given_list1) and given_list1[i]>0:
    total4 +=given_list1[i]
    i+=1
print(total4)

  