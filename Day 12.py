# Declare a function named evens_and_odds . It takes a positive integer as parameter and it counts number of evens and odds in the number.
def evens_and_odds(number):
    if number < 0:
        raise ValueError("The number must be a positive integer.")    
    even_count = 0
    odd_count = 0
    # Convert the number to a string to iterate through each digit
    num_str = str(number)
    for digit_char in num_str:
        # Convert the character digit back to an integer
        digit = int(digit_char)
        # Check if the digit is even or odd using the modulo operator
        if digit % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    return {"evens": even_count, "odds": odd_count}
my_number = 12345
counts = evens_and_odds(my_number)
print(f"The number is: {my_number}")
print(f"Number of even digits: {counts['evens']}")
print(f"Number of odd digits: {counts['odds']}")

