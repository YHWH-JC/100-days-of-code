import random
verses = [
    "Proverbs 3:5 - Trust in Yahweh with all your heart and lean not on your own understanding.",
    "Psalm 23:1 - Yahweh is my shepherd, I shall not want.",
    "Joshua 1:9 - Be strong and courageous. Do not be afraid, for Yahweh your God is with you.",
    "Isaiah 40:31 - Those who hope in Yahweh will renew their strength and soar on wings like eagles.",
    "Jeremiah 29:11 - For I know the plans I have for you, declares Yahweh, plans to prosper you."
]

while True:
    print("1. Show all verses")
    print("2. Show a random verse")
    print("3. Exit")
    user_choice = int(input("Pick a number: "))
    if user_choice == 1:
        for index, verse in enumerate(verses):
            print(f"Verse {index + 1}: {verse}")
    elif user_choice == 2:
        print(random.choice(verses))
    elif user_choice == 3:
        print("Goodbye, I hope you enjoyed our app.")
        break
    else:
        print("Invalid input.")