#Дано два числа. Вывести yes, если они отличаются на 100, иначе вывести No.
a = int(input("Please state the first number:\n"))
b = int(input("Please state the second number:\n"))

if ((a - b) >= 100) or ((b - a) >=100):
    print("Yes")
else:
    print("No") 
