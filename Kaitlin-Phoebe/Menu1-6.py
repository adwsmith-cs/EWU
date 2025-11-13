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
import turtle
import random

totalroll = 0
doubles = 0

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
    bobjr = turtle.Turtle()
    width = 2.544
    height = 3.55
    for i in range(2):
        bobjr.forward(width)
        bobjr.left(90)
        bobjr.forward(height)
        bobjr.left(90)
    width = float(input("enter width"))
    height = float(input("enter height"))
    for i in range(2):
        bobjr.forward(width)
        bobjr.left(90)
        bobjr.forward(height)
        bobjr.left(90)
    width = 5
    height = 2
    for i in range(2):
        bobjr.forward(width)
        bobjr.left(90)
        bobjr.forward(height)
        bobjr.left(90)
    width = float(input("enter width again"))
    height = float(input("enter height again"))
    for i in range(2):
        bobjr.forward(width)
        bobjr.left(90)
        bobjr.forward(height)
        bobjr.left(90)
    width = 10
    height = 10
    for i in range(2):
        bobjr.forward(width)
        bobjr.left(90)
        bobjr.forward(height)
        bobjr.left(90)
    width = float(input("enter width AGAIN AGAIN"))
    height = float(input("enter height AGAIN AGAIN"))
    for i in range(2):
        bobjr.forward(width)
        bobjr.left(90)
        bobjr.forward(height)
        bobjr.left(90)
        
def printrectangle(height,width):
        bobjr = turtle.Turtle()
        perimeter= 12.188
        area= 9.031
        for i in range(2):
            bobjr.forward(width)
            bobjr.left(90)
            bobjr.forward(height)
            bobjr.left(90)
           
def uirectangle():
        height=float(input("enter height"))
        width=float(input("enter width"))
        printrectangle(height,width)
        
def menuItemTwo():
    bobjr = turtle.Turtle()
    printrectangle(3.55,2.544)
    uirectangle()

def evaluate():
    holeNum=str(input("what hole are you on?"))
    parValue=int(input("What is the value of par?"))
    strokes=int(input("How many strokes did you need to complete the hole?"))
    score= strokes-parValue
    scoreSlang=0
    special=0
    if score == 0:
        scoreSlang = "even par"
    elif score == 1:
        scoreSlang = "Bogey"
    elif score == 2:
        scoreSlang = "Double Bogey"
    elif score == 3:
        scoreSlang = "Triple Bogey"
    elif score == 4:
        scoreSlang = "4 over par"
    elif score == 5:
        scoreSlang = "5 over par"
    elif score == 6:
        scoreSlang = "6 over par"
    elif score == 7:
        scoreSlang = "7 over par"
    elif score == 8:
        scoreSlang = "8 over par"
    elif score == -1:
        scoreSlang = "Birdie"
    elif score == -2:
        scoreSlang = "Eagle"
    elif score == -3:
        scoreSlang = "Albatross"
    elif score == -4:
        scoreSlang == "Condor"
    elif score == -5:
        scoreSlang == "Ostrich"
    else:
        scoreSlang = "I don't know"
    if strokes ==1:
        special="with a Hole in One!"
    elif strokes ==4:
        special="with a Sailboat."
    elif strokes ==8:
        special="with a Snowman."
    elif strokes ==10:
        special ="with a Bo Derek."
    else:
        special= "."
    if strokes == parValue*2:
        scoreSlang = "Beagle"
    print("On hole "+ holeNum +" a par " + str(parValue) + " you shot a " + scoreSlang + " " + special)

        
def menuItemThree():
    evaluate()

def menuItemFour():
    startnum=(int(input("Starting number: ")))
    endnum=(int(input("Ending number: ")))
    total = 0
    for i in range(startnum,endnum):
        if i % 3 != 0:
            if i % 4 != 0:
                    if i % 5 != 0:
                        total += i
    print(startnum,endnum,total)

def rollDie():
    global totalroll
    global doubles
    dice1roll = (random.randint(1,6))
    dice2roll = (random.randint(1,6))
    if dice1roll == dice2roll:
        doubles += 1
    else:
        totalroll = dice1roll + dice2roll

def menuItemFive():
    rolls=(int(input("How many times do you want to roll the dice: ")))
    global totalroll
    twos = 0
    threes = 0
    fours = 0
    fives = 0
    sixes = 0
    sevens = 0
    eights = 0
    nines = 0
    tens = 0
    elevens = 0
    twelves = 0
    per2 = 0
    per3 = 0
    per4 = 0
    per5 = 0
    per6 = 0
    per7 = 0
    per8 = 0
    per9 = 0
    per10 = 0
    per11 = 0
    per12 = 0
    dubper = 0
    for i in range(rolls):
        rollDie()
        if totalroll==2:
               twos += 1
        if totalroll==3:
               threes += 1
        if totalroll==4:
               fours += 1
        if totalroll==5:
               fives += 1
        if totalroll==6:
               sixes += 1
        if totalroll==7:
               sevens += 1
        if totalroll==8:
               eights += 1
        if totalroll==9:
               nines += 1
        if totalroll==10:
               tens += 1
        if totalroll==11:
               elevens += 1
        if totalroll==12:
               twelves += 1
        per2 = (twos/rolls)*100
        per3 = (threes/rolls)*100
        per4 = (fours/rolls)*100
        per5 = (fives/rolls)*100
        per6 = (sixes/rolls)*100
        per7 = (sevens/rolls)*100
        per8 = (eights/rolls)*100
        per9 = (nines/rolls)*100
        per10 = (tens/rolls)*100
        per11 = (elevens/rolls)*100
        per12 = (twelves/rolls)*100
        dubper = (doubles/rolls)*100
    print("2: "+str(twos)+" - "+str(per2)+"%")
    print("3: "+str(threes)+" - "+str(per3)+"%")
    print("4: "+str(fours)+" - "+str(per4)+"%")
    print("5: "+str(fives)+" - "+str(per5)+"%")
    print("6: "+str(sixes)+" - "+str(per6)+"%")
    print("7: "+str(sevens)+" - "+str(per7)+"%")
    print("8: "+str(eights)+" - "+str(per8)+"%")
    print("9: "+str(nines)+" - "+str(per9)+"%")
    print("10: "+str(tens)+" - "+str(per10)+"%")
    print("11: "+str(elevens)+" - "+str(per11)+"%")
    print("12: "+str(twelves)+" - "+str(per12)+"%")
    print("Doubles: "+str(doubles)+" - "+str(dubper)+"%")

def reverseString(numstring):
    newString = ""
    for i in range(len(numstring)-1,-1,-1):
        newString += numstring[i]
    if newString == numstring:
        return True
    else:
        return False

def addPalindromes(beg,end):
    total = 0
    for i in range(beg,end,1):
        if reverseString(str(i)):
            total += i
    print(total)
        
def menuItemSix():
    addPalindromes(int(input("give me a number")),int(input("give me another number")))
    

def menuItemSeven():
    print("This is Menu Item 7")

def main():
    menu()
    


if __name__ == '__main__':
    main()
