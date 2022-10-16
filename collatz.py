not1 = True


def collatz(number):
    if number == 1:
        global not1
        not1 = False
        return
    if (number % 2 == 0):
        print(number // 2)
        return collatz(number // 2)
    elif (number % 2 == 1):
        print(3 * number + 1)
        return collatz(3 * number + 1)

while not1:
    try:
        print('Enter a number, please: ')
        collatz(int(input()))
    except ValueError:
        print('', end='\n')
        print('Number must be an integer...')
        print('', end='\n')
