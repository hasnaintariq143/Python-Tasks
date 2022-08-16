filename=input("Enter name of the File: ")
file=open('file.txt','r')

content=file.read()

#print(content)

string=input("Enter a string: ")

if string in content:
    print("String found")
else:
    print("String not found")