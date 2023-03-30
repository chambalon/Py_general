# scope and global

a='sam'

def func(name):
    a=name          # assigned as local

print(a)

func('Ann')
print(a)

print("---------------------------------")

a='sam'

def func(name):
    global a        # a is assigned as global varriable
    a=name

print(a)

func('Ann')
print(a)