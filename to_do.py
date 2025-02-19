print(f"Welcome to TO-DO List")

tasks = []

def initializelist():
    global tasks
    

# Main Menu Function
def display_menu():
    print("To Do List Application")
    print("1. Add Task")
    print("2. View All Tasks")
    print("3. Remove Task")
    print("4. Exit")

# Add Task Function
def add_task():
    task = input("What is the task you would like to add? ")
    tasks.append(task)
    print("Task {task} has been added successfully!")

# View All Tasks Function
def view_tasks():
    print("All Tasks")
    for task in tasks:
        print(task)
    else:
        print("No tasks to display")

# Remove Task Function
def remove_task():
    task_to_remove = input("Enter the task you would like to remove: ")
    if task_to_remove in tasks:
        tasks.remove(task_to_remove)
        print(f"Task {task_to_remove} has been removed successfully!")
    else:
        print(f"Task {task_to_remove} is not in the list")


#Start programn - main function
def main():
    while True:
        display_menu()
        choice = input("Please select an option: ")
        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "":
            remove_task()
        elif choice == "4":
            print("Thank you for using the To-Do List Application")
            break
        else:
            print("Invalid option. Please try again.")

main()

