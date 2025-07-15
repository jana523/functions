def my_list():
    l = []
    for i in range(5):
        x=int(input("enter value : "))
        l.append(x)
        ascending_order = sorted(l)
        descending_order = sorted(l, reverse=True)
    print(l)
    print(ascending_order)
    print(descending_order)
my_list()
