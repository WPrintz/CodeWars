'''
Sum of two lowest positive integers
https://www.codewars.com/kata/558fc85d8fd1938afb000014
Solved 01-24-2017

Description: 7 kyu

Create a function that returns the sum of the two lowest positive numbers given an array of minimum 4 integers. No floats or empty arrays will be passed.

For example, when an array is passed like [19,5,42,2,77], the output should be 7.

[10,343445353,3453445,3453545353453] should return 3453455.

Hint: Do not modify the original array.

'''

def sum_two_smallest_numbers(numbers):
    numbers.sort()
    return numbers[0]+numbers[1]