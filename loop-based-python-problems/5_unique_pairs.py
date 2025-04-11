"""
Problem 5: Generate All Unique Pairs from a List Without Repetition
"""

def generate_unique_pairs(lst):
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            print(f"({lst[i]}, {lst[j]})")

# Example
generate_unique_pairs([1, 2, 3])
