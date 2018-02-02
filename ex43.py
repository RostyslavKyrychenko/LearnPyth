#Пользователь вводит номер месяца. Вывести название поры года (весна, лето и т.д.)
a = int(input("State the month number\n"))

if 1<= a <=2:
    print("Winter")
elif 3<= a <= 5:
    print("Spring")
elif 6<= a <= 8:
    print("Sumer")
elif 9<= a <= 11:
    print("Autumn")
elif a == 12:
    print("Winter")
else:
    print("Wrong month number")
     