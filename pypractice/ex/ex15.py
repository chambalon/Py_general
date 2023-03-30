# args and kwargs /keyword args

def func1(*args, **kwargs):     # when you have a set of elements to pass args and kwargs are used
    print(args, kwargs)
    print(*args)
func1(4,6,9,2,7, a=2, b=8)
