print("Bible Study Registration Program")
user_member = input("Are you a member of the church? Type y for Yes and n for No ")
bill = 0

if user_member == "y":
    user_age = int(input("How old are you? "))
    if user_age < 13:
        bill += 0
        print("Children's bible study is free.")
    elif user_age >= 13 and user_age <= 17:
        bill += 5
        print("Youth bible study cost $5.")
    else:
        bill += 10
        print("Adult bible study cost $10.")
    study_workbook = input("Would you like a study workbook? y for Yes and n for No ")
    if study_workbook == "y":
        bill += 3
        print("A study workbook is $3.")
    print(f"Your total registration cost is: ${bill}")
else:
    print("Please speak to a pastor to join our congregation!")