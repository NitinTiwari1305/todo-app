FILEPATH = "todos.txt"

def get_todos(filepath=FILEPATH):
    """ Reads the text file and returns
    a list of todos """
    with open(filepath, 'r') as file:
        todos_local = file.readlines()
    return todos_local

def write_todos(todos_arg, filepath=FILEPATH):
    """writes todos into a text file"""
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)

if __name__ == "__main__":
    print(get_todos())