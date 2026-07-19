# ============================================================
# README / ОПИСАНИЕ ИГРЫ
# ============================================================
#
# Название игры:
#   Пожарный вертолёт
#
# Цель игры:
#   Игрок управляет вертолётом, летает по карте, набирает воду из реки,
#   тушит горящие деревья, получает очки и старается не потерять все жизни.
#
# Что реализовано:
#   1. Игровое поле произвольного размера.
#   2. Генерация деревьев.
#   3. Генерация реки.
#   4. Генерация госпиталя.
#   5. Генерация магазина улучшений.
#   6. Управление вертолётом через клавиши W/A/S/D.
#   7. Набор воды из реки.
#   8. Тушение пожаров.
#   9. Начисление очков за потушенные пожары.
#   10. Потеря очков за сгоревшие деревья.
#   11. Распространение пожаров.
#   12. Погодные условия: sunny, cloudy, storm.
#   13. Жизни вертолёта.
#   14. Госпиталь для восстановления жизней.
#   15. Магазин для увеличения резервуара воды.
#   16. Сохранение игры в файл.
#   17. Загрузка игры из файла.
#
# Обозначения на карте:
#   A  - вертолёт игрока
#   .  - пустая клетка
#   T  - дерево
#   F  - горящее дерево / пожар
#   ~  - река
#   X  - сгоревшее дерево
#   H  - госпиталь
#   $  - магазин улучшений
#
# Управление:
#   W     - вверх
#   S     - вниз
#   A     - влево
#   D     - вправо
#   E     - набрать воду, если вертолёт стоит на реке
#   F     - потушить пожар, если вертолёт стоит на горящей клетке
#   H     - восстановить жизнь в госпитале
#   U     - купить улучшение в магазине
#   SAVE  - сохранить игру
#   LOAD  - загрузить игру
#   Q     - выйти из игры
#
# ============================================================


# Импортируем random для случайной генерации карты, деревьев, пожаров и погоды
import random

# Импортируем json для сохранения и загрузки игры из файла
import json

# Импортируем os, чтобы проверить, существует ли файл сохранения
import os

# Импортируем time, чтобы делать небольшую паузу после каждого хода
import time


# ============================================================
# ГЛОБАЛЬНЫЕ НАСТРОЙКИ И ОБОЗНАЧЕНИЯ
# ============================================================

# Название файла, в который будет сохраняться игра
SAVE_FILE = "save_game.json"

# Символы карты
EMPTY = "."
TREE = "T"
FIRE = "F"
RIVER = "~"
BURNED = "X"
HOSPITAL = "H"
SHOP = "$"
HELICOPTER = "A"


# ============================================================
# ФУНКЦИИ ДЛЯ СОЗДАНИЯ И ПРОВЕРКИ КАРТЫ
# ============================================================

# Функция создаёт матрицу нужного размера.
# rows - количество строк.
# cols - количество столбцов.
# fill - символ, которым заполняется каждая клетка.
def create_matrix(rows, cols, fill=EMPTY):
    matrix = []

    for i in range(rows):
        row = []

        for j in range(cols):
            row.append(fill)

        matrix.append(row)

    return matrix


# Функция проверяет, находится ли клетка внутри границ карты.
# x - номер строки.
# y - номер столбца.
# rows - всего строк.
# cols - всего столбцов.
def is_inside(x, y, rows, cols):
    return 0 <= x < rows and 0 <= y < cols


# Функция возвращает список всех пустых клеток на карте.
# Это нужно, чтобы случайно ставить деревья, госпиталь, магазин и вертолёт.
def get_empty_cells(field):
    empty_cells = []

    for x in range(len(field)):
        for y in range(len(field[0])):
            if field[x][y] == EMPTY:
                empty_cells.append((x, y))

    return empty_cells


# Функция выбирает случайную пустую клетку.
# Если пустых клеток нет, возвращает None.
def get_random_empty_cell(field):
    empty_cells = get_empty_cells(field)

    if len(empty_cells) == 0:
        return None

    return random.choice(empty_cells)


# ============================================================
# ФУНКЦИИ ГЕНЕРАЦИИ ОБЪЕКТОВ НА КАРТЕ
# ============================================================

# Функция создаёт реку.
# Река идёт сверху вниз по случайному столбцу.
# Иногда она немного смещается влево или вправо, чтобы выглядеть естественнее.
def generate_river(field):
    rows = len(field)
    cols = len(field[0])

    river_col = random.randint(0, cols - 1)

    for x in range(rows):
        field[x][river_col] = RIVER

        # Иногда меняем направление реки
        if random.randint(1, 100) <= 35:
            river_col += random.choice([-1, 1])

        # Не даём реке выйти за левую границу
        if river_col < 0:
            river_col = 0

        # Не даём реке выйти за правую границу
        if river_col >= cols:
            river_col = cols - 1


