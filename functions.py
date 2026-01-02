def get_todos(filepath="todos.txt"):
    """ Reads the text file and returns
    a list of todos """
    with open(filepath, 'r') as file:
        todos_local = file.readlines()
    return todos_local

def write_todos(todos_arg, filepath="todos.txt"):
    """writes todos into a text file"""
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)

