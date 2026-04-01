spies = ["Joshua", "Caleb"]

while True:
    menu = int(input("Choose an action: 1 to Add, 2 to Remove, 3 to View, 4 to Send them out: "))
    if menu == 1:
        new_spy = input("What is the name of the new spy? ")
        spies.append(new_spy)
    elif menu == 2:
        remove_spies = input("What is the name of the spy you would like to remove? ")
        spies.remove(remove_spies)
    elif menu == 3:
        print(f"The current spies are {spies}")
    elif menu == 4:
        print("The spies have entered Canaan. May Yahweh protect them!")
        break
    else:
        print("Invalid input, please try again.")