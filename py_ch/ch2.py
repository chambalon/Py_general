#create a list with elements in the range 1 to 25. Find the element 11 and replace it with 'element found' text

mylist=list(range(1,26))
print(mylist)

element=int(input("type the number to be found. \nFind: "))

#method1
'''mylist[(element-1)]="element found"
print(mylist)'''

#method2
'''mylist.insert((mylist.index(element)), "element found")
mylist.remove(element)
print(mylist)'''

#method3
mylist[mylist.index(element)]="element found"
print(mylist)

