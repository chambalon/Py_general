import math

'''r=int(input("enter the radius: "))

p=2*math.pi*r
v=(4/3)*math.pi*pow(r,3)

print("perimeter of the circle= ", p)
print("volum of sphere= ",v)'''

print("------------------------------")

def read():
    r=int(input("radius= "))
    return r

def calculate(r):
    p=2*math.pi*r
    v=(4/3)*math.pi*pow(r,3)
    return p,v

def display():
    r=read()
    p,v=calculate(r)
    print("perimeter of the circle= ", p)
    print("volum of sphere= ",v)

display()

