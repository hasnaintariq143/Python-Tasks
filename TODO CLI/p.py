print("1) Show tasks\n2) Add Task\n3) Delete Task\n4) Exit")

choice=input("Enter your Choice: ")
if choice=='1':
    #
    print("\n")
    file=open('task.txt','r')
    str=file.readlines()
    file.close()
    print(str)

elif choice=='2':
    #
    print("\n")
    task=input("Enter new Task: ")
    file=open('task.txt','a')
    file.write(task)
    file.write('\n')
    file.close()
    print("\nTaskAdded!\n")

elif choice=='3':
    #
    print("\n")
    file=open('task.txt','r')
    string=file.readlines()
    print(string)
    file.close()
    task=input("Enter task which you want to delete: ")
    task=task+"\n"
    string.remove(task)
    file=open('task.txt','w')

    for item in string:
        file.write(item)
    file.close()

    print("\nTask Deleted.\n")

elif choice=='4':
    #
    print("\n")
else:
    print("\nInalid Input!\n")