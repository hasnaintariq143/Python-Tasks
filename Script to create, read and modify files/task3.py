file=open('hello.txt','w')

file.write("hello this is Xflow")

file.close()

file=open('hello.txt','r')

content=file.read()

file.close()

print(content)