print("---Tithe Calculator---")
user_shekels = int(input("How many silver shekels did you earn this year? "))
tithe_amount = user_shekels * .10
kept_amount = user_shekels - tithe_amount

print(f"God bless you fellow beliver. Your tithe amount is {tithe_amount} and you will be keeping {kept_amount}")