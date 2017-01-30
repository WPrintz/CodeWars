"""
Mumbling
https://www.codewars.com/kata/5667e8f4e3f572a8f2000039
Solved 01-24-2017

Description: 7 kyu

This time no story, no theory. The examples below show you how to write function accum:

Examples:

accum("abcd")    # "A-Bb-Ccc-Dddd"
accum("RqaEzty") # "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
accum("cwAt")    # "C-Ww-Aaa-Tttt"
The parameter of accum is a string which includes only letters from a..z and A..Z.
"""

def accum(s):
    out=[]
    for i in range(0,len(s)):
        thisStr=s[i].upper()+s[i].lower()*(i)
        out.append(thisStr)
    return '-'.join(out)