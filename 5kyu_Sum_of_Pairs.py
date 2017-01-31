"""
Sum of Pairs
https://www.codewars.com/kata/sum-of-pairs
Solved 01-31-2017

Description: 5 kyu

Sum of Pairs

Given a list of integers and a single sum value, return the first two values (parse from the left please) in order of appearance that add up to form the sum.

sum_pairs([11, 3, 7, 5],         10)
#              ^--^      3 + 7 = 10
== [3, 7]

sum_pairs([4, 3, 2, 3, 4],         6)
#          ^-----^         4 + 2 = 6, indices: 0, 2 *
#             ^-----^      3 + 3 = 6, indices: 1, 3
#                ^-----^   2 + 4 = 6, indices: 2, 4
#  * entire pair is earlier, and therefore is the correct answer
== [4, 2]

sum_pairs([0, 0, -2, 3], 2)
#  there are no pairs of values that can be added to produce 2.
== None/nil/undefined (Based on the language)

sum_pairs([10, 5, 2, 3, 7, 5],         10)
#              ^-----------^   5 + 5 = 10, indices: 1, 5
#                    ^--^      3 + 7 = 10, indices: 3, 4 *
#  * entire pair is earlier, and therefore is the correct answer
== [3, 7]
Negative numbers and duplicate numbers can and will appear.

NOTE: There will also be lists tested of lengths upwards of 10,000,000 elements. Be sure your code doesn't time out.
"""

import itertools
def sum_pairs(ints, s):
    uniquekeys = list(set(ints))
    sums = [pair for pair in list(itertools.product(uniquekeys, repeat=2)) if sum(pair) == s]

    best_pair = []
    best_ind = (0, len(ints))
    for i,key in enumerate(sums):
        try:
            first = ints.index(key[0])
            second = ints.index(key[1], first+1)
            if second < best_ind[1]:
                best_ind = (first, second)
                best_pair = [ints[first], ints[second]]
        except ValueError or IndexError:
            pass
    if len(best_pair) == 0:
        return None
    else:
        return best_pair

# ("Testing For Sum of Pairs")
l1= [1, 4, 8, 7, 3, 15]
l2= [1, -2, 3, 0, -6, 1]
l3= [20, -13, 40]
l4= [1, 2, 3, 4, 1, 0]
l5= [10, 5, 2, 3, 7, 5]
l6= [4, -2, 3, 3, 4]
l7= [0, 2, 0]
l8= [5, 9, 13, -3]
l9= [0]*10**7 ; l9[-1] = 3 ; l9[-2] = 5


# print(sum_pairs(l1, 8) == [1, 7]) #, "Basic: %s should return [1, 7] for sum = 8" % l1)
# print(sum_pairs(l2, -6) == [0, -6]) #, "Negatives: %s should return [0, -6] for sum = -6" % l2)
# print(sum_pairs(l3, -7) == None) #, "No Match: %s should return None for sum = -7" % l3)
# print(sum_pairs(l4, 2) == [1, 1]) #, "First Match From Left: %s should return [1, 1] for sum = 2 " % l4)
# print(sum_pairs(l5, 10) == [3, 7]) #, "First Match From Left REDUX!: %s should return [3, 7] for sum = 10 " % l5)
# print(sum_pairs(l6, 8) == [4, 4]) #, "Duplicates: %s should return [4, 4] for sum = 8" % l6)
# print(sum_pairs(l7, 0) == [0, 0]) #, "Zeroes: %s should return [0, 0] for sum = 0" % l7)
# print(sum_pairs(l8, 10) == [13, -3]) #, "Subtraction: %s should return [13, -3] for sum = 10" % l8)
print(sum_pairs(l9, 8) == [1, 1]) #, "Long array: %s should return [13, -3] for sum = 10" % l8)