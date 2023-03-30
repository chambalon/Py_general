# sys.argv is a list in Python that contains all the command-line arguments passed to the script. When a python script is executed with arguments, it is captured by Python and stored in a list called sys.argv.


import sys


print("name of the script is ", sys.argv[0])
print("number of arguments: ", len(sys.argv))
print("argument list is ", str(sys.argv))



