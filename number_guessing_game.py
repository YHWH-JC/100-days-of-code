import random

computer_choice = random.randint(1,100)
attempts_counter = 0

print("---Number Guessing Game---")
while True:
    user_guess = int(input("Guess a number between 1 and 100: "))
    attempts_counter += 1
    if user_guess < computer_choice:
        print("Too low")
    elif user_guess > computer_choice:
        print("Too high")
    else:
        print(f"You got it in {attempts_counter} attempts!")
        break