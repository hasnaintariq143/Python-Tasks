dictionary = {'hello': 'hii','bye':'Get Out','XFLOW':'Love'}

word=input("Enter a word: ")
if word in dictionary:
    print("The meaning is: {}".format(dictionary[word]))
else:
    print("No such word in the Dictionary.")