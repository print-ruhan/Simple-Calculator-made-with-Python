#This is a simple calculator made by Iram Mahmud Ruhan
import time

def second_math(num1):
    #This is the function for using a number from adding, substracting, multiplicating or dividing
    while True:
        print("Your first number is " + str(num1))
        num2 = input("Please enter the 2nd number:") 
        time.sleep(.3)
        if num2.isalpha():
            print("Please enter a number!")
            time.sleep(.3)
        else:
            break
    print("Your first number is", str(num1)," and your second number is", num2)
    time.sleep(.3)
    operate(num1, num2)

    
#--------------------------------------------------------

def addition(num1, num2):
    #This is for addition
    try:
        sum = float(num1) + float(num2)
        print("Your addition should be =", str(sum))
        time.sleep(.1)
        while True:
            choice = input("Do you want to do something with your addition? (y/n):").lower()
            time.sleep(.3)
            if choice == "y":
                second_math(sum)
                break
            else:
                break
        while choice == 'n' or not(choice == 'y'):
            choice2 = input("Do you want to go the main menu? (y/n):").lower()
            time.sleep(.3)
            if choice2 == "y":
                menu()
                break
            elif choice2 == "n":
                print("Goodbye!")
                time.sleep(1)
                break
            else:
                print("Please enter a valid answer")
                time.sleep(.3)
    except ValueError:
        while True:
            choice3 = input(("There's something wrong :(\nWould you like to go to the first menu? (y/n):")).lower()
            time.sleep(.3)
            if choice3 == "y":
                menu()
                break
            elif choice3 == "n":
                print("Goodbye!")
                time.sleep(1)
                break
            else:
                print("Please enter a valid answer!")
                time.sleep(.3)
                            
                       
#--------------------------------------------------------

def substraction(num1, num2):
    #This is for substraction
    try:
        sum = float(num1) - float(num2)
        print("Your substraction should be =", str(sum))
        time.sleep(.1)
        while True:
            choice = input("Do you want to do something with your substracted number? (y/n):").lower()
            time.sleep(.3)
            if choice == "y":
                second_math(sum)
                break
            else:
                break
        while choice == 'n' or not(choice == 'y'):
            choice2 = input("Do you want to go the main menu? (y/n):").lower()
            time.sleep(.3)
            if choice2 == "y":
                menu()
                break
            elif choice2 == "n":
                print("Goodbye!")
                time.sleep(1)
                break
            else:
                print("Please enter a valid answer")
                time.sleep(.3)
    except ValueError:
        while True:
            choice3 = input(("There's something wrong :(\nWould you like to go to the first menu? (y/n):")).lower()
            time.sleep(.3)
            if choice3 == "y":
                menu()
                break
            elif choice3 == "n":
                print("Goodbye!")
                time.sleep(1)
                break
            else:
                print("Please enter a valid answer!")
                time.sleep(.3)

#--------------------------------------------------------

def multiplication(num1, num2):
    #This is for multiplication
    try:
        sum = float(num1) * float(num2)
        print("Your multiplied number should be =", str(sum))
        time.sleep(.1)
        while True:
            choice = input("Do you want to do something with your multiplied number? (y/n):").lower()
            time.sleep(.3)
            if choice == "y":
                second_math(sum)
                break
            else:
                break
        while choice == 'n' or not(choice == 'y'):
            choice2 = input("Do you want to go the main menu? (y/n):").lower()
            time.sleep(.3)
            if choice2 == "y":
                menu()
                break
            elif choice2 == "n":
                print("Goodbye!")
                time.sleep(1)
                break
            else:
                print("Please enter a valid answer")
                time.sleep(.3)
    except ValueError:
        while True:
            choice3 = input(("There's something wrong :(\nWould you like to go to the first menu? (y/n):")).lower()
            time.sleep(.3)
            if choice3 == "y":
                menu()
                break
            elif choice3 == "n":
                print("Goodbye!")
                time.sleep(1)
                break
            else:
                print("Please enter a valid answer!")
                time.sleep(.3)

#--------------------------------------------------------

def division(num1, num2):
    #This is for division
    try:
        sum = float(num1) / float(num2)
        print("Your divided number should be =", str(sum))
        time.sleep(.1)
        while True:
            choice = input("Do you want to do something with your divided number? (y/n):").lower()
            time.sleep(.3)
            if choice == "y":
                second_math(sum)
                break
            else:
                break
        while choice == 'n' or not(choice == 'y'):
            choice2 = input("Do you want to go the main menu? (y/n):").lower()
            time.sleep(.3)
            if choice2 == "y":
                menu()
                break
            elif choice2 == "n":
                print("Goodbye!")
                time.sleep(1)
                break
            else:
                print("Please enter a valid answer")
                time.sleep(.3)
    except ValueError:
        while True:
            choice3 = input(("There's something wrong :(\nWould you like to go to the first menu? (y/n):")).lower()
            time.sleep(.3)
            if choice3 == "y":
                menu()
                break
            elif choice3 == "n":
                print("Goodbye!")
                time.sleep(1)
                break
            else:
                print("Please enter a valid answer!")
                time.sleep(.3)

#--------------------------------------------------------

def menu():
    #This is the main menu
    print("Welcome to a simple calculator made by Iram Mahmud Ruhan!\nHere you can add, substact, multiply and divide\nThis is in pre-alpha(New features will be added soon!)")
    time.sleep(.3)
    print("Give me two numbers")
    time.sleep(.3)
    while True:
        num1 = input("Number 1: ")
        time.sleep(.3)
        if num1.isalpha():
            print("Please enter a number!")
            time.sleep(.3)
        else:
            break
    while True:
        num2 = input("Number 2: ")
        time.sleep(.3)
        if num2.isalpha():
            print("Please enter a number!")
            time.sleep(.3)
        else:
            break
    operate(num1, num2)
def operate(num1, num2):
    #This is the chosing menu
    print("If you want to add those numbers, click 1\nIf you want to subtract them, click 2\nIf you want to multiply them, click 3\nIf you want to divide them, click 4\nIf you want to exit, click 5")
    time.sleep(.3)
    while True:
        choice = input("Your choice: ")
        time.sleep(.3)
        if choice == "1":
            addition(num1, num2)
            break
        elif choice == "2":
            substraction(num1, num2)
            break
        elif choice == "3":
            multiplication(num1, num2)
            break
        elif choice == "4":
            division(num1, num2)
            break
        elif choice == "5":
            print("Goodbye!")
            time.sleep(.3)
            break
        else:
            print("Please enter a valid options!")
            time.sleep(1)
            
            

#--------------------------------------------------------

menu()