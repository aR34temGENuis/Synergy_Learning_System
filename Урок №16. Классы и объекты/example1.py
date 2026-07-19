class Kassa:
    def __init__(self, money=0):
        self.money = money

    def top_up(self, x):
        self.money += x

    def count_1000(self):
        return self.money // 1000

    def take_away(self, x):
        if x > self.money:
            raise ValueError("Недостаточно денег в кассе")
        self.money -= x


kassa = Kassa()

while True:
    command = input("Введите команду: top_up, count_1000, take_away или stop: ")

    if command == "top_up":
        x = int(input("Введите сумму пополнения: "))
        kassa.top_up(x)
        print(f"Касса пополнена. Сейчас в кассе: {kassa.money}")

    elif command == "count_1000":
        print(f"Целых тысяч в кассе: {kassa.count_1000()}")

    elif command == "take_away":
        x = int(input("Введите сумму, которую нужно забрать: "))

        if x > kassa.money:
            print("Недостаточно денег в кассе")
        else:
            kassa.take_away(x)
            print(f"Деньги выданы. Сейчас в кассе: {kassa.money}")

    elif command == "stop":
        print("Программа завершена")
        break

    else:
        print("Неизвестная команда")