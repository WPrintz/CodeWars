'''
Conways game of life on a toroidal array
https://www.codewars.com/kata/conways-game-of-life-on-a-toroidal-array/
Solved 08-02-2017

Description: 5 kyu


Conways game of life (https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life) is usually implemented without considering neigbouring cells that would be outside of the arrays range, but another way to do it is by considering the left and right edges of the array to be stitched together, and the top and bottom edges also, yielding a toroidal array and thus all cells get 8 neighbours.

Implement the function get_generation(cells, n) which takes a 2d-array cells an returns generation 'n' of game of life with the initial 'cells' and which considers the array as a toroidal array.

you can use the function print2dArr(list) to print out your array in a more readable format.

Example:

The following pattern would be considered Still life (a pattern which does not change after a generation) on a toroidal array because each live element have exactly 3 neighbours at the toroids stiched edges.

[   1,   0,   0,   1]
[   0,   0,   0,   0]
[   0,   0,   0,   0]
[   1,   0,   0,   1]


Rules:
Every cell interacts with its eight neighbours, which are the cells that are horizontally, vertically, or diagonally adjacent. At each step in time, the following transitions occur:
1. Any live cell with fewer than two live neighbours dies, as if caused by underpopulation.
2. Any live cell with two or three live neighbours lives on to the next generation.
3. Any live cell with more than three live neighbours dies, as if by overpopulation.
4. Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.

'''



def print2dArr(cells):
    for row in cells:
        print row

import numpy as np

def neighbor_generator(x, y, n):
    for i in [-1,0,1]:
        for j in [-1,0,1]:
            if (j == 0) and (i == 0):   # Don't include the cell as neighbor of itself
                pass
            else:
                if x+i < 0:             # Wrap left side
                    xnew = n[0]-1
                elif x+i > n[0]-1:      # Wrap right side
                    xnew = 0
                else:
                    xnew = x+i

                if y+j < 0:             # Wrap left side
                    ynew = n[1]-1
                elif y+j > n[1]-1:      # Wrap right side
                    ynew = 0
                else:
                    ynew = y+j

                yield (xnew, ynew)


def get_generation(cells, generation):

    print "Original cells: "
    print2dArr(cells)

    npcells = np.array(cells)
    lastindex = npcells.shape

    for gen in xrange(generation):
        flip_dead = []
        flip_live = []

        # Loop through all the cells in the matrix, sum the neighbors and flip state of those that meet criteria
        for i in xrange(lastindex[0]):
            for j in xrange(lastindex[1]):

                sum_neighbors = 0
                neighbor = neighbor_generator(i, j, lastindex)  # Generate neighbors

                for _ in xrange(8):
                    sum_neighbors += npcells[next(neighbor)]    # Total number of live neighbors

                if (npcells[i, j] == 1) and (sum_neighbors not in [2, 3]):  # Rule 1 & 3
                    flip_dead.append((i, j))

                if ((npcells[i, j] == 1) and (sum_neighbors in [2, 3])) \
                        or ((npcells[i, j] == 0) and (sum_neighbors == 3)):  # Rule 2 & 4
                    flip_live.append((i, j))

        # Flip state of those cells that need it
        for ind in flip_dead:
            npcells[ind] = 0
        for ind in flip_live:
            npcells[ind] = 1

        # Show end state of each generation
        print "Generation : {}".format(gen+1)
        print npcells
        print

    return npcells.tolist()


'''
******* Test code below *******
'''

test1 = [[1, 0, 0, 1], [0, 0, 0, 0], [0, 0, 0, 0], [1, 0, 0, 1]]
expected5gen = [[1,   0,   0,   1],
             [0,   0,   0,   0],
             [0,   0,   0,   0],
             [1,   0,   0,   1]]

test1output = get_generation(test1, 5)
print "Test 1 : {}".format(test1output == expected5gen)


test2 = [[0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 1, 0], [0, 1, 1, 1, 0], [0, 0, 0, 0, 0]]
expected12gen = [[0,   1,   0,   0,   0],
             [1,   1,   0,   0,   1],
             [0,   0,   0,   0,   0],
             [0,   0,   0,   0,   0],
             [1,   0,   0,   0,   0]]

test2output =  get_generation(test2, 12)
print "Test 2 : {}".format(test2output == expected12gen)
