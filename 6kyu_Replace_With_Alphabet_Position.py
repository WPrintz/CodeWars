"""
Bits Battle
https://www.codewars.com/kata/546f922b54af40e1e90001da
Solved 01-24-2017

Description: 6 kyu

Welcome. In this kata you are required to, given a string, replace every letter with its position in the alphabet. If anything in the text isn't a letter, ignore it and don't return it. a being 1, b being 2, etc. As an example:

alphabet_position("The sunset sets at twelve o' clock.")
Should return "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11" (As a string.)
"""

def alphabet_position(text):
    lcase='abcdefghijklmnopqrstuvwxyz'
    ucase=lcase.upper()
    out=[]
    for i in range(0,len(text)):
        if text[i] in lcase:
            out.append(str(lcase.index(text[i])+1))
        elif text[i] in ucase:
            out.append(str(ucase.index(text[i]) + 1))
        else:
            pass
    return ' '.join(out)