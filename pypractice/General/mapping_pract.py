import csv
import pprint

csvfile=input("Filename: ")
file=csv.DictReader(open(csvfile))

mylist=[]

for lines in file:
    mylist.append(lines)

#print(mylist)

pp=pprint.PrettyPrinter(indent=2,width=30)
pp.pprint(mylist)