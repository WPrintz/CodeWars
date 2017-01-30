"""
Is the string uppercase?
https://www.codewars.com/kata/56cd44e1aa4ac7879200010b
Solved 01-24-2017

Description: 8 kyu

Task

Create a method is_uppercase() to see whether the string is ALL CAPS. For example:

is_uppercase("c") == False
is_uppercase("C") == True
is_uppercase("hello I AM DONALD") == False
is_uppercase("HELLO I AM DONALD") == True
is_uppercase("ACSKLDFJSgSKLDFJSKLDFJ") == False
is_uppercase("ACSKLDFJSGSKLDFJSKLDFJ") == True
Corner Cases

For simplicity, you will not be tested on the ability to handle corner cases (e.g. "%*&#()%&^#" or similar strings containing alphabetical characters at all) - an ALL CAPS (uppercase) string will simply be defined as one containing no lowercase letters. Therefore, according to this definition, strings with no alphabetical characters (like the one above) should return True.
"""

import re
def is_uppercase(inp):
    if inp.upper() == inp:
        return True
    elif re.match('[a-z]',inp) != None:
        return False
    else:
        return False