# Функция генерирует деревья.
# count - сколько деревьев нужно создать.
def generate_trees(field, count):
    for i in range(count):
        cell = get_random_empty_cell(field)

        if cell is not None:
            x, y = cell
            field[x][y] = TREE


# Функция размещает госпиталь и магазин улучшений.
# Госпиталь обозначается H.
# Магазин обозначается $.
def place_special_objects(field):
    hospital_cell = get_random_empty_cell(field)

    if hospital_cell is not None:
        hospital_x, hospital_y = hospital_cell
        field[hospital_x][hospital_y] = HOSPITAL

    shop_cell = get_random_empty_cell(field)

    if shop_cell is not None:
        shop_x, shop_y = shop_cell
        field[shop_x][shop_y] = SHOP


# ============================================================
# ФУНКЦИИ ОТРИСОВКИ ИНТЕРФЕЙСА
# ============================================================

# Функция выводит карту в консоль.
# Если координаты клетки совпадают с координатами игрока, выводим вертолёт A.
# Иначе выводим обычное содержимое клетки.
def draw_field(field, player):
    print("\nКарта:")

    for x in range(len(field)):
        for y in range(len(field[0])):
            if player["x"] == x and player["y"] == y:
                print(HELICOPTER, end=" ")
            else:
                print(field[x][y], end=" ")
        print()


# Функция выводит текущее состояние игрока:
# погоду, очки, жизни, количество воды и список команд.
def print_status(player):
    print("\nСтатус:")
    print(f"Погода: {player['weather']}")
    print(f"Очки: {player['score']}")
    print(f"Жизни: {player['lives']}/{player['max_lives']}")
    print(f"Вода: {player['water']}/{player['water_capacity']}")
    print("Команды:")
    print("W/A/S/D - движение")
    print("E - набрать воду")
    print("F - потушить пожар")
    print("H - госпиталь")
    print("U - магазин улучшений")
    print("SAVE - сохранить игру")
    print("LOAD - загрузить игру")
    print("Q - выход")


# ============================================================
# ФУНКЦИИ ПОГОДЫ И СОБЫТИЙ НА КАРТЕ
# ============================================================

# Функция случайно выбирает погоду.
# sunny - солнечно, пожары появляются чаще.
# cloudy - облачно, пожары появляются реже.
# storm - гроза, пожары появляются редко, но вертолёт может получить урон.
def change_weather():
    chance = random.randint(1, 100)

    if chance <= 50:
        return "sunny"
    elif chance <= 80:
        return "cloudy"
    else:
        return "storm"


# Функция иногда выращивает новое дерево на пустой клетке.
def grow_tree(field):
    if random.randint(1, 100) <= 25:
        cell = get_random_empty_cell(field)

        if cell is not None:
            x, y = cell
            field[x][y] = TREE


# Функция иногда создаёт новый пожар.
# Вероятность появления пожара зависит от погоды.
def start_random_fire(field, weather):
    fire_chance = 10

    if weather == "sunny":
        fire_chance = 18
    elif weather == "cloudy":
        fire_chance = 8
    elif weather == "storm":
        fire_chance = 4

    # Если случайное число больше шанса пожара, пожар не появляется
    if random.randint(1, 100) > fire_chance:
        return

    trees = []

    # Собираем все клетки, где есть деревья
    for x in range(len(field)):
        for y in range(len(field[0])):
            if field[x][y] == TREE:
                trees.append((x, y))

    # Если деревья есть, выбираем случайное и поджигаем
    if len(trees) > 0:
        x, y = random.choice(trees)
        field[x][y] = FIRE


# Функция распространяет пожар на соседние деревья.
# Пожар может перейти вверх, вниз, влево или вправо.
def spread_fire(field, weather):
    rows = len(field)
    cols = len(field[0])

    spread_chance = 15

    if weather == "sunny":
        spread_chance = 30
    elif weather == "cloudy":
        spread_chance = 12
    elif weather == "storm":
        spread_chance = 5

    new_fire_cells = []

    for x in range(rows):
        for y in range(cols):
            if field[x][y] == FIRE:
                directions = [
                    (x - 1, y),
                    (x + 1, y),
                    (x, y - 1),
                    (x, y + 1)
                ]

                for nx, ny in directions:
                    if is_inside(nx, ny, rows, cols):
                        if field[nx][ny] == TREE:
                            if random.randint(1, 100) <= spread_chance:
                                new_fire_cells.append((nx, ny))

    # Поджигаем новые клетки после проверки всей карты
    # Это нужно, чтобы пожар не распространялся слишком быстро за один ход
    for x, y in new_fire_cells:
        field[x][y] = FIRE


