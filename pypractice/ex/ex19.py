# map and filter

# map
list1=[1,45,8,11,39,489,47,5,8,855,77,4,8,7,55,8]

list2=map(lambda i: i+5, list1)

print(list(list2))

print("-----------------------------------------")

# filter

list3=filter(lambda i: i % 2 == 0, list1)

print(list(list3))