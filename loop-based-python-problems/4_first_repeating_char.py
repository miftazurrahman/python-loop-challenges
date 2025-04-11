"""
Problem 4: Find the First Repeating Character in a String
"""

def first_repeating_char(s):
    seen = set()
    for char in s:
        if char in seen:
            return char
        seen.add(char)
    return None

# Example
print("First repeating character:", first_repeating_char("interview"))
