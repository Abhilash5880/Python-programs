"""
This program generates all prime numbers within a user-defined range.
A prime number is a natural number greater than 1 that has no positive divisors
other than 1 and itself.
"""

def is_prime(n):
    """
    Checks if a number is prime.

    Args:
        n (int): The number to check.

    Returns:
        bool: True if the number is prime, False otherwise.
    """
    # Prime numbers must be greater than 1.
    if n <= 1:
        return False
    # 2 is the only even prime number.
    if n == 2:
        return True
    # All even numbers greater than 2 are not prime.
    if n % 2 == 0:
        return False
    # Check for odd divisors from 3 up to the square root of n.
    # We can skip even numbers as they are not divisors.
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

def generate_primes_in_range(start, end):
    """
    Generates and prints all prime numbers within a specified range.

    Args:
        start (int): The start of the range (inclusive).
        end (int): The end of the range (inclusive).
    """
    if start > end:
        print("Error: The start of the range cannot be greater than the end.")
        return

    print(f"\nPrime numbers between {start} and {end}:")
    
    found_primes = False
    for number in range(start, end + 1):
        if is_prime(number):
            print(number, end=" ")
            found_primes = True

    if not found_primes:
        print("No prime numbers found in this range.")
    else:
        print() # Print a newline for better formatting

# Main part of the program
if __name__ == "__main__":
    try:
        # Prompt the user to enter the range
        start_range = int(input("Enter the starting number of the range: "))
        end_range = int(input("Enter the ending number of the range: "))

        # Call the function to generate and print primes
        generate_primes_in_range(start_range, end_range)

    except ValueError:
        print("Invalid input. Please enter whole numbers.")
