x = int(input('Минимальная сумма инвестиции = '))
a = int(input('У Майкла денег = '))
b = int(input('У Ивана денег = '))

if a < 0 or b < 0 or x < 0:
    print('Деньги не могут быть в отрицательном значении')
elif a >= x and b >= x:
    print(2)
elif a >= x and b < x:
    print("Mike")
elif a < x and b >= x:
    print("Ivan")
elif a + b >= x:
    print(1)
else:
    print(0)                    