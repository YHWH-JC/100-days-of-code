print("You are on a journey to find the Word of Truth")

choice_one = input("pray or ignore? ")

if choice_one == "pray":
    choice_two = input("trust or doubt? ")
    if choice_two == "trust":
        choice_three = input("which scroll? red, blue or gold ")
        if choice_three == "red":
            print("False doctrine! Game Over.")
        elif choice_three == "blue":
            print( "Deception! Game Over.")
        elif choice_three == "gold":
            print( "You found the Word of Truth! You Win! 🙌")
        else:
            print("Game over")
    else:
        print("Fear consumed you. You turned back. Game Over.")
else:
    print("You walked your own path. Lost in the wilderness. Game Over.")

