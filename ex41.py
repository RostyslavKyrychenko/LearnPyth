#Дано число. Если оно более 100 или менее -100, то занулить, иначе увеличить его на 1.
a = int(input("State the number\n"))

if a > 100 or a < -100:
    a = 0
else:
    a = a + 1
print(a)