from random import randint

print("Hello! Let's play in my favorit game!\nI thought of a number from 1 to 50, you have six attempts to guess it.\nGood luck! ")
a = randint(1, 50)
#AttributeError: 'builtin_function_or_method' object has no attribute 'randint'

for x in range(1, 8):
    number = int(input("Try to guess the number: "))
    if number == a:
        print("Well done! Right!")
        break
    elif x == 7:
        print("Game over! Goodbye!")
    else:
        print("You are wrong.Try again!")
    x += 1