user_age = int(input("Age: "))

is_student = input("Are you a student? yes or no? ").lower().strip()
bill = 0
if user_age < 5:
    bill = 0
elif user_age >= 5 and user_age <= 12:
    bill = 8
elif is_student == "yes" and user_age >= 13:
    bill = 10
elif user_age >= 13 and user_age <= 17:
    bill = 12
elif user_age >= 18 and user_age <= 64:
    bill = 15
elif user_age >= 65:
    bill = 10
print(f"Your ticket price is ${bill}")