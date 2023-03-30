# except: block gets excecuted when there is an error occures at try block
# Finally block gets excecuted if we get an error or if dont

a=int(input("a= "))
b=int(input("b= "))



try:
    print("file/resouce open")
    print(a/b)
    c=int(input("c= "))

except ZeroDivisionError as e:
    print("Error:",e)
    print("b cannot be zero, enter a number next time")

except ValueError as e:
    print("Error",e)
    print("invalid input")

except Exception as e:
    print("Error:",e)
    print("something went wrong")

finally:
    print("file/resource closed")
