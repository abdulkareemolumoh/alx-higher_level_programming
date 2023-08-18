#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    diff_elements = set_1.symmetric_difference(set_2)
    return diff_elements

# Example usage
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
result = only_diff_elements(set1, set2)
print(result)  # Output: {1, 2, 5, 6}

