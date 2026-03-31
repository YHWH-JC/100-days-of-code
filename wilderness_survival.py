print("---The Wilderness Survival Loop---")

miles_to_go = 100
manna = 50
water = 50

while miles_to_go > 0:
    print(f"Miles left: {miles_to_go} | Manna: {manna} | Water: {water}")
    action = input("Do you want to 'travel' or 'scavenge' ")
    if action == "travel":
        miles_to_go -= 20
        manna -= 15
        water -= 15
    elif action == "scavenge":
        manna += 20
        water += 20
    else:
        print("You wasted a day doing nothing.")
        manna -= 5
        water -= 5
    if manna <= 0 or water <= 0:
        print("You have run out of resources and perished in the wilderness.")
        break
if miles_to_go <= 0:
    print("Hallelujah! You have reached the Promised Land!")