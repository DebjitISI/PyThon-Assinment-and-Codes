## String Indexing
##word="My name is Debjit Khaskel"
##print(word[::2])
string="Data Science"
##print(string[0])
##print(string[1])
##print(string[4])
##print(string[-1])
##print(string[-2])
##print(string[1:3])
##print(string[0:3])
##print(string[:3])
##print(string[1:])
##print(string[::2])

## 18. Create a string containing just the first three letters of the string "Data Science".
##print(string[0:3])
##
#### 19. print the string "Sci" by using slice notation on the string "Data Science" to specify the correct range of characters.
##print(string[5:8])
##
#### 20. Alter the string "goal" to "coal" using slicing and cocatenation.
##print("c"+"goal"[1:])

## F STRING(Formatted string)

a=2
b=3
##print("The sum of",a,"and",b,"is",(a+b))
##print(f"The sum of {a} and {b} is {a+b}")

##name=input("Enter your name:\n")
##
##print("My name is ",name)
##
##name.lower()
####print(name.capitalize())
##
##name_upp=name.upper()
##print("Hello!",name_upp)

##
##Age=input("Enter your age:\n")
##print(2*Age)
##print(f"After 5 years the age will be {5+int(Age)} years.")
##print("After 5 years the age will be "+str((5+int(Age)))+" years.")

##name="House"
##Windows=4
##doors=2
##print(f"The {name} has {Windows} Windows and {doors} doors.")

## OPERATORS

##1. Arithmetic Operators
## -> +:addition
##-:subtraction
##*:multiplication
##/:true division
##//:integer division
##%:modulo
##**:power

####1.
##print(f"\n2+3 and 2-3 is {2+3} and {2-3} respectively")
####2.
##print(f"\n2*3 and 2^3 is {2*3} and {2**3} respectively")
####3.
##print(f"\n2/3 is {2/3}")
####4.
##print(f"\nQuotient and the remainder of 10/7 are {10//7} and {10%7} respectively")
####5.
##print(f"\nCircumference and area of circle with radius 2 are {2*(22/7)*2} and {(22/7)*(2**2)}")
#### 6.
##print(f"The arithmatic mean of 1,2 and 3 is {(1+2+3)/3}")
##
####7.
##print(f"Execute the expression 3*3+3/3-3: {3*3+3/3-3}")
####8.
##x=5
##print(f"Solution to expression 5x^2 + 2x + 3 given x=5 is {5*(x**2) + 2*x + 3}")
####9.
##x=5
##y=2
##print(f"Solution to expression x^2 + 5(xy)^(1/2) + 2y^3 given x=5 and y=2 is {x**2 + 5*((x*y)**(1/2)) + 2*y**3}")
##
##print(len(string))
##print(pow(2,3))
##
##import math as m
##x=5
##y1=m.cos(m.radians(x))
##print(y1)
##y2=m.log(x)
##y3=m.log(x,10)
##print(y3)

## 
## 1.Take two values from the user store thm in 2 variables a and b and find the sum of the values. Print the sum of a and b is <sum>.
##2. take 2 values from user. Swap the values.(Home Work)
import math as mt
####1. taking user input and adding
##a=int(input("Enter a value for a:\n"))
##b=int(input("Enter a value for b:\n"))
##print(f"The sum of {a} and {b} is {a+b}")
##print()
##
####2. Swapping Values
##x=int(input("Enter a value for x:\n"))
##y=int(input("Enter a value for y:\n"))
##t=0
##t=x
##x=y
##y=t
##print(f"The swapped values of x and y is: {x} and {y} respectively.")

## AND OR NOT
##x=5
##print(x<5 & x<8)
##print(x>6 & x<8)
##print(x>6 | x<8)
##print(x>6 | x<3)
##print(not x==5)
##print(not x<5)

## if condition:
##      do this
## elif condition:
##      do this
## else:
##      do this

##1.
##x=float(input(f"Enter the marks (out of 100) of the student 'A':\n"))
##if x>=30:
##    print("Congratulation! you have passed the test.")
##else:
##    print("Good try! Best wishes dor the next time.")
##
##print()
####2.
##x=float(input(f"Enter the marks (out of 100) of the student 'A':\n"))
##if x<=100:
##    if x>=60:
##        print("Congratulation! you have passed first class.")
##    elif x>=30:
##        print("Congratulation! you have passed the test.")
##    else:
##        print("Good try! Best wishes dor the next time.")
##else:
##    print("Invalid Input!entered marks cannot be greater than 100.")
##
####Nested if else
#### if marks greater than 97 
##x=float(input("Enter the marks (out of 100) of the student 'A':\n"))
##if x>80:
##    print("Can Apply.")
##    if x>97:
##        print("Selected")
##    else:
##        print("Not Selected.")
##else:
##    print("Can't apply")
import math as mt
##Assignment 4
##1.
##a=int(input("Enter a positive integer:\n"))
##if a%2==0:
##    print("The entered number is even.")
##else:
##    print("The entered number is odd.")
##print()
####2.input hgt and weight and calculate BMI=weight/(height)^2
##height=float(input("Enter your height in meter:"))
##weight=float(input("Enter your weight in kg:"))
##if height>0.0 and weight>0.0:
##    bmi=weight/mt.pow(height,2)
##    if bmi>=35:
##        print("Clinically obese.")
##    elif bmi>=30:
##        print("Obese.")
##    elif bmi>=25:
##        print("Slightly overwight.")
##    elif bmi>=18.5:
##        print("Normal Weight.")
##    else:
##        print("Underweight.")
##else:
##    print("INVALID INPUT!!")

##n=int(input("Enter the value of n:\n"))
##for i in range(n):
##    if(i+1==1):
##        print(f"The{i+1}st element is:{i+1}")
##    elif(i+1==2):
##        print(f"The{i+1}nd element is:{i+1}")
##    elif(i+1==3):
##        print(f"The{i+1}rd element is:{i+1}")
##    else:
##        print(f"The{i+1}th element is:{i+1}")
##
##print(f"The sum of the n natural numbers are:{n*(n+1)/2}")
##print()
##n=int(input("Enter the value of n:\n"))
##sum=0
##for i in range(n):
##    sum+=i+1
##print(f"The sum of the n natural numbers are:{sum}")

##print()
##n=int(input("Enter the value of n:\n"))
##for i in range(n):
##    for j in range(i+1):
##        print(j+1,end='\t')
##    print("\n")

print()
n=int(input("Enter the value of n:\n"))
s=0
for i in range(n):
    for j in range(i+1):
        s+=1
        print(s,end='\t')
    print("\n")

