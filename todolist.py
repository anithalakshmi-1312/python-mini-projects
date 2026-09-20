tasks = []

def show_tasks():
    if not tasks:
        print("No tasks yet!")
    else:
        for i,task in enumerate(tasks,1):
            #i=number starting from 1, task=the actual item
            print(f"{i}. {task}")

while True:
    print("\n1. Add Task")
    print("2. Show Tasks")
    print("3. Remove Task")
    print("4. Exit")

    choice= input("Choose an option: ")

    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)
        #Adds the new task to the end of the list
        print("Task added!")
    elif choice == "2":
        show_tasks()
    elif choice == "3":
        show_tasks()
        number=int(input("Task number to remove: "))
        tasks.pop(number-1)
        #Remove the task at the specified index
        print("Task removed!")

    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice!")