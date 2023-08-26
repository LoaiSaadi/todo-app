FILEPATH = 'todos.txt'


def get_todos(file_path=FILEPATH):
    """ Read a text file and return the list of
    to-do items.
    """
    with open(file_path, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, file_path=FILEPATH):
    """ Write the to-do items list in the text file."""
    with open(file_path, 'w') as file:
        file.writelines(todos_arg)


# now, when we do "import functions", these 2 line will NOT be executed:
# because "__name__" here is equals to "__main__",
# if we call it from other module, its value will be "functions"
if __name__ == "__main__":
    print("Hello")
    print(get_todos())