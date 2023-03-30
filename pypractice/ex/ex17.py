# try and except error/ exception handling

try:
    a=4/0
except Exception as e:
    print(e)
finally:
    print("final")          # here you add the final action you want the script to perform