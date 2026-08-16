print("Welcome to To-Do List!")

tasks = []

while True:
    user_input = input("Add a task: ")

    if user_input.lower() == "exit":
        break

    task = {
        "task": user_input,
        "completed": False
    }

    tasks.append(task)

print(tasks)
