'''
Memoized Log Cutting
https://www.codewars.com/kata/memoized-log-cutting
Solved 08-04-2017

Description: 4 kyu

CLEAR CUTTER'S NEEDS YOUR HELP!

The logging company Clear Cutter's makes its money by optimizing the price-to-length of each log they cut before selling them. An example of one of their price tables is included:

# So a price table p
p = [ 0,  1,  5,  8,  9, 10]

# Can be imagined as:
# length i | 0  1  2  3  4  5 *in feet*
# price pi | 0  1  5  8  9 10 *in money*
They hired an intern last summer to create a recursive function for them to easily calculate the most profitable price for a log of length n using price table p as follows:

def cut_log(p, n):
   if (n == 0):
      return 0
   q = -1
   for i in range(1, n+1)
      q = max(q, p[i] + cut_log(p, n-i))
   return q
An example of the working code:

cut_log(p, 5) # => 13
# 5ft = $10, BUT 2ft + 3ft = 5ft -> $5 + $8 = $13 which is greater in value
However, their senior software engineer realized that the number of recursive calls in the function gives it an awful running time of 2^n (as this function iterates through ALL 2^n-1 possibilities for a log of length n).

Having discovered this problem just as you've arrived for your internship, he responsibly delegates the issue to you.

Using the power of Stack Overflow and Google, he wants you to create a solution that runs in theta(n^2) time so that it doesn't take 5 hours to calculate the optimal price for a log of size 50. (He also suggests to research the problem using the keywords in the tags)

(Be aware that if your algorithm is not efficient, it will attempt to look at 2^49 = 562949953421312 nodes instead of 49^2 = 2401... The solution will automatically fail if it takes longer than 6 seconds... which occurs at right around Log 23)

'''


prices = dict()

def cut_log(p, n):
    if (n == 0):
        return 0

    for j in xrange(len(p)):
        prices[j] = p[j]

    for j in xrange(0, n+1):
        for i in xrange(0, n-j+1): # Two nested loops = theta(n^2)
            small_board = i+j
            if prices[small_board] < (p[i] + prices[j]):
                prices[small_board] = p[i] + prices[j]

    return prices[n]




#      0    1    2    3    4    5    6    7... and so on
p = [  0,   1,   5,   8,   9,  10,  17,  17,  20,  24, # 0X's
      30,  32,  35,  39,  43,  43,  45,  49,  50,  54, # 1X's
      57,  60,  65,  68,  70,  74,  80,  81,  84,  85, # 2X's
      87,  91,  95,  99, 101, 104, 107, 112, 115, 116, # 3X's
     119] # 40th element



'''
******* Test code below *******
'''


print "The optimal price for n = 1 should be $1", cut_log(p, 1) == 1

print "The optimal price for n = 5 should be $13", cut_log(p, 5) == 13

print  "The optimal price for n = 8 should be $22", cut_log(p, 8) == 22

print  "The optimal price for n = 10 should be $30", cut_log(p, 10)== 30

print  "The optimal price for n = 22 should be $65", cut_log(p, 22) == 65

# Uncomment this when you think your function can handle it
print "The optimal price for n = 35 should be $105", cut_log(p, 35) == 105


