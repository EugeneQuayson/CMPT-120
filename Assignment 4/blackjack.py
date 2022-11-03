import random


def bust():
    numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11)

    val1 = random.choice(numbers)
    val2 = random.choice(numbers)
    val3 = random.choice(numbers)

    total = val1 + val2 + val3

    print("Card One: ", val1)
    print("Card Two: ", val2)
    print("Card Three: ", val3)

    if 11 in {val1, val2, val3}:
        result = total - 10
        if result > 21:
            print("Bust!")
        elif result < 21:
            print(result)
        else:
            print("Blackjack!")
    else:
        if total > 21:
            print("Bust!")
        elif total < 21:
            print(total)
        else:
            print("Blackjack!")


def main():
    while True:
        play = input("Would you like to play a game of Blackjack? (Y or N) ")
        if play == "Y":
            bust()
        else:
            print("Ok, bye!")

    while True:
        cont = input("Would you like to play again? (Y or N) ")

        if cont == "Y":
            bust()
        else:
            print("Ok, bye!")
            break


main()
