print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

print("welcome to tresure island")
print("your mission is find a tresure")
first_choice = input("Where do you wanna go? left or right").lower()

if first_choice == "left":
    second_choice = input('You\'ve come to a lake, There is a island on the middle of the lake, do you wanna "wait" for a boat or "swim?"').lower()
    if second_choice == "wait":
        third_choice = input("you arrived at the island there is a house with three doors red blue and yellow what do ou chose?").lower()
        if third_choice == "yellow":
            print("you found the tresure!")
        else:
            print("game over you were close!")
    if second_choice == "right":
        print("you got attacked by shark, game over!")
    else:
        print("?")
if first_choice == "right":
    print("bad way, game over")
