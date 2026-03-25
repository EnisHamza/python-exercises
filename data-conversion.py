def convert_to_string(values):
    # Convert string values to int
    valid_values = []
    for value in values:
        try:
            valid_values.append(int(value))
        except (ValueError, TypeError):
            continue
    return valid_values


values = ["10", "20", "abc", "40"]
print(convert_to_string(values))
