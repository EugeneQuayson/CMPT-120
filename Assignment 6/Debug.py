class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Employee:
    def __init__(self, name, idNumber, department):
        self.name = name
        self.idNumber = idNumber
        self.department = department


class Cake:
    def __init__(self, cake_flavor, cake_frosting):
        self.cake_flavor = cake_flavor
        self.cake_frosting = cake_frosting
    # can you fill out the rest of this for me? im dumb
    # the cake needs to have the cake flavor and cake frosting stored


class Cat:
    def __init__(self, name, age, fur_length):
        self.name = name
        self.age = age
        self.fur_length = fur_length

    def breedGuess(self):
        if self.fur_length == "long":
            return ("Domestic Longhair")
        else:
            return ("Domestic Shorthair")


class Car:
    def __init__(self, model, year, color):
        self.model = model
        self.year = year
        self.color = color

    def fast_car(self):
        if self.color == "red":
            return ("Fast car")
        else:
            return ("Not fast car")

    # create your own function! what do you want it to do?


def main():
    # fill this one out with a dog's name and age.. can be your dog, friend's dog, etc
    dog1 = Dog("George", 4)
    print(dog1.name, dog1.age)

    # and what about a new employee
    employee1 = Employee("Connor", 20134535, "Comp Sci")
    # how would we print out each of the variables from newEmployee?
    print(employee1.name, employee1.department, employee1.idNumber)

    # now create and print out a cake you make
    cake1 = Cake("Chocolate", "Strawberry")
    print(cake1.cake_flavor, cake1.cake_frosting)

    # and now create another cake and print it out
    cake2 = Cake("Eggplant", "Blue Cheese")
    print(cake2.cake_frosting, cake2.cake_flavor)

    # create a cat!
    cat1 = Cat("Gingie", 3, "long")
    # create another cat!
    cat2 = Cat("Venessa", 2, "short")
    # What would we put here to print out the result of breedGuess for cat1?
    print(cat1.breedGuess())

    # create a car!
    car1 = Car("Toyota", 1999, "red")
    # Now print out the function you made for car :)
    print(car1.fast_car())


main()
