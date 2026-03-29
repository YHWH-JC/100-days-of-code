import random
verses = [
    "Proverbs 3:5 - Trust in Yahweh with all your heart",
    "Psalm 23:1 - Yahweh is my shepherd, I shall not want",
    "John 3:16 - For Yahweh so loved the world..."
]
while True:
    print("\n What would you like to do?")
    print("1. View a memory verse")
    print("2. Take a Bible quiz")
    print("3. Read a devotional")
    print("4. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        verse = random.choice(verses)
        print(verse)
    elif choice == "2":
        choice_two = input("What is the first book of the Bible? ")
        if choice_two == "Genesis":
            print("Correct! ")
        else:
            print("Incorrect")
    elif choice == "3":
        print("Yahweh is not looking for perfect people — He is looking for willing hearts. Every morning His mercies are new. Draw near to Him today and He will draw near to you.\n— Based on Lamentations 3:22-23 & James 4:8")
    elif choice == "4":
        print("Shalom! Keep seeking Yahweh.")
        break