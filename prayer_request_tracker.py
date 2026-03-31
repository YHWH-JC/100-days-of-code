menu = """---Prayer Request Tracker---
1. View all requests
2. Add a prayer request
3. Exit"""

prayer_request = []
while True:
    print(menu)
    choice = int(input("Pick a number: "))
    match choice:
        case 1:
            for index, request in enumerate(prayer_request):
                print(f"{index + 1}. {request}")
        case 2:
            request = input("Enter your prayer request: ")
            prayer_request.append(request)
            print("Request added! 🙏")
        case 3:
            print("Thank you for using our Prayer Request tracker")