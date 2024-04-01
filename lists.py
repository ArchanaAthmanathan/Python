a=[10,-1,2,3]
print(a)

a.append(4)               #appending
print(a)

a.append("hello")         #both numbers and strings can be appended in python
print(a)

a.append(["world",5,])      # can add lists into list 
print(a)

a.pop()         #to delete last item
print(a)

a.pop()
print(a)

print(a[0])     #retreving item with index "0"
                # careful of which brackets are used where

a[0]=8          #to change value of list element
print(a)          
                