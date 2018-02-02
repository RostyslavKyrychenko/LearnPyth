#Дано два числа. Вывести наибольшее из них.
a = int(input("State the first number:\n"))
b = int(input("State the second number:\n"))

if a > b:
    print(a)
elif a == b:
    print("the numbers are equal")
elif b > a:
    print(b)
