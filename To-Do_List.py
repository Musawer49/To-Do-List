print("Welcome to To-Do List!")

tasks = []

while True:
    user_input = input("Add a task: ")

    if user_input.lower() == "exit":
        break
    print("Task added successfully!")

    task = {
        "task": user_input,
        "status": False
    }

    tasks.append(task)

print(tasks)
