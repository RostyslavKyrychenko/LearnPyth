#Пользователь вводит номер месяца, вывести название месяца.
import sys
months = "JanFebMarAprMayJunJulAugSepOctNovDec"
months_list = [months[i*3:(i+1)*3] for i in range(12)]
n = int(input("Enter a month number\n"))

if n > 12:
  sys.exit("Incorrect month number")
if n < 1:
  sys.exit("Incorrect month number")
if n >= 1:
  print(months_list[n-1])