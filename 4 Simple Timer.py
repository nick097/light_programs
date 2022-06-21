import time

while True:
    i = 0   # секунды
    ii = 0 # минуты
    iii = 0 # часы

    time_user = int(input("Введите коллиество секунд"))
    comment = str(input("Введите Ваш комментарий"))

    for q in range(time_user):
        time.sleep(1)
        i += 1
        print("Прошло секунд", i)
        if (i % 60) == 0:
            ii += 1
            print("Прошло минут", ii)

        if (i % 3600) == 0:
            iii += 1
            print("Прошло часов", iii)

    print("\nВремя окончено!!!!!!\n")
    print("Ваш комментарий\n\n", comment, "\n")

    rerun = input("Запустить таймер еще раз? Введите - y - если да, введите  - n - если нет\n")

    if rerun == "n":
        print("\n\n\nСПАСИБО ЧТО ВОСПОЛЬЗОВАЛИСЬ НАШИМ СЕРВИСОМ.\n\n\n!!!ДО ВСТРЕЧИ!!!")
        break
    elif rerun == "y":
        pass