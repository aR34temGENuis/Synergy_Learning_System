first = set(map(int, input(f'Введите количетсво числе не более 100000 для первого множества: ').split()))
second = set(map(int, input(f'Введите количетсво числе не более 100000 для второго множества: ').split()))
result = first & second
print(len(result))