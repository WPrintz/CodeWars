"""
Multiples of 3 and 5
https://www.codewars.com/kata/514b92a657cdc65150000006
Solved 01-26-2017

Description: 6 kyu

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in.

Note: If the number is a multiple of both 3 and 5, only count it once.
Courtesy of ProjectEuler.net
"""

def solution(number):
    multiples = []
    for x in range(number-1,2,-1):
        if x % 3 == 0 or x % 5 == 0:
            print(x)
            multiples.append(x)

    return sum(multiples)