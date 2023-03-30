# unpack operator

#def func(*args, **kwargs):
    #pass

x=[1,45,700,21]

print(*x)
print("------------------------")

def func2(a,b):
    print(a,b)

pair_list=[(1,2), (5,6)]

for pair in pair_list:
    func2(*pair)

print("------------------------")
def func3(x,y):
    print(x,y)

func3(**{'x':2,'y':9})          # ** for tuple