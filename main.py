print("Calculator:")
print("Available options:\n")
print("1.Addition\n2.Subtraction\n3.Multiplication\n4.Division")
while True:
    c=int(input("Enter your option:"))
    if((c==1) or( c==2) or (c==3) or (c==4)):
        a=float(input("Enter a number:"))
        b=float(input("Enter another  number:"))
        if(c==1):
            print(f"Addition of {a} and {b} is {a+b}")
        elif(c==2):
            print(f"Subtraction of {a} and {b} is {a-b}")
        elif(c==3):
            print(f"Multiplication of {a} and {b} is {a*b}")
        elif(c==4):
            if(b==0):
                print("Undefined")
            else:
                print(f"Division of {a} and {b} is {a/b}")
    ch=input("Do you want to give inputs again(Yes/No):")
    if ch.lower!='yes':
            break
    else:
        print("Invalid input")
        