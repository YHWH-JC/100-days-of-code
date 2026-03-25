degrees_fahrenheit = int(input("Please type in a temperature (F): "))
c = (degrees_fahrenheit - 32) / 1.8
message = f"{degrees_fahrenheit} degrees Fahrenheit equals {c} degrees Celsius"
if c < 0:
    print(message)
    print("Brr! It's cold in here!")
else:
    print(message)