#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
  """
  Prints a dictionary by ordered keys.

  Args:
    a_dictionary: The dictionary to print.
  """

  keys = sorted(a_dictionary.keys())
  for key in keys:
    print(f"{key}: {a_dictionary[key]}")


