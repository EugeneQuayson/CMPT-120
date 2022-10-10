def main():
    age = int(input("What is your age? "))
    if age >= 25:
        print("You can buy alcohol, nicotine products, and rent a car")
    elif age < 18:
        print("You can only purchase candy cigarettes and sody pops")
    elif age >= 18 < 21:
        print("You can only buy nicotine products in some states")
    elif age >= 21 < 25:
        print("You can buy alcohol and nicotine products, but cannot rent a car")
    else:
        print("You can buy alcohol")


main()
