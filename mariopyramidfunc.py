def mario_pyramid(x):
    for i in range(1,x):
        print(' '*(x-i)+"*"*i) 
x = int(input("enter x : "))
mario_pyramid(x)