print("----Bible Quiz----")
q1 = input("Who built the ark? ").strip().lower()
q2 = int(input("How many days did Yeshua fast in the wilderness? "))
q3 = input("What city was Yeshua born in? ").strip().lower()

score = 0

if q1 == "noah":
    score +=1
    print("Correct! ✅")
else:
    print("Wrong ❌ The answer was noah")
if q2 == 40:
    score += 1
    print("Correct! ✅")
else:
    print("Wrong ❌ The answer was 40")
if q3 == "bethlehem":
    score += 1
    print("Correct! ✅")
else:
    print("Wrong ❌ The answer was bethlehem")
print(f"Your score: {score}/3")
if score == 3:
    print("Perfect score! Yahweh is pleased with you.")
elif score == 2:
    print("Well done! Keep studying the Word.")
elif score == 1:
    print("Keep seeking Yahweh. His Word is a lamp to your feet.")
else:
    print("Don't give up! Open your Bible and try again.")