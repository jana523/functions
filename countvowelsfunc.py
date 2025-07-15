def count_vowels(x):
    vowels = "aieouAIEOU"
    c = 0
    for i in x:
        if i in vowels:
            c += 1
    return c
x = input ("enter a string: ")
print(count_vowels(x))