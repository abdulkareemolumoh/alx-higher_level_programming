#!/usr/bin/python3

def update_dictionary(a_dictionary, key, value):
    a_dictionary[key] = value

# Example usage
my_dict = {'a': 1, 'b': 2, 'c': 3}
update_dictionary(my_dict, 'b', 5)
update_dictionary(my_dict, 'd', 4)
print(my_dict)  # Output: {'a': 1, 'b': 5, 'c': 3, 'd': 4}

