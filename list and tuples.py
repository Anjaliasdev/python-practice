#Q1. Write a program to store seven fruites in a list entered by the user.

fruits = []
f1= input("Enter the name : ")
fruits.append(f1)
f2= input("Enter the name : ")
fruits.append(f2)
f3= input("Enter the name : ")
fruits.append(f3)
f4= input("Enter the name : ")
fruits.append(f4)
f5= input("Enter the name : ")
fruits.append(f5)
f6= input("Enter the name : ")
fruits.append(f6)
f7= input("Enter the name : ")
fruits.append(f7)
print(fruits)
          
#Q2 Write a programtp accept marks of 6 students and display them in a sorted manner

marks = []
m1 = int(input("Enter marks : "))
marks.append(m1)
m2 = int(input("Enter marks : "))
marks.append(m2)
m3 = int(input("Enter marks : "))
marks.append(m3)
m4 = int(input("Enter marks : "))
marks.append(m4)
m5 = int(input("Enter marks : "))
marks.append(m5)
m6 = int(input("Enter marks : "))
marks.append(m6)

marks.sort()
print(marks)


#Q3 Check that a tupal type cannot be changed in python

a = (2, 234, "Anjali")

a[2] = "pooja"

#Q4. Write a program to sum a list with 4 number

l= [34,56,78,23]
print (sum(l))

# so it give an error becouse tuples are immutable

#Q5. Write a program to count the number of zeros in the following tuple:

a= (7,0,5,0,0,3,0)

n= a.count(0)
print(n)

