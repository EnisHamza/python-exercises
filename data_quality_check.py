records = [{"user_id": 1, "age": 25, "email": "test@gmail.com"},
           {"user_id": 2, "age": -5, "email": "invalid-email"},
           {"user_id": None, "age": 30, "email": "user@mail.com"}]


def validate_data(records):
    # Validate records list and return new list of invalid records and reason why they are invalid
    invalid_records = []

    for record in records:
        reasons = []

        if record["user_id"] == None:
            reasons.append("User id must not be None")

        if record["age"] < 0:
            reasons.append("Age must be positive number")

        if not "@" in record["email"]:
            reasons.append("Email must contain @")

        if reasons:
            invalid_records.append({
                "record": record,
                "reasons": reasons
            })
    return invalid_records


print(validate_data(records))
