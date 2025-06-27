# Python Developer Basic Math Interview Questions
# ===============================================
# Write your solutions in the functions provided below

# 1. Check if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# 2. Generate Fibonacci series up to n terms
def fibonacci_series(n):
    series = []
    a, b = 0, 1
    for _ in range(n):
        series.append(a)
        a, b = b, a + b
    return series

# 3. Calculate factorial of a number
def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

# 4. Check if a number is an Armstrong number
def is_armstrong(n):
    digits = [int(d) for d in str(n)]
    power = len(digits)
    return sum(d ** power for d in digits) == n

# 5. Find GCD of two numbers
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# 6. Convert decimal to binary
def decimal_to_binary(n):
    return bin(n)[2:]

# 7. Print multiplication table of a number up to 10
def multiplication_table(n):
    return [f"{n} x {i} = {n * i}" for i in range(1, 11)]

# 8. Check if a number is palindrome
def is_palindrome(n):
    return str(n) == str(n)[::-1]

# 9. Find the sum of digits of a number
def sum_of_digits(n):
    return sum(int(d) for d in str(abs(n)))

# 10. Find all prime numbers in a range
def primes_in_range(start, end):
    return [x for x in range(start, end + 1) if is_prime(x)]

# BONUS: Entry point for testing
if __name__ == '__main__':
    print("Run individual functions to test your logic.")
    # Example test
    print("is_prime(7):", is_prime(7))
    print("fibonacci_series(5):", fibonacci_series(5))
    print("factorial(5):", factorial(5))
    print("is_armstrong(153):", is_armstrong(153))
    print("gcd(48, 18):", gcd(48, 18))
    print("decimal_to_binary(10):", decimal_to_binary(10))
    print("multiplication_table(5):")
    for line in multiplication_table(5):
        print(line)
    print("is_palindrome(121):", is_palindrome(121))
    print("sum_of_digits(1234):", sum_of_digits(1234))
    print("primes_in_range(10, 20):", primes_in_range(10, 20))
