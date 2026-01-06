# import py_module  #requires: py_module.print_me()
# from py_package import py_module
# from py_package.py_module import print_me()

from py_module import print_me

def fn():
    print("test me")

print('hello ')


if __name__ == '__main__': #if executed this file
    fn()