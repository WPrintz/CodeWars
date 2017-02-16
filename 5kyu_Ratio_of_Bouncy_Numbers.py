"""
Ratio of Bouncy Numbers
https://www.codewars.com/kata/ratio-of-bouncy-numbers/
Solved 02-15-2017

Description: 5 kyu

Working from left-to-right if no digit is exceeded by the digit to its left it is called an increasing number; for example, 134468.

Similarly if no digit is exceeded by the digit to its right it is called a decreasing number; for example, 66420.

We shall call a positive integer that is neither increasing nor decreasing a "bouncy" number; for example, 155349.

Clearly there cannot be any bouncy numbers below one-hundred, but just over half of the numbers below one-thousand (525) are bouncy. In fact, the least number for which the proportion of bouncy numbers first reaches 50% is 538.

Surprisingly, bouncy numbers become more and more common and by the time we reach 21780 the proportion of bouncy numbers is equal to 90%.

Your Task

Complete the bouncyRatio function.

The input will be the target ratio.

The output should be the smallest number such that the proportion of bouncy numbers reaches the target ratio.

You should throw an Error for a ratio less than 0% or greater than 99%.

Source

https://projecteuler.net/problem=112
"""




def b_eval(val):
    str_num = str(val)
    str_eval = [0, 0]
    for n in range(1, len(str_num)):
        if str_num[n] > str_num[n-1]:
            str_eval[0] = 1
        elif str_num[n] < str_num[n - 1]:
            str_eval[1] = 1
        else:
            pass

        if sum(str_eval) > 1:
            return True
    return False


def bouncy_ratio(percent):
    i = 0
    bouncies = 0
    while True:
        i += 1
        if b_eval(i) == True:
            bouncies += 1

        if float(bouncies) / i >= percent:
            return i





print(bouncy_ratio(.9))

"""
Test.describe("Example Test Cases")
Test.assert_equals(bouncy_ratio(0.1), 132, 'A 10% bouncy ratio should be reached by 132')
Test.assert_equals(bouncy_ratio(0.15), 160, 'A 15% bouncy ratio should be reached by 160')
Test.assert_equals(bouncy_ratio(0.5), 538, 'A 50% bouncy ratio should be reached by 538')
Test.assert_equals(bouncy_ratio(0.75), 3088, 'A 10% bouncy ratio should be reached by 3088')
Test.assert_equals(bouncy_ratio(0.9), 21780, 'A 90% bouncy ratio should be reached by 21780')
"""