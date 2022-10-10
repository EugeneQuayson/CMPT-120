def main():
  
  #set this to any double
  doubleValue = 6.6
  
  #set this to any int
  intValue = 6
  
  #print out addition, subtraction, multiplication, and division of these two values

  multiplication = doubleValue * intValue
  print(multiplication)
  division = doubleValue / intValue
  print(division)
  addition = doubleValue + intValue
  print(addition)
  subtraction = doubleValue - intValue
  print(subtraction)

  #populate this list
  myFriends = ["Dylan", "Daniel", "Saba", "Anthony"]
  
  #print out your friends at index 2 and index 3
  print(myFriends[2], myFriends[3])
  
  
  #populate this list with five numbers
  fiveNumbers = [1, 3, 5, 7, 9, 11]
  
  #do each of the four equations with different numbers each time.

  multiplication2 = fiveNumbers[1] * fiveNumbers[2]
  division2 = fiveNumbers[3] / fiveNumbers[4]
  addition2 = fiveNumbers[5] + fiveNumbers[0]
  subtraction2 = fiveNumbers[0] - fiveNumbers[1]

  print(multiplication2)
  print(division2)
  print(addition2)
  print(subtraction2)

  #now replace two of the numbers in the list with a different number (using name of list[x] = ?, not rewriting the fiveNumber list)

  fiveNumbers[0] = 2
  fiveNumbers[1] = 4

  #print out the list

  print(fiveNumbers)
  
main()  
