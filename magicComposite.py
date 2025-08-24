def is_magic_number(n):
    """
    Checks if a number is a magic number.
    A magic number's eventual sum of digits is 1.
    For example: 28 -> 2+8=10 -> 1+0=1
    """
    while n > 9:  # Keep summing until the number is a single digit
        sum_of_digits = 0
        temp_n = n
        while temp_n > 0:
            sum_of_digits += temp_n % 10  # Add the last digit
            temp_n //= 10 # Remove the last digit (will only give the last quotient, like 145/10 =14.5 in  python but 145//10 will be only 14)
        n = sum_of_digits
    return n == 1

def is_composite_number(n):
    """
    Checks if a number is a composite number.
    A composite number has more than two factors.
    Returns True for composite numbers and False for prime numbers or 1.
    """
    if n <= 1:
        return False
    # Check for factors from 2 up to the square root of n
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return True  # Found a factor, so it's composite
    return False

def find_composite_magic_numbers(m, n):
    """
    Finds and displays all composite magic numbers in the range [m, n].
    """
    if m > n or m < 1:
        print("Invalid range. Please enter m < n and both as positive integers.")
        return

    composite_magic_list = []
    
    # Iterate through the given range
    for num in range(m, n + 1):
        # Check if the number is both a magic number and a composite number
        if is_magic_number(num) and is_composite_number(num):
            composite_magic_list.append(num)

    # Display the results
    if not composite_magic_list:
        print(f"No composite magic numbers found in the range {m} to {n}.")
    else:
        print(f"Composite magic numbers in the range {m} to {n}:")
        for number in composite_magic_list:
            print(number, end=" ")
        print(f"\nFrequency of composite magic integers: {len(composite_magic_list)}")

# Get the range from the user
try:
    lower_range = int(input("Enter lower range (m): "))
    upper_range = int(input("Enter upper range (n): "))
    find_composite_magic_numbers(lower_range, upper_range)
except ValueError:
    print("Invalid input. Please enter valid integer numbers for the range.")