# Функция отвечает за сгорание деревьев.
# Если пожар горит слишком долго, клетка становится X.
# За сгоревшее дерево игрок теряет очки.
def burn_trees(field, fire_age, player):
    rows = len(field)
    cols = len(field[0])

    for x in range(rows):
        for y in range(cols):
            if field[x][y] == FIRE:
                key = f"{x},{y}"

                if key not in fire_age:
                    fire_age[key] = 1
                else:
                    fire_age[key] += 1

                # Если пожар горит 5 ходов, дерево сгорает
                if fire_age[key] >= 5:
                    field[x][y] = BURNED
                    player["score"] -= 5
                    del fire_age[key]

    # Удаляем из fire_age те пожары, которых уже нет на карте
    keys_to_delete = []

    for key in fire_age:
        x, y = map(int, key.split(","))

        if field[x][y] != FIRE:
            keys_to_delete.append(key)

    for key in keys_to_delete:
        del fire_age[key]


# Функция наносит урон вертолёту во время грозы.
# Во время storm есть небольшой шанс потерять 1 жизнь.
def storm_damage(player):
    if player["weather"] == "storm":
        if random.randint(1, 100) <= 10:
            player["lives"] -= 1
            print("Во время грозы вертолёт получил повреждение! -1 жизнь")


# Функция игрового тика.
# Один тик происходит после каждого действия игрока.
# Здесь обновляется погода, растут деревья, появляются пожары,
# пожар распространяется, деревья сгорают, а гроза может повредить вертолёт.
def game_tick(field, fire_age, player, turn):
    # Каждые 5 ходов меняем погоду
    if turn % 5 == 0:
        player["weather"] = change_weather()

    grow_tree(field)
    start_random_fire(field, player["weather"])
    spread_fire(field, player["weather"])
    burn_trees(field, fire_age, player)
    storm_damage(player)


# ============================================================
# ФУНКЦИИ ДЕЙСТВИЙ ИГРОКА
# ============================================================

# Функция двигает игрока.
# dx - изменение по строкам.
# dy - изменение по столбцам.
def move_player(player, dx, dy, field):
    rows = len(field)
    cols = len(field[0])

    new_x = player["x"] + dx
    new_y = player["y"] + dy

    if is_inside(new_x, new_y, rows, cols):
        player["x"] = new_x
        player["y"] = new_y
    else:
        print("Вертолёт не может вылететь за границу карты")


# Функция позволяет набрать воду.
# Воду можно набрать только тогда, когда вертолёт стоит на реке.
def take_water(player, field):
    x = player["x"]
    y = player["y"]

    if field[x][y] == RIVER:
        player["water"] = player["water_capacity"]
        print("Вода набрана в резервуар")
    else:
        print("Здесь нет реки. Набрать воду нельзя")


# Функция тушит пожар.
# Пожар можно потушить только если вертолёт стоит на клетке F.
# Для тушения нужна хотя бы 1 единица воды.
def extinguish_fire(player, field, fire_age):
    x = player["x"]
    y = player["y"]

    if field[x][y] != FIRE:
        print("На этой клетке нет пожара")
        return

    if player["water"] <= 0:
        print("Нет воды для тушения")
        return

    player["water"] -= 1
    player["score"] += 10
    field[x][y] = EMPTY

    key = f"{x},{y}"

    if key in fire_age:
        del fire_age[key]

    print("Пожар потушен! +10 очков")


# Функция госпиталя.
# Если вертолёт стоит на H, можно восстановить 1 жизнь за очки.
def visit_hospital(player, field):
    x = player["x"]
    y = player["y"]

    if field[x][y] != HOSPITAL:
        print("Вы не в госпитале")
        return

    if player["lives"] >= player["max_lives"]:
        print("Здоровье уже полное")
        return

    price = 10

    if player["score"] < price:
        print(f"Не хватает очков. Лечение стоит {price} очков")
        return

    player["score"] -= price
    player["lives"] += 1

    print("Вертолёт отремонтирован. +1 жизнь")


