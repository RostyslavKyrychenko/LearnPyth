#Даны два числа. 
#Если первое число больше второго, то вывести yes, иначе поменять значения этих переменных и вывести их на экран.
a = int(input("State the first number\n"))
b = int(input("State the second number\n"))

if a > b:
    print("yes")
else:
    a, b = b, a
    print(a, b)