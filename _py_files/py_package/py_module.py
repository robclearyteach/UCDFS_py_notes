print("inside: py_package.py_module: name is:", __name__)
def print_me():
    print('me: from py_package.py_module.py')

def print_you():
    print('you: from py_package.py_module.py')

if __name__ == '__main__': #if executed this file
    print_me()
    print_you()
    