#Q1. Write a progam to create a dictionary of hindi words with values as their english translation. Provide user with an option to look it up.

words= {
    "hindi": "english",
    "billi" : "cat",
    "yrr" : "bro",
    "nhi" : "no"
    }
word= input("enter the hindi word")
print (words[word])

#Q2. Write a program to input 8 number from the user and display all the unique numbers(once).

s= set()
n = input("Enter the number : ")
s.add(int(n))
n = input("Enter the number : ")
s.add(int(n))
n = input("Enter the number : ")
s.add(int(n))
n = input("Enter the number : ")
s.add(int(n))
n = input("Enter the number : ")
s.add(int(n))
n = input("Enter the number : ")
s.add(int(n))
n = input("Enter the number : ")
s.add(int(n))
n = input("Enter the number : ")
s.add(int(n))
print(s)

#Q3. create a empty dictionary. Allow 4 friends to enter their favorite language as value and use key as their name. Assume that the names are unique.

d = {}
name = input ("Enter friends name : ")
lang = input ("Enter lang name : ")
d.update({name : lang})

name = input ("Enter friends name : ")
lang = input ("Enter lang name : ")
d.update({name : lang})

name = input ("Enter friends name : ")
lang = input ("Enter lang name : ")
d.update({name : lang})

name = input ("Enter friends name : ")
lang = input ("Enter lang name : ")
d.update({name : lang})

print(d)
