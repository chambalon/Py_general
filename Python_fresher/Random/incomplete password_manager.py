from cryptography.fernet import Fernet

'''def write_key():
    key=Fernet.generate_key()
    with open('file1key.key', 'wb') as key_file:
        key_file.write(key)'''

def load_key():
    with open('file1key.key', 'rb') as file:
        key=file.read()
        return key


key=load_key()
fer=Fernet(key)



def view():
   #f=open('file.txt', 'r')
   # #f.close()

    with open('file.txt', 'r') as f :
        for line in f.readlines() :
            #print(line)
            #print(line.strip())
            data=line.rstrip()
            user, passwd=data.split("|")
            print("user:", user, ", password:", fer.decrypt(passwd.encode()).decode())

def create():
    name =input("enter the account name: ")
    pwd =input("enter the password : ")

    with open('file.txt', 'a') as f:
        f.write(name+ "|"+ fer.encrypt(pwd.encode()).decode()+"\n")


while True:
    mode=input("would you like to view the existing passwords or create new ones? (view/create) or type q to quit : ").lower()

    if mode == "q":
        break

    if mode == "view":
        view()


    elif mode == "create":
        create()

    else:
        print("invalid option")
        continue
