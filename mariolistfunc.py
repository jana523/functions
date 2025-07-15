def list(x):
    list = ([" "," "," "," "," "])
    for i in list:
        list.append("*")
        list.pop(0)
        print(list)
x = int(input("enter x: "))
list(x)