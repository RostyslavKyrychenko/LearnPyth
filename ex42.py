#Дано число. 
#Если оно от 2 до 5 включительно, то увеличить его на 10. 
#Если оно от 7 до 40, то уменьшить на 100. 
#Если оно не более 0 или более 3000, то увеличить в 3 раза (то есть умножить на 3). 
#Иначе занулить это число.
a = int(input("State the number\n"))

if a >= 2 and a <= 5:
    a = a + 10
elif a >= 7 and a <= 40:
    a = a -100
elif a <= 0 or a > 3000:
    a = a * 3
else:
    a = 0
print(a)