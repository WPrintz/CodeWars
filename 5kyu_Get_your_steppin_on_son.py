'''
Get your steppin' on son
https://www.codewars.com/kata/get-your-steppin-on-son/
Solved

Description: 5 kyu

Write function wordStep(str)
that takes in a string and creates a step with that word.

E.g

wordStep('SNAKES SHOE EFFORT TRUMP POTATO') ===

[['S','N','A','K','E','S',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
 [' ',' ',' ',' ',' ','H',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
 [' ',' ',' ',' ',' ','O',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
 [' ',' ',' ',' ',' ','E','F','F','O','R','T',' ',' ',' ',' ',' '],
 [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','R',' ',' ',' ',' ',' '],
 [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','U',' ',' ',' ',' ',' '],
 [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','M',' ',' ',' ',' ',' '],
 [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','P','O','T','A','T','O']]

Every word will end with the character that the next word will start with.
You will start top left of the array and end bottom right.
All cells that are not occupied by a letter needs to be a space ' '


'''

def word_step(s):

    output = []
    cols = 0
    rows = 0

    words = s.split()

    ''' Determine size of final matrix '''
    for i, word in enumerate(words):
        if i%2 == 0:
            cols += len(word) - 1
        else:
            if i > 1:
                rows += len(word) - 1
            else:
                rows += len(word)

    ''' Convert '' to ' ' (with space) '''
    f = lambda x: ' ' if not x else None


    '''  Initialize empty matrix of spaces  '''
    for i in xrange(rows):
        output.append(map(f, ('_'*(cols)).split('_')))

    ''' Place even words horizontally, and odd words vertically  '''
    col_count = 0
    row_count = 0
    for i, word in enumerate(words):
        for j, letter in enumerate(word):
            if i%2 == 0:
                output[row_count][j+col_count] = letter
            else:
                output[row_count][col_count] = letter
                row_count += 1
        if i%2 == 0:
            col_count += j
        else:
            row_count -= 1

    return output




'''
******* Test code below *******
'''


test1out = word_step('HELLO OIL')
print "Test 1 : {}".format(test1out == [['H','E','L','L','O'],[' ',' ',' ',' ','I'],[' ',' ',' ',' ','L']])


test2out = word_step('SNAKES SHOE EFFORT TRUMP POTATO')
print "Test 2 : {}".format(test2out == [['S', 'N', 'A', 'K', 'E', 'S', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', 'H', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', 'O', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', 'E', 'F', 'F', 'O', 'R', 'T', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'R', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'U', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'M', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'P', 'O', 'T', 'A', 'T', 'O']])

test3out = word_step('CODEWARS SNAIL LAKE EEK')
print "Test 3 : {}".format(test3out == [['C', 'O', 'D', 'E', 'W', 'A', 'R', 'S', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', 'N', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', 'A', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', 'I', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', 'L', 'A', 'K', 'E'], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'E'], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'K']])

