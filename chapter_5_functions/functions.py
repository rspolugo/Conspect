import random
MIN = 1
MAX = 6
def main():
    again = 'да'
    while again == 'да':
        print('бросем кубики')
        print('значение граней')
        print(random.randint(MIN, MAX))
        print(random.randint(MIN, MAX))
        again = input('бросить еще раз?: да/нет ')

main()
