while True:
    comand = input("Введите команду(simvol, slova, probel)")
    # Перечень команд:      simvol, slova, probel
    if comand == "simvol":
        user_text = str(input("Введите текст"))
        otvet = len(user_text)    # len - функция пересчтиывает слова разделенные пробелом
        print("Колличество символов в тексте:", otvet)

    elif comand == "slova":
        user_text = str(input("Введите текст")).split(' ')  # split(' ') -делет строку по пробелам(выстаивает в столбик) МИНУС - ЛЮБОЙ СИМВОЛ ОТДЕЛЕННЫЙ ПРОБЕЛОМ СЧИТАЕТСЯ КАК СЛОВО
        otvet = len(user_text)
        print("Колличество слов в тексте:", otvet)

    elif comand == "probel":
        user_text = str(input("Введите текст")).split(' ')
        otvet = len(user_text)
        otvet -= 1
        print("Колличество пробелов в тексте:", otvet)