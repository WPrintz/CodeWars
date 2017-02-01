"""
Tic-Tac-Toe Checker
https://www.codewars.com/kata/tic-tac-toe-checker/python
Solved 02-01-2017

If we were to set up a Tic-Tac-Toe game, we would want to know whether the board's current state is solved, wouldn't we? Our goal is to create a function that will check that for us!

Assume that the board comes in the form of a 3x3 array, where the value is 0 if a spot is empty, 1 if it is an X, or 2 if it is an O, like so:

[[0,0,1],
 [0,1,2],
 [2,1,0]]
We want our function to return -1 if the board is not solved yet, 1 if X won, 2 if O won, or 0 if it's a cat's game (i.e. a draw).

You may assume that the board passed in is valid in the context of a game of Tic-Tac-Toe.
"""

def isSolved(board):
    #Strategy : replace O = 2 with O = 4.  Sum across winning triplets, if sum = 3 = X win, if sum = 12 = O win,
    # else if 0 is present = unfinished, and if all filled but no winning = cats game.

    if type(board[0][0]) is str:
        temp_board = [eval(elem) for elem in board[0]]
        mod_board = [[elem if elem is not 2 else 4 for elem in row] for row in temp_board]
    else:
        mod_board = [[elem if elem is not 2 else 4 for elem in row] for row in board]

    h_sum = [sum(row) for row in mod_board]
    diag1_sum = [sum([mod_board[i][i] for i in range(3)])]
    diag2_sum = [sum([mod_board[i][-i+2] for i in range(3)])]
    mod_board_T = list(map(list, zip(*mod_board)))
    v_sum = [sum(row) for row in mod_board_T]
    all_sums = h_sum + v_sum + diag1_sum + diag2_sum
    if 3 in all_sums:
        return 1
    elif 12 in all_sums:
        return 2
    elif 0 in mod_board[0] or 0 in mod_board[1] or 0 in mod_board[2]:
        return -1
    else:
        return 0




  # You can use test.expect(boolean, [optional] string) to test your code
print(isSolved([[0, 0, 1], [0, 1, 2], [2, 1, 0]]) is -1)    #Test no winner
print(isSolved([[1, 1, 1], [0, 1, 2], [2, 0, 0]]) is 1)     #Test horiz win X
print(isSolved([[0, 0, 1], [2, 2, 2], [2, 1, 0]]) is 2)     #Test horiz win O
print(isSolved([[1, 0, 1], [0, 1, 2], [2, 1, 1]]) is 1)     #Test diag win X
print(isSolved([[0, 0, 2], [0, 1, 2], [2, 1, 2]]) is 2)     #Test vert win O
print(isSolved([['[1,2,1]', '[1,1,2]', '[2,1,2]']]) is 0)     #Test string entry & is cats game


