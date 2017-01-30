'''
Bits Battle
https://www.codewars.com/kata/546e2562b03326a88e000020
Solved 01-24-2017

Description: 7 kyu

Welcome. In this kata, you are asked to square every digit of a number.

For example, if we run 9119 through the function, 811181 will come out.

Note: The function accepts an integer and returns an integer
'''

def square_digits(num):
    NumStr = str(num)
    OutStr = ''
    for i in NumStr:
        OutStr += str(int(i)**2)
    return int(OutStr)