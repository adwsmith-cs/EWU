#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      adsmith
#
# Created:     20/09/2024
# Copyright:   (c) adsmith 2024
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import random

def menu():
    user = 0
    while user != 8:
        printMenu()
        user = int(input("type in the number of your choice"))
        if user == 1:
            menuItemOne()
        if user == 2:
            menuItemTwo()
        if user == 3:
            menuItemThree()
        if user == 4:
            menuItemFour()
        if user == 5:
            menuItemFive()
        if user == 6:
            menuItemSix()
        if user == 7:
            menuItemSeven()
        if user == 8:
            print("thank you for using the menu")


def printMenu():
    print("1. Item one")
    print("2. Item two")
    print("3. Item three")
    print("4. Item four")
    print("5. Item five")
    print("6. Item six")
    print("7. Item seven")
    print("8. exit")

def menuItemOne():
    width = 2.544
    height = 3.55
    area = width * height
    perimeter = width + width + height + height
    print("Width: " + str(width))
    print("Height: " + str(height))
    print("Area: " + str(area))
    print("Width: " + str(perimeter))
def menuItemTwo():
    width = float(input("What is the width of the rectangle"))
    height = float(input("What is the height of the rectangle"))
    printRectangle(width, height)
def menuItemThree():
    hole_num = int(input("Enter the hole number: "))
    par_val = int(input("Enter the par for the hole: "))
    strokes = int(input("Enter the number of strokes: "))

    parWord = ["Ostrich", "Condor", "Albatross", "Eagle", "Birdie", "Even Par", "Bogey", "Double Bogey", "Triple Bogey", "4 Over Par", "5 Over Par"]
    special_slang = []

    score_diff = strokes - par_val

    if score_diff < -5:
        par_result = "Ostrich"
    elif score_diff <= 5:
        index = score_diff + 5
        par_result = parWord[index]
    else:
        par_result = str(score_diff) + " Over Par"

    if strokes == 1:
        special_slang.append("Hole in One!")
    if strokes == 4:
        special_slang.append("Sailboat")
    if strokes == 8:
        special_slang.append("Snowman, Frosty")
    if strokes == 10:
        special_slang.append("Bo Derek")

    if strokes == (par_val * 2) and strokes != 1:
        special_slang.append("Beagle!")

    base_string = "On hole # " + str(hole_num) + " a par " + str(par_val) + " you shot a " + par_result

    if len(special_slang) == 1:
        print(base_string + ", with a " + special_slang[0] + ".")
    elif len(special_slang) == 2:
        print(base_string + ", with a " + special_slang[0] + ", a " + special_slang[1] + ".")
    else:
        print(base_string + ".")
    
def menuItemFour():
    total = 0
    startNum = int(input("What is the starting number"))
    endNum = int(input("What is the ending number"))
    for i in range(startNum, endNum, 1):
        if i/3 == int(i/3) and i/4 == int(i/4) and i/5 == int(i/5):
            total += i
    print("Starting Number: " + str(startNum))
    print("Ending Number: " + str(endNum))
    print(total)
        
def menuItemFive():
    rolls = int(input("How many rolls: "))
    roll_counts = [0] * 13
    doubles_count = 0
    snake_eyes_count = 0

    for i in range(rolls):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        
        roll_sum = dice1 + dice2
        roll_counts[roll_sum] += 1
        
        if dice1 == dice2:
            doubles_count += 1
            if dice1 == 1:
                snake_eyes_count += 1

    for i in range(2, 13):
        count = roll_counts[i]
        percentage = (count / rolls) * 100
        print(f"{i}- {percentage:.6f}%")

    doubles_percentage = (doubles_count / rolls) * 100
    print(f"Doubles-{doubles_percentage:.6f}%")
    
    snake_eyes_percentage = (snake_eyes_count / rolls) * 100
    print(f"Snake Eyes-{snake_eyes_percentage:.6f}%")
        
def menuItemSix():
    global word
    word = int(input("What number would you like reversed?: "))
    isNumberPalindrome(word)
def menuItemSeven():
    print("This is Menu Item 7")

def printRectangle(width, height):
    area = width * height
    perimeter = width + width + height + height
    print("Width: " + str(width))
    print("Height: " + str(height))
    print("Area: " + str(area))
    print("Width: " + str(perimeter))

def reverseString(word):
    global revWord
    revWord = ""
    
    for i in range(len(word),0,-1):
        revWord += word[i - 1]
    print(word)
    print(revWord)
    
    isPalindrome(word, revWord, True)
    

def isPalindrome(word, revWord, isRan):
    if isRan != True:
        reverseString(word)
        isRan = True
    elif word == revWord:
        print("True")
    else:
        print("False")

def isNumberPalindrome(word):
    isRan = False
    word = str(word)
    isPalindrome(word, "e", isRan)

def main():
    menu()

if __name__ == '__main__':
    main()
