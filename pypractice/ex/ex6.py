# convert kg to Lbs and vice versa
w=int(input("enter your weight: "))
unit=input("kg or Lbs? press k or l : ").lower()

if unit=="k" :
    new=w/.45
    print(" your weight is converted to Lbs: ", str(new))
elif unit=="l":
    new=w*.45
    print("your weight is converted to kg: " + str(new))

