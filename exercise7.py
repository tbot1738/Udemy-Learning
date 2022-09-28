from random import randint
# generate a number 1~10

# input from user?
# check that input is a number 1~10


def game_guess(guess, answer):
    if 0 < guess < 11:
        if guess == answer:
            print('you are a genius!')
            return True
    else:
        print('hey bozo, I said 1~10')


if __name__ == "__main__":
    answer = randint(1, 10)
    while True:
        try:
            guess = int(input('guess a number 1~10:  '))
            if game_guess(guess, answer):
                break
        except ValueError:
            print('please enter a number')
            continue
