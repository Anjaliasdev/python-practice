#Q1 Write a python to display a user entered name followed by good afternoon using input() function
name = input("Enter your name : ")
print(" Good Afternoon ", {name})

#Q2 Write a program to fill in a letter template given below with name and date.
letter = '''
dear <|Name|>,
you are selected !
 <|Date|>
'''
letter = '''
dear <|Name|>,
you are selected !
<|Date|> '''

print(letter.replace ("<|Name|>", "Anjali"). replace("<|Date|>", "13 sepember 2026"))

#Q3 Write a program to detect double space in a string.
name = ("Anjali is a good girl and")
print(name.find(" "))

#Q4. Replace the double space from promlem 3 wth single spaces
name = "Anjali is a good girl and"
print(name.replace(" ", ""))

#Q5. Write the program to format the following letter using escape sequence character.

letter = "Dear anjali, \n\t This is python code.\n Thanks!"
print(letter)
