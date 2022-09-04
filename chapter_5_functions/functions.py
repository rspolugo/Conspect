import random


def main(MIN: int, MAX: int):
    again = "да"

    while again == "да":
        print("бросем кубики\nзначение граней")
        print(random.randint(MIN, MAX))
        print(random.randint(MIN, MAX))
        again = input("бросить еще раз?: да/нет ")


main(1, 6)
