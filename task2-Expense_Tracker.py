total = 0
while True:
    user_input = input("Enter expense or type 'quit': ")
    if user_input == "quit":
        break
    try:
        expense = int(user_input)
        total += expense
        print("Current Total:", total)
    except ValueError:
        print("Invalid input! Please enter numbers only.")
print("Final Total Spent:", total)