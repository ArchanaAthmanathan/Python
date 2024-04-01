name="xyz"
height_m=2
weight_kg=80

BMI=weight_kg/(height_m**2)  #Formula for calculating BMI of a person

print(BMI)

if BMI<25:
    print(name,"is not overweight")
else:
    print(name,"is overweight")
