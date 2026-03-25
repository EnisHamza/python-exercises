transactions = [{"id": 1, "amount": 120, "status": "completed"},
                {"id": 2, "amount": -20, "status": "completed"},
                {"id": 3, "amount": 50, "status": "failed"},
                {"id": 4, "amount": 200, "status": "completed"}]


def get_valid_transactions(transactions):
    # Return only the transactions that fulfill the conditions
    valid_transactions = []

    for transaction in transactions:
        if transaction["amount"] > 0 and transaction["status"] == "completed":
            valid_transactions.append(transaction)
    return valid_transactions


print(get_valid_transactions(transactions))
