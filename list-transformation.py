numbers = [1, 2, 3, 4, 5]
# Returning a list of squares of even numbers using list comprehension
square_number = [number ** 2 for number in numbers if number % 2 == 0]
print(square_number)
