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
from random import randint
def menu():
    user = 0
    while user != 8:
        printMenu()
        user = int(input("type in the number of your choice: "))
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
def printRectangle(w, h):
    print(f"\nWidth: {w}\nHeight: {h}\nArea: {h*w}\nPerimeter: {2*(w+h)}\n")
    
def menuItemOne():
    #set rectangle
    width, height = 2.544, 3.55
    print(f"\nWidth: {width}\nHeight: {height}\nArea: {height*width}\nPerimeter: {2*(width+height)}\n")

    
def menuItemTwo():
    w = float(input("Enter the width: "))
    h = float(input("Enter the height: "))
    printRectangle(w,h)
def menuItemThree():
    try:
        holenum, par, strokes = int(input("Hole Number: ")), int(input("Par: ")), int(input("Strokes: "))
        diff = strokes - par
        s2p = {
            -5 : "Ostrich",
            -4 : "Condor",
            -3 : "Albatross",
            -2 : "Eagle",
            -1 : "Birdie",
            0 : "Even Par",
            1 : "Bogey",
            2 : "Double Bogey",
            3 : "Triple Bogey",
            4 : "4 Over Par",
            5 : "5 Over Par"
            }
        def extra():
            if strokes == 1:
                return ", with a hole in one"
            elif strokes == 4:
                return ", with a Sailboat"
            elif strokes == 8:
                return ", with a Frosty"
            elif strokes == 10:
                return ", with a Bo Derek"
            else:
                return ""
        print(f"On Hole #{holenum}, a par {par}, you shot a(n) {s2p[diff]}{extra()}")
    except KeyError:
        print(f"On Hole #{holenum}, a par {par}, you shot {strokes}{extra()} ")

def menuItemFour():
    start = int(input("Starting point: "))
    end = int(input("Ending point: "))
    count = 0
    for i in range(start, end):
        if i % 3 != 0 and i % 4 != 0 and i % 5 != 0:
            count += i
        
    print(f"\nStarting Number: {start}\nEnding Number: {end}\nTotal: {count}\n")
    
        
def perc(number, rolls):
    percent = (number / rolls) * 100
    return (f"{percent:.2f}%")
    

def menuItemFive():
    rollamount = int(input("Enter Amount of Rolls: "))
    two = 0
    three = 0
    four = 0
    five = 0
    six = 0
    seven = 0
    eight = 0
    nine = 0
    ten = 0
    eleven = 0
    twelve = 0
    doubles = 0
    for i in range(rollamount):
        dice1, dice2 = randint(1,6), randint(1,6)
        total = dice1+dice2
        if total == 2:
            two += 1
        elif  total == 3:
            three += 1
        elif total == 4:
            four += 1
        elif total == 5:
            five += 1
        elif total == 6:
            six += 1
        elif total == 7:
            seven += 1
        elif total == 8:
            eight += 1
        elif total == 9:
            nine += 1
        elif total == 10:
            ten += 1
        elif total == 11:
            eleven += 1
        elif total == 12:
            twelve += 1
        if dice1 == dice2:
            doubles += 1
    print(f"2 - {two} {perc(two, rollamount)}")
    print(f"3 - {three} {perc(three, rollamount)}")
    print(f"4 - {four} {perc(four, rollamount)}")
    print(f"5 - {five} {perc(five, rollamount)}")
    print(f"6 - {six} {perc(six, rollamount)}")
    print(f"7 - {seven} {perc(seven, rollamount)}")
    print(f"8 - {eight} {perc(eight, rollamount)}")
    print(f"9 - {nine} {perc(nine, rollamount)}")
    print(f"10 - {ten} {perc(ten, rollamount)}")
    print(f"11 - {eleven} {perc(eleven, rollamount)}")
    print(f"12 - {twelve} {perc(twelve, rollamount)}")
    print(f"Doubles - {doubles} {perc(doubles, rollamount)}")


def reverseString(string):
    print(string[::-1])
def isPalindrome(string):
    if string == string[::-1]:
        print(True)
    else:
        print(False)
def isNumberPalindrome(num):
    if str(num) == str(num)[::-1]:
        print(True)
    else:
        print(False)
    
def menuItemSix():
    reverseString("tacocat")
    isPalindrome("tacocat")
    isNumberPalindrome("101")
    
def menuItemSeven():
    print("This is Menu Item 7")

def main():
    menu()

if __name__ == '__main__':
    main()
