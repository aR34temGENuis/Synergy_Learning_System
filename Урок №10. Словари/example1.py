pets = {}

pet_name = input("Введите кличку питомца: ")
pet_type = input("Введите вид питомца: ")
pet_age = int(input("Введите возраст питомца: "))
owner_name = input("Введите имя владельца: ")

pets[pet_name] = {
    "Вид питомца": pet_type,
    "Возраст питомца": pet_age,
    "Имя владельца": owner_name
}

age = pets[pet_name]["Возраст питомца"]

if age % 100 in [11, 12, 13, 14]:
    age_word = "лет"
elif age % 10 == 1:
    age_word = "год"
elif age % 10 in [2, 3, 4]:
    age_word = "года"
else:
    age_word = "лет"

print(
    f'Это {pets[pet_name]["Вид питомца"]} по кличке "{pet_name}". '
    f'Возраст питомца: {age} {age_word}. '
    f'Имя владельца: {pets[pet_name]["Имя владельца"]}'
)