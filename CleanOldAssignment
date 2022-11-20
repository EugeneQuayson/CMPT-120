def main():
    # this loop asks the user their age, checks if the input is a number, makes it an int, then moves on
    while True:
        # if the user does not give a numeric answer the program repeats the question and says "please input a number"
        age = input("What is your age? ")
        if age.isdigit():
            age = int(age)
            break
        else:
            print("please input a number")
    # these statements check what number the input is and gives a certain response depending on what number age is
    if age >= 25:
        print("You can buy alcohol, nicotine products, and rent a car")
    elif age < 18:
        print("You can only purchase candy cigarettes and soda pops")
    elif age >= 18 < 21:
        print("You can only buy nicotine products in some states")
    elif age >= 21 < 25:
        print("You can buy alcohol and nicotine products, but cannot rent a car")
    else:
        print("You can buy alcohol")


main()
