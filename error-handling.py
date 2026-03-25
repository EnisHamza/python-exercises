def withdraw(balance, amount):
    # Withdrawing amount from the balance and handling errors without crashing the app
    try:
        if amount > balance:
            raise ValueError("Amount can not be grater than balance!")
        if amount < 0:
            raise ValueError("Invalid amount!")
        new_balance = balance - amount
        return f"Withdrawal successful. Your current balance is: {new_balance}"
    except ValueError as error:
        print("Error: ", error)
        return f"Your current balance is: {balance}"


print(withdraw(30, 20))
