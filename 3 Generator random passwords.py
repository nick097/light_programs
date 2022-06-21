import random

chars = "qwertyuiop[]asdfghjkl;'zxcvbnm,./QWERTYUIOP[]ASDFGHJKL;ZXCVBNM,.1234567890!@#$%^&*()_+-=<>?:{}"

quantityPasswords = int(input("Введите необходимое колличество паролей"))
length = int(input("Ввeдите длинну паролей"))

for x in range(quantityPasswords):
    password = ""

    for i in range(length):
        password += random.choice(chars)

    print(password)

    file = open("password.txt", "a")
    file.write('\n' + password)
    file.close()



