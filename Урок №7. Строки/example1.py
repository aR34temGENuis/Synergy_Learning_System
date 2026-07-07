slovo = input('Введите слово: ')
palindrom = slovo[::-1]
if slovo == palindrom:
    print('yes')
else:
    print('no')        