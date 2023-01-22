FILEPATH = 'todo.txt'
def get_todo(filepath = FILEPATH):
    """Read a text file and return alist of
    to-do items
    """
    with open(filepath,'r') as file:
        todos_local = file.readlines()
    return todos_local

def write_todo(todos_arg, filepath = FILEPATH):
    """write todo item list to file"""
    with open(filepath,'w') as file:
        file.writelines(todos_arg)

if __name__ == '__main__':
    print("Hello")
    print(get_todo())