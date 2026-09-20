a=int(input("A: "))
b=int(input("B: "))
operation=input("Operation (+, -, *, /): ")
if(operation=="+"):
    print(a+b)
elif(operation=="-"):
    print(a-b)
elif(operation=="*"):
    print(a*b)
elif(operation=="/"):
    if(b!=0):
        print(a/b)
    else:
        print("Cannot divide by zero")
else:
    print("Invalid operation")