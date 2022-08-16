def add(x,y):
    return x+y

def subtract(x,y):
    return x-y

def multiply(x,y):
    return x*y

def divide(x,y):
    return x/y

x=int(input("Enter First number: "))
op=input("Enter operationi to be performed (+,-,*,/): " )
y=int(input("Enter Second number: "))

if op=="+":
    print("Answer : ",add(x,y))

elif op=="-":
    print("Answer : ",subtract(x,y))

elif op=="*":
    print("Answer : ",multiply(x,y))

elif op=="/":
    print("Answer : ",divide(x,y))

else:
    print("Invalid Operation!")