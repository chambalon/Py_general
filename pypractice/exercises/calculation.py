def add(a,b):
    return a+b

def substract(a,b):
    return a-b

def calculate(a,b):
    return a+b, a-b, a*b, a/b, a%b

print(add(2,3))

print(substract(3,2))

i,j,k,l,m=calculate(10,4)
print("a+b= {} a-b= {} a*b= {} a/b= {} a%b= {}".format(i,j,k,l,m))
print("-------------------------------------------------")
print("a+b=",i, "a-b=",j, "a*b=", k, "a/b=",l,"a%b=",m)
