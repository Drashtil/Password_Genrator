data =[]
try:
    with open("data.text","r") as f:
        for line in f:
            data.append(line.strip())
except:
    pass
def save_data():
    with open("data.text","w") as f:
        for pwd in data:
            f.write(pwd + "\n")
def add_pwd():
    url = input("Enter url: ")
    pin = input("Enter password: ")
    pwd = url + ":" + pin
    data.append(pwd)
    save_data()
def view_pwd():
    for d in data:
        print(d)
def search_pwd():
    search1 = input("Enter url: ")
    for d in data:
        if search1 in d:
            print(d)
        else:
            break


while True:
    print("1.add passwords")
    print("2.view passwords")
    print("3.seach passwords")
    print("4.exit")

    choice = int(input("Enter your choice: "))
    if(choice==1):
        add_pwd()
    elif(choice==2):
        view_pwd()
    elif(choice==3):
        search_pwd()
    elif(choice==4):
        break
    else:
        print("invaild choice")