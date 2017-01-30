"""
Shortest Word
https://www.codewars.com/kata/57cebe1dc6fdc20c57000ac9
Solved 01-26-2017

Description: 7 kyu

x Simple, given a string of words, return the length of the shortest word(s).

String will never be empty and you do not need to account for different data types.
"""

def find_short(s):
    test = s.split()
    minword=10000000
    for x in test:
        if len(x) < minword:
            minword = len(x)

    return minword