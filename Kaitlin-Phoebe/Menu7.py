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
    mylist = [1,2,3,4,5]
    print(mylist)
    mylist.append(int(input("Type a number to add to the list: ")))
    print(mylist)
def menuItemTwo():
    mylist=[5,4,3,2,1]
    print(mylist)
    mylist.remove(int(input("Type a number to remove from the list:")))
    print(mylist)
def menuItemThree():
    mylist=[2,1,3,5,4]
    print(mylist)
    mylist.pop(int(input("Type position of number to remove:"))-1)
    print(mylist)
def menuItemFour():
    mylist=[1,5,3,4,2]
    print(mylist)
def menuItemFive():
    mylist=[5,2,1,3,4,]
    print(mylist)
    total=0
    for i in range(len(mylist)):
        total+=mylist[i]
    total/=len(mylist)
    print(total)
def menuItemSix():
    mylist[1,2,3,4,5]
    print(mylist)
if len(list)%2==1:
    (mylist)[int(len(mylist)/2)]
else: (mylist)[(int(len(mylist)/2))]+mylist[(len((mylist))/2)-1]/2
print(mylist)

    
def menuItemSeven():
    print("This is Menu Item 7")

def main():
    menu()

if __name__ == '__main__':
    main()
