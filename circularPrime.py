import math

def is_prime_optimized(n):
    """
    Checks if a number is prime with optimized time complexity.
    """
    # A prime number is a natural number greater than 1
    if n <= 1:
        return False
    # 2 and 3 are prime numbers
    if n <= 3:
        return True
    # If n is divisible by 2 or 3, it's not prime
    if n % 2 == 0 or n % 3 == 0:
        return False
    # Check for factors from 5 up to the square root of n
    # The step of 6 ensures we only check numbers of the form 6k ± 1
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    # If no factors are found, the number is prime
    return True

# Example usage:
print(is_prime_optimized(7))  # Output: True
print(is_prime_optimized(10)) # Output: False
print(is_prime_optimized(97)) # Output: True
print(is_prime_optimized(121)) # Output: False