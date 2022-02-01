a=(float)(input(""))
b=(float)(input(""))

BMI= a/(b*b)

if BMI> 25: print("Overweight")
elif BMI<18.5: print("Underweight")
elif BMI >= 18.5 and BMI <= 25: print("Normal weight")
