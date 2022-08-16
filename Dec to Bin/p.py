import re

print("1) Decimal to Binary\n2) Binary to Decimal")
choice=input("Enter your Choice: ")

if choice=='1':
    number=int(input("Enter a Decimal number: "))
    n=bin(number)
    print(n)

elif choice=='2':
    number=input("Enter a binary number: ")
    number=int(number,2)
    print(number)