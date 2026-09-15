#Q1. if else elif ladder
a = int(input("Enter your age : "))

if(a>=18):
    print("you are above the age of consent")
elif(a<0):
     print("you are entering an invalid nagative age")
elif(a==0):
     print("you are entering 0, which is not valid age")

else:
    print("you are the below the age of consent")

print("End of program")

#Q2 Write a program to find the greatest of four numbers entered by the user.

a = int(input("Enter no. 1 : "))
b = int(input("Enter no. 2 : "))
c = int(input("Enter no. 3 : "))
d = int(input("Enter no. 4 : "))

if (a>b and a>c and a>d):
    print("A is greater : ", a)
elif (b>a and b>c and b>d):
    print("B is greater : ", b)
elif (c>a and c>b and c>d):
    print("C is greater : ", c)
else:
    print("D is greater : ", d)

#Q3. Write a program to find out whether a student has passed or failed if it requires a total of 40% and at least 33% in each subject to pass. Assume 3 subject and take marks as an input from the user.

m1= int(input("Enter marks 1 : "))
m2= int(input("Enter marks 2 : "))
m3= int(input("Enter marks 3 : "))

total_percentage= (100*m1+m2+m3)/300
if (total_percentage>=40 and m1>33 and m2>33 and m3>33):
    print("you are passed : ", total_percentage)
else:
    print("you failed, try again next year: ", total_percentage)

#Q4. A spam comment is defined as a text containing following keyword : "make a lot of money","buy now","subscribe this","click this".Write a program to detect these spams

p1 = "Make a lot of money"
p2 = "buy now"
p3 = "Subscribe this"
p4 = "click this"

message = input("Enter your comment : ")
if((p1 in message) or (p2 in message) or (p3 in message) or (p4 in message)):
    print("This comment is a spam")

else:
    print("This comment is not a spam")


#Q5 Write a program to find wheather a given username contains less than 10 character or nor

username = input("Enter username : ")
if (len(username)<10):
    print("your username contain less than 10 character")
else:
    print("your username contain more than or equal to 10 charater")


#Q6. Write a program which finds out whether a given name is present in a list or not.

l = ["Anjali", "Rajeshwari", "Divya", "Mona"]

name = input ("Enter your name : ")

if (name in l):
    print("your name is in the list")
else:
    print("your name is not in the list")


#Q7. Write a program to calculate the grade of a student from his marks.

marks = int(input("Enter marks : "))

if(marks<=100 and marks>=90):
   grade = "Ex"
elif(marks<=90 and marks>=80):
   grade = "A"
elif(marks<=80 and marks>=70):
   grade = "B"
elif(marks<=70 and marks>=60):
   grade = "C"
elif(marks<=60 and marks>=50):
   grade = "D"
elif(marks<50):
   grade = "F"

print("your grade is : ", grade)

#Q8. Write a program to find out whether a given post is talking about "anjali" or not


post = input("Enter the post : ")
if("anjali" in post.lower()):
    print("This post is talking about anjali")
else:
    print("This post is not talking about anjali")





















