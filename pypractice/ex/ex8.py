# print only the objects in a list

a=[1,2,3,4,5,6]

# method 1
for item in a:
    print(item, end=" ")

print("\n---------------------------------------")

# method 2
for item in a:
    print(item)

print("\n---------------------------------------")

# method 3
i=0                 #index
while i < len(a) :
    print(a[i])
    i+=1