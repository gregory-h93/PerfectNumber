print("Welcome to Perfect Number! I will check any number of your choosing to see if it is a perfect number!")
while True:    #This simulates a Do Loop
    isPerfect = False
    total = 0
    print("Enter in a number: ")
    num = int(input())
    while num < 0:
        print("Invalid input! Number must be greater than or equal to 0. Please enter another number: ")
        num = int(input())
    for i in range(1, num + 1, 1):
        if num % i == 0:
            total = total + i
    total = total - num
    if total == num:
        isPerfect = True
        print("The number entered is a perfect number!")
    else:
        isPerfect = False
        print("The number entered is not a perfect number!")
    print("Would you like to search for another perfect number? (Y/N)")
    again = input()
    while again != "Y" and again != "y" and again != "N" and again != "n":
        print("Please enter in (Y/N). Would you like to run the program again? (Y/N)")
        again = input()
    if not(again == "Y" or again == "y"): break   #Exit loop
print("You have chosen to end the program. Goodbye!")
