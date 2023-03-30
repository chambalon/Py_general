abc=("i am learning python")
print(abc.upper())
print(abc.lower())
print(abc.find("i"))    #find the index of first occurence of 'i' in abc
print(abc.find("am"))    #find the index of first occurence of 'i' in abc
print("am" in abc)   #find the index of first occurence of 'i' in abc
print(abc.find("G"))    #return -1 as no 'G" in abc ie case sensitive
print(abc.replace("i am", "neha is"))