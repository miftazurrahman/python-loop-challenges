"""
Problem 2: Count and Print All Even and Odd Numbers in a Range
"""

def print_even_odd(start, end):
    evens = []
    odds = []
    for i in range(start, end + 1):
        if i % 2 == 0:
            evens.append(i)
        else:
            odds.append(i)
    print("Even:", *evens)
    print("Odd:", *odds)

# Example
print_even_odd(1, 10)
