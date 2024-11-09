##Suppose number of misprints are counted in 9 pages from the beginning of the first edition of the book of 1000 pages and are recorded as follows
## 2,2,1,0,1,4,2,5,0
## Store the observation in a list x
##
##1.
x=[2,2,1,0,1,4,2,5,0]
print(x)

##2.
## Verify the length of the list

print(len(x))

##3.
## 1 more page was scutinized and observed as the number of misprints as 3.
## Add the observation at end of the list x

x.append(3)

##4.
## Later it was found that a page was not checked, obs of which turned up as 2.
## Insert this value at the 2nd pos of the list.

x.insert(1,2)

##5.
##Remove the first page without error from the list

x.remove(0)

##6.
## Remove the third element from the list

x.pop(2)

##7.
##Find the first page with maximum error
print(x)
print(f"the page number {x.index(max(x))+1} has maximmum error")

##8.
## Find the number of pages with number of misprints 1

print(f"{x.count(1)} pages have 1 misprint")

##9.
## Sort the list
x.sort()
print(f"the sorted list is {x}")
##10.
##Reverse the list
x.reverse()
print(f"the revrse of the list is {x}")
## 11.
## find the unique values from the list (here we want values wiyhout repeatations)

print(set(x))

## 12.
## Print the second elemrnt of x
print(x[1])

##.1.
y=list(range(5,16))
print(y)
## 2.
y.reverse()
print(y)
## 3.
z=list(range(5,23,3))
print(z)
## 4.
c=[2,3,4]
print(c*4)
## 5.
z=c*2
z.sort()
print(z)
## 6.
x=list()
for i in range(2,5):
    for j in range(i,6):
        x.append(i)
print(x)
print(set(x))

##7.
##Find the arithmetic mean of th first three natural number
n=3
print(int((n+1)/2))

##MATRICES

A=[[0,-1,5],
   [2,4,-6],
   [1,1,5]]

B=[[5,3,0],
   [1,2,-4],
   [-2,-4,8]]

##1.
## Display the (2,3)th element of matrix A
print(A[1][2])

## 2.
## Make a matix C by deleting the third row  from matrix B
c=B[0:2]
print(c)

## 3.
## Extract the third row from matrix A
print(A[2])
