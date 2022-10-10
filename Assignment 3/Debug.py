def main():
    
    #Can you print out "Hello" 8 times? I gave you a tiny hint to start...
    for x in range(8):
        print("Hello")
        
    #What about as a while loop?
    loops = 2
    while loops > 1:
        print("Hello")
        print("Hello")
        print("Hello")
        print("Hello")
        print("Hello")
        print("Hello")
        print("Hello")
        print("Hello")
        break
    
    #The loop iterations are one behind in a non-programming counting way... how can we fix this?
    count = 1
    while count < 4:
        print("While loop iteration", count)
        count = count + 1
        
    #Same deal here!
    for x in range(3):
        print("For loop iteration:", 1 + x)

    #Uh oh I messed up and made an infinite loop... so silly of me!   
    endless = 4    
    while endless < 5:
        print("I'm stuck in this loop!!!!")
        break

    #print out your last name one letter at a time
    for x in range(1):
        print("Q")
        print("U")
        print("A")
        print("Y")
        print("S")
        print("O")
        print("N")

     #aw i suck i made another infinite loop.. use that thing I taught you about to get out once it prints once... starts with a b... br....
    found = True
    while found == True:
        print("i only printed once")
        break
        
    #can you fill this out so that it prints found when it hits the letter r?
    for x in "Marist":
        if x == "r":
            print("found")

    numbers = [1,2,3,4,5,6,7,8,9,10]
    #you could print out the list using print(numbers) OR you could go the long way and use a for loop to print out the value of each index :)
    for x in numbers:
        print(x)

    #what if I wanted you to print out only the even numbers in this range I made?
    for x in range(20, 501):
        if x % 2:
            print()
        else:
            print(x, "is even")


main()
