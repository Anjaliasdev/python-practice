a = int(input("Enter first number : "))
b = int(input("Enter second number : "))
c = input("Enter operatioin : ")
        
if (c=="+"):
        print("Result", a+b)
elif(c =="-"):
    print("Result", a-b)
elif(c=="*"):
    print("Result", a*b)
elif(c=="/"):
    print("Result", a/b)
else:
    print("Invalid operation")
