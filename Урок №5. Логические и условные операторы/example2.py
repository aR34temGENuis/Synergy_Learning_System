slovo = input('Введите слово из маленьких латинских букв: ')

a, e, i, o, u = slovo.count("a"), slovo.count("e"), slovo.count("i"), slovo.count("o"), slovo.count("u")

glas = a + e + i + o + u
soglas = len(slovo) - glas

print(f'Гласных = {glas}')
print(f'Согласных = {soglas}')

if a > 0:
    print("a =", a)
else:
    print(False)

if e > 0:
    print("e =", e)
else:
    print(False)

if i > 0:
    print("i =", i)
else:
    print(False)

if o > 0:
    print("o =", o)
else:
    print(False)

if u > 0:
    print("u =", u)
else:
    print(False)