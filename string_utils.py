"""14. Implement a Python module named string_utils.py containing functions for string manipulation, such as
reversing and capitalizing strings."""

def reverse(s):
    reversed_str = ""
    for char in s:
        reversed_str = char + reversed_str
    return reversed_str

def capitalize(s):
    return s.capitalize()