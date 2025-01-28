# Module for string manipulation, such as reversing and capitalizing strings

def string_reverse(s):
    rev_s = ""

    for char in s:
        rev_s = char + rev_s

    return rev_s

def capitalize(s):
    return s.upper()