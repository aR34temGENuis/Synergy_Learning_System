a, b = map(int, input('Введите первое и второе число через пробел: ').split())
if b <= a:
    while b < a:
        b = int(input('Второе число должно быть больше первого: '))
        for i in range(a, b + 1):
            if i % 2 == 0:
                print(i, end=" ")
else:
    for i in range(a, b + 1):
        if i % 2 == 0:
            print(i, end=" ")
          
