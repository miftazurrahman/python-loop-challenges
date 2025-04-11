"""
Problem 1: Right-Angled Triangle Pattern
Print a right-angled triangle with n rows.
"""

def print_triangle(n):
    for i in range(1, n + 1):
        print('*' * i)

# Example
print_triangle(5)
