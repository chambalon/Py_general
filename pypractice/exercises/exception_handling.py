a=int(input("a= "))
b=int(input("b= "))

try:
    print(a/b)
#except Exception as e:
except ZeroDivisionError as e:            # be specific about the type of error

    print("Error:",e)
    print("b cannot be zero, enter a number next time")

print("bye")
