from random import randint


def gen_number():
    random_number = randint(1, 101)
    return random_number


def intro():
    print("Welcome, guess the number between 1-100 that the Computer is 'thinking' of!")


def ask_number(question, random_number, count=0):
    response = None
    while response != random_number:
        try:
            response = int(input(question))
            count += 1
            if response > random_number:
                print("Lower... ")
            elif response < random_number:
                print("Higher... ")
            else:
                congrat_winner(response, random_number, count)
        except ValueError:
                print("Invalid value. Enter a number between 1-100 ")
    return response, count


def human_guess():
    print("Ok Human! Let's begin... ")
    random_number = gen_number()
    guess = ask_number("Guess the number: ", random_number)


def congrat_winner(correct, random_number, count):
    if correct == random_number:
        print("WELL DONE! The answer was indeed,", str(correct) + "!")
        print("Number of trials:", count)


if __name__ == '__main__':
    while True:
        intro()
        human_guess()
        ask = input('Would you like to play again? (y/n)')
        if ask == 'y':
            continue
        else:
            break
