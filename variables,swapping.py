a=1
b=2
c="variables"
d=2 #same value can be contained by two variables
b=1 #b now refers to 1, not 2
f=a #f refers to the value a is refering to
print(a+b) #1+1=2
print(f)
a=3
print(f) # f refers to the same old value of "a" that is 1.
f=a #now f refers to the recent value of "a" that is 3.
print(f)
print(c)

###################################

#***Swapping two variables***

v1="first string"
v2="second string"
c=v1  #using two variables
d=v2

c=d
d=v1

print(c,d)

v1=d
v2=c

print(c,d)

c=v1  #using one variable(this is best one)
v1=v2
v2=c

print(v1,v2)