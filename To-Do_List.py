print("Welcome to To-Do List!")

tasks = [
    {"task": "Practice Python", "status": "pending"},
    {"task": "Reading Book", "status": "pending"}
]
while True:
    print("""
    1. Add task
    2. View tasks
    3. Complete task
    4. Delete task
    5. Exit
    """)
    choice = int(input("Choose an option: "))
    if choice == 1:
        task = input("Add a task: ")
        print("Task added successfully!")
        tasks.append(task)
    elif choice == 2:
        for number, task in enumerate(tasks, start=1):
            print(number, ".", task["task"], "-", task["status"])
    elif choice == 3:
        ask_num = int(input("Which task number you want to complete: "))
        if ask_num == 1:
            tasks[0]["status1"] = "completed"
    elif choice == 4:
        ask_num = int(input("Which task number do you want to delete: "))
        if ask_num == 1:
            del tasks[0]
    elif choice == 5:
        print("Good Bye!")
        break
    else:
        print("Invalid numer. Please enter a valid number.")