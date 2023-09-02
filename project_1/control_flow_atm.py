def deposit():
    amount = int(input("Enter amount to deposit: "))
    new_balance = balance + amount
    print(f"You have deposited ${amount} to your account. Your balance is now ${new_balance}.")

def withdraw():
    amount = int(input("Enter amount to withdraw: "))
    new_balance = balance - amount
    print(f"You have withdrawn ${amount} from your account. Your balance is now ${new_balance}.")

def handler():
    command = input("Enter d to deposit or w to withdraw: ")
    if command == "d" or command == "D":
        deposit()
    elif command == "w" or command == "W":
        withdraw()
    else:
        print("Enter d to deposit or w to withdraw: ")

balance = 2000
pin = 1234

user_input = int(input("Enter your pin: "))

if user_input == pin:
    #print(f"Your balance is ${balance}")
    handler()
else:
    print("Wrong pin! Try again")
