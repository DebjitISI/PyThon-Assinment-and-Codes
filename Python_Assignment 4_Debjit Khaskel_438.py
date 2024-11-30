import math as mt
##Assignment 4
##1.Check even or odd
a=int(input("Enter a positive integer:\n"))
if a%2==0:
    print("The entered number is even.")
else:
    print("The entered number is odd.")
print()
##2.input hgt and weight and calculate BMI=weight/(height)^2
height=float(input("Enter your height in meter:"))
weight=float(input("Enter your weight in kg:"))
if height>0.0 and weight>0.0:
    bmi=weight/mt.pow(height,2)
    if bmi>=35:
        print("Clinically obese.")
    elif bmi>=30:
        print("Obese.")
    elif bmi>=25:
        print("Slightly overwight.")
    elif bmi>=18.5:
        print("Normal Weight.")
    else:
        print("Underweight.")
else:
    print("INVALID INPUT!!")
