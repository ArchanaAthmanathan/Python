a=6
b=2
if a<b:
    print("a is less than b")
else:    
    print("a is not less than b")
print("outside the if block")

#####################################

a=4
b=4
if a<b:
    print("a is less than b")
elif a==b:                       # we can have multiple elif clauses
    print("a is equal to b") 
else:    
    print("a is greater than b")

#####################################

a=15
b=4
if a<b:
    print("a is less than b")
elif a==b:        
    print("a is equal to b")
elif a>b+10:                                      # we can have multiple elif clauses
    print("a is more than 10 greater than b ")     
else:    
    print("a is greater than b")
    
#################################
 #***Nested If-Else ***

a=6
b=2
if a<b:
    print("a is less than b")
else:
  if a>b:    
    print("a is not less than b")
  else:
    print("a is equal to b")
    

    
