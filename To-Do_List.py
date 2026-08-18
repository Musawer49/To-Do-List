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
    user_input = int(input("Choose an option: "))
    if user_input == 1:
        task = input("Add a task")
    elif user_input == 2:
        print(tasks)
    task ={
        "task" : user_input,
        "status" : "pending",
        }
    tasks.append(task)
for number, task in enumerate(tasks, start=1):
    print(number,".", task["task"], "-" , task["status"])
