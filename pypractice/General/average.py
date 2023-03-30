# methode 1     -find the average of the user input values
sum=0
average=0
count=0

while True:
    num=input("enter the number(enter 'done' when finished): ")
    if num =="done":
        break
    
    sum+=int(num)
    count+=1

average=sum/count

print("average= ", average)
