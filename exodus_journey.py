leader_name = input("What is the leader's name? ")
manna_rations = 100
water_flasks = 5

print(f"God bless you {leader_name}. Your starting manna rations is {manna_rations} and your starting water flasks is {water_flasks}.")

leader_manna_rations = int(input("How many manna rations will you pass out to the tribes today? "))

manna_rations = manna_rations - leader_manna_rations

if manna_rations < 0:
    print("You promised more food than you have! The camp is complaining!")
else:
    print(f"The camp is fed. You have {manna_rations} rations left.")

fork_in_the_road = input("You reach a fork in the wilderness. Do you travel to the 'mountains', the 'sea', or the 'desert'? ")

if fork_in_the_road == "mountains":
    print("You found a safe cave, but you lost 1 water flask.")
    water_flasks -= 1
elif fork_in_the_road == "sea":
    print("Pharaoh's army is approaching, Yahweh will part the sea.")
elif fork_in_the_road == "desert":
    print("The sun is extremely hot, you won't make it without YAHWEH.")
else:
    print("Invalid input.")

print(f"Here is your final report for the day {leader_name}. Your final manna count is {manna_rations} and your final water count is {water_flasks}")

