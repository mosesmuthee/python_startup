def detect_even_odd(number):
    # Check if the number is even
    if number % 2 == 0:
        return f"{number} is an even number."
    else:
        return f"{number} is an odd number."

# Example usage
numbers_to_check = [10, 1, 32, 43, 5543]

for number in numbers_to_check:
    result = detect_even_odd(number)
    print(result)