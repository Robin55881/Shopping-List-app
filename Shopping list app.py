# Shopping list app 
import sys


def mainManu():
    while True:
        print("##### Shopping List ######")
        
        # This is a list of maintain
        print(
            """Select a number for the action that you would like to do?\n
1. View Shopping list.\n
2. Add item to shopping list.\n
3. Remove item from shopping list\n
4. Check if item is on shopping list.\n
5. How many items on shopping list.\n
6. Clear shopping list.\n
7. Exit."""
        )
        selection = input("Make your selection:")
        if selection == "1":
            displayList()
        elif selection == "2":
            addItem()
        elif selection == "3":
            removeItem()
        elif selection == "4":
            checkItem()
        elif selection == "5":
            itemLength()
        elif selection == "6":
            clearItem()
        elif selection == "7":
            sys.exit()
        else:
            print("You did not make a valid selection")

# List of Shopping 
shoppingList = ["apple", "Banana", "Carot", "Cerry", "Potatos", "Grap", "jackfruit"]


# This part is item Selection part
def displayList():
    for i in shoppingList:
        print('### Shopping List ###')
        print("* " +i)


 # This part is item add part       
def addItem():
    item= input ("Enter the item you wise the add to item list:")
    shoppingList.append(item)
    print(item+" has been added in Your item list.")

  # This part is item remove  
def removeItem():
    item= input ("Enter the item you wise the remove to item list:")
    shoppingList.remove(item)
    print(item+" has been removed in Your item list.")

 # This part is item Check   
def checkItem():
    item= input ("Enter the item you wise the Check to item list:")
    if item in shoppingList:
        print("Yes, that " +item+" in shopping list.")
    else:
        print("No, that "+item+" not in shopping list.")


# This part is item length
def itemLength():
    print("There are ",len(shoppingList)," item of shopping List.")

 # This part is item Clear

def clearItem():
   
    print(shoppingList.clear()," No, item in your shopping List.")


    
mainManu()
