print(f"Welcome to TO-DO List")

tasks = []

def initializelist():
    global tasks
    

# Main Menu Function
def display_menu():
    print("\nTo Do List Application\n")
    print("\n1. Add Task\n")
    print("\n2. View All Tasks\n")
    print("\n3. Remove Task\n")
    print("\n4. Exit\n")

# Add Task Function
def add_task():
    task = input("\nWhat is the task you would like to add?\n ")
    tasks.append(task)
    print("\nTask {task} has been added successfully!\n")

# View All Tasks Function
def view_tasks():
    print("\nAll Tasks\n")
    if tasks:  
        for task in tasks:
            print(task)
    else:  
        print("\nNo tasks to display\n")

# Remove Task Function

def remove_task():
    task_to_remove = input("\nEnter the task you would like to remove:\n ")
    if task_to_remove in tasks:
        tasks.remove(task_to_remove)
        print(f"\nTask {task_to_remove} has been removed successfully!\n")
    else:
        print(f"\nTask {task_to_remove} is not in the list\n")


#Start programn - main function
def main():
    while True:
        display_menu()
        choice = input("\nPlease select an option:\n ")
        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            remove_task()
        elif choice == "4":
            print("\nThank you for using the To-Do List Application\n")
            break
        else:
            print("\nInvalid option. Please try again.\n")

main()

