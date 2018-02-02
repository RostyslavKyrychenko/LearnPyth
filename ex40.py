#Дано число. Если оно от -10 до 10 не включительно, то увеличить его на 5, иначе уменьшить на 10.
a = int(input("State the number\n"))

if a > -10 and a < 10:
    n = a + 5
    print(n)
else:
    f = a - 10
    print(f)
