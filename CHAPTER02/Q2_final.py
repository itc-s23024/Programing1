import random


def check_initial(name):
    target_initial = name[0].upper()

    while True:
        random_char = chr(random.randint(65, 90))

        print(random_char)

        if random_char == target_initial:
            break


name = input("名前の頭文字を入力してください: ")
check_initial(name)
