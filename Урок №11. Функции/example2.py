import collections


pets = {
    1: {
        "Мухтар": {
            "Вид питомца": "Собака",
            "Возраст питомца": 9,
            "Имя владельца": "Павел"
        }
    },
    2: {
        "Каа": {
            "Вид питомца": "желторотый питон",
            "Возраст питомца": 19,
            "Имя владельца": "Саша"
        }
    }
}


def get_pet(ID):
    return pets[ID] if ID in pets.keys() else False


def get_suffix(age):
    if age % 100 in [11, 12, 13, 14]:
        return "лет"
    elif age % 10 == 1:
        return "год"
    elif age % 10 in [2, 3, 4]:
        return "года"
    else:
        return "лет"


def pets_list():
    if len(pets) == 0:
        print("База данных пуста")
    else:
        for ID, pet_info in pets.items():
            pet_name = list(pet_info.keys())[0]
            pet_data = pet_info[pet_name]

            age = pet_data["Возраст питомца"]
            suffix = get_suffix(age)

            print(
                f'ID: {ID}. Это {pet_data["Вид питомца"]} по кличке "{pet_name}". '
                f'Возраст питомца: {age} {suffix}. '
                f'Имя владельца: {pet_data["Имя владельца"]}'
            )


def create():
    if len(pets) == 0:
        new_id = 1
    else:
        last = collections.deque(pets, maxlen=1)[0]
        new_id = last + 1

    pet_name = input("Введите кличку питомца: ")
    pet_type = input("Введите вид питомца: ")
    pet_age = int(input("Введите возраст питомца: "))
    owner_name = input("Введите имя владельца: ")

    pets[new_id] = {
        pet_name: {
            "Вид питомца": pet_type,
            "Возраст питомца": pet_age,
            "Имя владельца": owner_name
        }
    }

    print(f"Питомец добавлен. ID новой записи: {new_id}")


def read():
    ID = int(input("Введите ID питомца: "))

    pet = get_pet(ID)

    if pet == False:
        print("Питомец с таким ID не найден")
    else:
        pet_name = list(pet.keys())[0]
        pet_data = pet[pet_name]

        age = pet_data["Возраст питомца"]
        suffix = get_suffix(age)

        print(
            f'Это {pet_data["Вид питомца"]} по кличке "{pet_name}". '
            f'Возраст питомца: {age} {suffix}. '
            f'Имя владельца: {pet_data["Имя владельца"]}'
        )


def update():
    ID = int(input("Введите ID питомца, которого нужно изменить: "))

    pet = get_pet(ID)

    if pet == False:
        print("Питомец с таким ID не найден")
    else:
        pet_name = input("Введите новую кличку питомца: ")
        pet_type = input("Введите новый вид питомца: ")
        pet_age = int(input("Введите новый возраст питомца: "))
        owner_name = input("Введите новое имя владельца: ")

        pets[ID] = {
            pet_name: {
                "Вид питомца": pet_type,
                "Возраст питомца": pet_age,
                "Имя владельца": owner_name
            }
        }

        print("Информация о питомце обновлена")


def delete():
    ID = int(input("Введите ID питомца, которого нужно удалить: "))

    pet = get_pet(ID)

    if pet == False:
        print("Питомец с таким ID не найден")
    else:
        del pets[ID]
        print("Запись удалена")


command = ""

while command != "stop":
    command = input(
        "\nВведите команду create, read, update, delete, list или stop: "
    ).lower()

    if command == "create":
        create()
    elif command == "read":
        read()
    elif command == "update":
        update()
    elif command == "delete":
        delete()
    elif command == "list":
        pets_list()
    elif command == "stop":
        print("Программа завершена")
    else:
        print("Неизвестная команда")