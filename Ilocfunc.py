def mylen(x):
    for i in range(len(x)):
        if x[i]=='i':
            print(i)

x = input('enter value: ')
mylen(x)