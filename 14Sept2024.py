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
print(string[0:3])

## 19. print the string "Sci" by using slice notation on the string "Data Science" to specify the correct range of characters.
print(string[5:8])

## 20. Alter the string "goal" to "coal" using slicing and cocatenation.
print("c"+"goal"[1:])

## F STRING(Formatted string)

a=2
b=3
##print("The sum of",a,"and",b,"is",(a+b))
print(f"The sum of {a} and {b} is {a+b}")

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

name="House"
Windows=4
doors=2
print(f"The {name} has {Windows} Windows and {doors} doors.")

## OPERATORS

##1. Arithmetic Operators
## -> +:addition
##-:subtraction
##*:multiplication
##/:true division
##//:integer division
##%:modulo
##**:power

print(f"\n2+3 and 2-3 is {2+3} and {2-3} respectively")
print(f"\n2*3 and 2^3 is {2*3} and {2**3} respectively")
print(f"\n 2/3 is {2/3}")
