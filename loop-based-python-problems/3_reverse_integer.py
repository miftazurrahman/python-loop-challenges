"""
Problem 3: Reverse an Integer Without String Conversion
"""

def reverse_integer(n):
    rev = 0
    while n > 0:
        rev = rev * 10 + n % 10
        n = n // 10
    return rev

# Example
print("Reversed:", reverse_integer(1234))
