n = int(input('Введите количество чисел для ввода: '))
tmp = []
for i in range(n):
    num = int(input(f'Введите число {i + 1}: '))
    tmp.append(num)
print(*reversed(tmp))