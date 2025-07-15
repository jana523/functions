def mylist(x):
    list=[]
    for i in range(1,x+1):
        temp=[]
        for j in range(1,i+1) :
            temp.append(i*j)
        list.append(temp)
    print(list)
x = int(input("enter a number : "))
mylist(x)