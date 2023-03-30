list1=[]     # to store reminder
zeros=[0,0,0,0,0,0,0,0]


num=int(input("enter the number: "))

while num > 0 :
        r=int(num%2)
        list1.append(r)
        num=int(num/2)

#reverse_list=list(reversed(list1))
reverse_list=list1[::-1]


binary=zeros[len(reverse_list):len(zeros)]+reverse_list
print(binary)

