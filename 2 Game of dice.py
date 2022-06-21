import random

while 1 == 1:
    print("Игра кости. ИСПЫТАЙ СВОЮ УДАЧУ")

    input("Для начала игры нажмите Enter")

    gamer1 = input("введите Ваше число от 1 до 6 и нажмите Enter ")
    print("Ваше число")
    print(gamer1)

    gamer2 = str(random.randint(1, 6))  # Вызываем из модуля random метод randint(1, 6) - сгенерировать случайное число в диапазоне от 1 до 6
    print("Число противника")
    print(gamer2)

    if gamer1 > gamer2:
        print("Поздравляю Вы выиграли")
    elif gamer1 == gamer2:
        print("Ничья")
    else:
        print("К сожадению вы проиграли")

    igra = input("Сыграть еще раз? Введите - y - если да, введите  - n - если нет")

    if igra == "n":
        print("!!!ДО ВСТРЕЧИ!!")
        break
    elif igra == "y":
        pass


