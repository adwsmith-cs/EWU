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

def menu():
    user = 0
    while user != 10:
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
            menuItemEight()
        if user == 9:
            menuItemNine()
        if user == 10:
            print("thank you for using the menu")


def printMenu():
    print("1. Item one")
    print("2. Item two")
    print("3. Item three")
    print("4. Item four")
    print("5. Item five")
    print("6. Item six")
    print("7. Item seven")
    print("8. Item Eight")
    print("9. Item Nine")
    print("10. exit")
floatlist = [1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 6.6, 6.6, 7.7, 8.8, 9.9, 11.1, 21.2]
def menuItemOne():
    floatlist.append(11.0)
def menuItemTwo():
    floatlist.remove(3.3)
def menuItemThree():
    floatlist.pop(1)
def menuItemFour():
    print(floatlist)
def menuItemFive():
    total = 0
    for i in floatlist:
        total += i
    print(total/len(floatlist))

def menuItemSix():
    half = int(len(floatlist)/2)
    evenmed = floatlist[half-1], floatlist[half]
    #check if even
    if len(floatlist) % 2 == 0:
        print(f"{(floatlist[half-1]+floatlist[half])/2} {floatlist[half-1], floatlist[half]}")
    else:
        print(floatlist[half])
def menuItemSeven():
    start = floatlist[0]
    end = floatlist[-1]
    print((start + end) / 2)
def menuItemEight():
    #Get Mode
    tempc = 1
    finalc = 1
    findex = 0
    for i in range(len(floatlist)):
        for counter in range(i, len(floatlist)):
            if floatlist[counter] == floatlist[i]:
                tempc += 1
            if tempc > finalc:
                finalc = tempc
                findex = counter
                
            if finalc == 1:
                print("there is no mode")
        tempc = 1
    print(floatlist[findex])
    
            
def menuItemNine():
    total = 0
    squarediffs = []
    squaresum = 0
    for i in range(len(floatlist)):
        total += i
    mean = total/len(floatlist)
    for i in range(len(floatlist)):
        diff = i-mean
        squarediffs.append(diff*diff)
    for i in range(len(squarediffs)):
        squaresum += i
    print(squaresum/(len(squarediffs)-1))
    
def main():
    menu()

if __name__ == '__main__':
    main()
