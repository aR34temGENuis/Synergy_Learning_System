n = int(input('Введите количество чисел: '))

while n < 1 or n > 100000:
    n = int(input('Число должно быть в диапазоне от 1 до 100000. Введите количество чисел: '))

numbers = list(map(int, input('Введите числа через пробел: ').split()))

while len(numbers) != n or any(abs(x) > 2000000000 for x in numbers):
    numbers = list(map(int, input('Введите ровно N чисел, каждое по модулю не больше 2000000000: ').split()))

print(len(set(numbers)))