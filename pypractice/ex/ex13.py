# functions

def func1():
    print("hi")

    def func2():
        print("whatsup")
    func2()
func1()
print("-------------------------------")

def func3(a, b) :
    return a*b
print(func3(6,2))     # when the function is called, it will on;y return a*b;   to print it on the screen we pass the function to  print

print("-------------------------------")

def func3(a, b) :
    return a*b, a/b     # return the values in a tuple
print(func3(6,2)) 

print("-------------------------------")
#method 2

def func3(a, b) :
    return a*b, a/b
x,y = func3(6,2)
print(x,y)

