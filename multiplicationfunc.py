x = input("enter num")
x =int(x)
def multiplication(x):
    for i in range(1,x+1):
        for j in range(1,i+1):
            print(f"{i}*{j}={i*j}")

multiplication(x)
