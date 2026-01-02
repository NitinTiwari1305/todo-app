from functions import *
while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()


    if user_action.startswith("add"):
        todo = user_action[4:]

        todos = get_todos("todos.txt")

        todos.append(todo +"\n")

        write_todos(todos)

    elif user_action.startswith("show"):

        todos = get_todos("todos.txt")

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}-{item}"
            print(row)

    elif user_action.startswith("edit"):
        try:

            number = int(user_action[5:])
            number = number - 1

            todos = get_todos("todos.txt")

            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + "\n"

            write_todos(todos)

        except ValueError:
            print("Invalid input")
            continue

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])

            todos = get_todos("todos.txt")
            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            write_todos(todos)

            message = f"Todo {todo_to_remove} has been completed successfully and removed from the list."
            print(message)

        except IndexError:
            print("There are no items with that  number.")
            continue

    elif user_action.startswith("exit"):
        break
    else:
        print("Invalid input")

print("bye")