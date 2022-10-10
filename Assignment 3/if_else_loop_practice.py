def main():
    numbers = [11, 31, 23, 27, 44, 38, 32, 42]
    for x in numbers:
        if x > 35:
            print(x, "is greater than 35")
        elif 20 < x < 35:
            print(x, "is between 20-35")
        elif 5 < x < 20:
            print(x, "is between 5 and 20")
        else:
            print(x, "is less than 5")


main()
