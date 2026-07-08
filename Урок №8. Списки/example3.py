lodka = int(input('Введите максимальный вес, который может выдержать лoдка: '))
while lodka >= 10000000:
        print('Максимальный вес не может быть больше 10000000')
        lodka = int(input('Введите максимальный вес, который может выдержать лodка: '))
rybak = int(input('Введите количество рыбаков: '))
while rybak > 100:
    print('Количество рыбаков не может быть больше 100')
    rybak = int(input('Введите количество рыбаков: '))
weight = []
for i in range(rybak):
    w = int(input(f'Введите вес рыбака {i + 1}: '))
    while w > lodka:
        print(f'Вес рыбака не может быть больше {lodka} кг самой лодки')
        w = int(input(f'Введите вес рыбака {i + 1}: '))
    weight.append(w)
weight.sort()

left = 0
right = rybak - 1
boats = 0
while left <= right:
    if weight[left] + weight[right] <= lodka:
        left += 1
        right -= 1
    else:
        right -= 1    
    boats += 1
print(f'Минимальное количество лодок, которое потребуется: {boats}')    

