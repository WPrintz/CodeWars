'''
Even or Odd
https://www.codewars.com/kata/53da3dbb4a5168369a0000fe
Solved 01/24/2017

Description:  8 kyu

Create a function that takes an integer as an argument and returns "Even" for even numbers or "Odd" for odd numbers.
'''


def even_or_odd(number):
    test = number % 2

    if test == 0:
        return ("Even")

    if test != 0:
        return ("Odd")