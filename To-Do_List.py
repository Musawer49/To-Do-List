print("Welcome to To-Do List!")

tasks = []
while True:
    print("""
    1. Add task
    2. View tasks
    3. Complete task
    4. Delete task
    5. Exit
    """)
    try:
        choice = int(input("Choose an option: "))
    except ValueError:
        print("Please enter a number")
        continue
    if choice == 1:
        task = input("Add a task: ")
        tasks.append({
            "task" : task,
            "status" : "pending"
        })
        print("Task added successfully!")
    elif choice == 2:
        for number, task in enumerate(tasks, start=1):
            print(number, ".", task["task"], "-", task["status"])
    elif choice == 3:
        try:
            ask_num = int(input("Which task number you want to complete: "))
        except ValueError:
            print("Please enter a number")
            continue
        tasks[ask_num - 1]["status"] = "completed"
        print("Task marked as completed.")
    elif choice == 4:
        ask_num = int(input("Which task number do you want to delete: "))
        del tasks[ask_num - 1]
        print("Task deleted successfully")
    elif choice == 5:
        print("Good Bye!")
        break
    else:
        print("Invalid numer. Please enter a valid number.")