# Функция магазина.
# Если вертолёт стоит на $, можно увеличить вместимость резервуара воды.
def visit_shop(player, field):
    x = player["x"]
    y = player["y"]

    if field[x][y] != SHOP:
        print("Вы не в магазине улучшений")
        return

    price = player["water_capacity"] * 15

    if player["score"] < price:
        print(f"Не хватает очков. Улучшение стоит {price} очков")
        return

    player["score"] -= price
    player["water_capacity"] += 1
    player["water"] = player["water_capacity"]

    print("Резервуар улучшен!")
    print(f"Новая вместимость воды: {player['water_capacity']}")


# ============================================================
# ФУНКЦИИ СОХРАНЕНИЯ И ЗАГРУЗКИ
# ============================================================

# Функция сохраняет игру в JSON-файл.
# Сохраняется карта, данные игрока, возраст пожаров и номер хода.
def save_game(field, player, fire_age, turn):
    data = {
        "field": field,
        "player": player,
        "fire_age": fire_age,
        "turn": turn
    }

    with open(SAVE_FILE, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

    print("Игра сохранена")


# Функция загружает игру из JSON-файла.
# Если файла нет, возвращает None.
def load_game():
    if not os.path.exists(SAVE_FILE):
        print("Файл сохранения не найден")
        return None

    with open(SAVE_FILE, "r", encoding="utf-8") as file:
        data = json.load(file)

    print("Игра загружена")

    return data["field"], data["player"], data["fire_age"], data["turn"]


# ============================================================
# СОЗДАНИЕ НОВОЙ ИГРЫ
# ============================================================

# Функция создаёт новую игру:
# 1. Спрашивает размер карты.
# 2. Создаёт пустую карту.
# 3. Генерирует реку.
# 4. Генерирует деревья.
# 5. Ставит госпиталь и магазин.
# 6. Ставит вертолёт на случайную пустую клетку.
# 7. Создаёт словарь игрока.
def create_game():
    rows = int(input("Введите количество строк карты: "))
    cols = int(input("Введите количество столбцов карты: "))

    while rows < 5 or cols < 5:
        print("Размер карты должен быть минимум 5x5")
        rows = int(input("Введите количество строк карты: "))
        cols = int(input("Введите количество столбцов карты: "))

    field = create_matrix(rows, cols)

    generate_river(field)

    tree_count = rows * cols // 4
    generate_trees(field, tree_count)

    place_special_objects(field)

    start_cell = get_random_empty_cell(field)

    if start_cell is None:
        start_x = 0
        start_y = 0
    else:
        start_x, start_y = start_cell

    player = {
        "x": start_x,
        "y": start_y,
        "score": 0,
        "lives": 3,
        "max_lives": 3,
        "water": 0,
        "water_capacity": 1,
        "weather": "sunny"
    }

    fire_age = {}
    turn = 1

    return field, player, fire_age, turn


# ============================================================
# ГЛАВНЫЙ ИГРОВОЙ ЦИКЛ
# ============================================================

# Главная функция игры.
# Здесь создаётся игра и запускается цикл.
# Цикл продолжается, пока у игрока есть жизни.
def main():
    print("Игра: пожарный вертолёт")
    print("Цель: тушить пожары, набирать очки и не потерять все жизни")

    field, player, fire_age, turn = create_game()

    while player["lives"] > 0:
        draw_field(field, player)
        print_status(player)

        command = input("\nВведите команду: ").lower()

        if command == "w":
            move_player(player, -1, 0, field)

        elif command == "s":
            move_player(player, 1, 0, field)

        elif command == "a":
            move_player(player, 0, -1, field)

        elif command == "d":
            move_player(player, 0, 1, field)

        elif command == "e":
            take_water(player, field)

        elif command == "f":
            extinguish_fire(player, field, fire_age)

        elif command == "h":
            visit_hospital(player, field)

        elif command == "u":
            visit_shop(player, field)

        elif command == "save":
            save_game(field, player, fire_age, turn)

        elif command == "load":
            loaded_data = load_game()

            if loaded_data is not None:
                field, player, fire_age, turn = loaded_data

        elif command == "q":
            print("Вы вышли из игры")
            break

        else:
            print("Неизвестная команда")

        game_tick(field, fire_age, player, turn)
        turn += 1

        time.sleep(0.3)

    if player["lives"] <= 0:
        print("\nИгра окончена. У вертолёта закончились жизни")
        print(f"Финальный счёт: {player['score']}")


# Эта проверка нужна, чтобы игра запускалась только тогда,
# когда файл открыт напрямую, а не импортирован как модуль.
if __name__ == "__main__":
    main()