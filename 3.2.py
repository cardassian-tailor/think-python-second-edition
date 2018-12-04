'''

A function object is a value you can assign to a variable or pass as an argument. For example, do_twice is a function that takes a function object as an argument and calls it twice:

def do_twice(f):
    f()
    f()

Here’s an example that uses do_twice to call a function named print_spam twice.

def print_spam():
    print('spam')

do_twice(print_spam)


'''


def do_twice(f, ar):
	f(ar)
	f(ar)

def print_twice(p):
	print(p)
	print(p)

def do_four(f, ar):
	do_twice(f, ar)
	do_twice(f, ar)


'''
output


In [13]: %run 3.2 do_twice(print_twice, "bob")

In [14]: do_four(print_twice, 'bob')
bob
bob
bob
bob
bob
bob
bob
bob

In [15]: do_twice(print_twice, 'bob')
bob
bob
bob
bob
'''

