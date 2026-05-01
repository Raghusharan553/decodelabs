def show_menu():
    print("\n--- TO-DO LIST MENU ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Exit")
def add_task(tasks):
    task_name = input("Enter your task: ")
    task = {
        "id": len(tasks) + 1,
        "task": task_name
    }
    tasks.append(task)
    print("Task added successfully!")
def view_tasks(tasks):
    if not tasks:
        print("No tasks available.")
        return
    print("\nYour Tasks:")
    for task in tasks:
        print(f"{task['id']}. {task['task']}")
def main():
    my_tasks = []
    while True:
        show_menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            add_task(my_tasks)
        elif choice == '2':
            view_tasks(my_tasks)
        elif choice == '3':
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Try again.")
if __name__ == "__main__":
    main()