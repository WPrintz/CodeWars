'''
Directions Reduction
https://www.codewars.com/kata/directions-reduction/
Solved 07-31-2017

Description: 5 kyu


Task

Write a function dirReduc which will take an array of strings and returns an array of strings with the needless directions removed (W<->E or S<->N side by side).

The Haskell version takes a list of directions with data Direction = North | East | West | South. The Clojure version returns nil when the path is reduced to nothing. The Rust version takes a slice of enum Direction {NORTH, SOUTH, EAST, WEST}.

Examples

dirReduc(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]) => ["WEST"]
dirReduc(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH"]) => []


'''

def dirReduc(arr):
    # Pairs of directions to check
    NS_pair = {"NORTH", "SOUTH"}
    EW_pair = {"EAST", "WEST"}

    stop_flag = False
    while stop_flag == False:
        reduc_lst = []        # Reset list of pairs of indexes to reduce

        # Work backwards through the list, looking for pairs.
        # This makes it easier to pop the pairs without messing up the index list.
        for i in reversed(xrange(len(arr)-1)):
            if arr[i] != arr[i+1]:
                if (arr[i] in NS_pair and arr[i+1] in NS_pair) \
                        or (arr[i] in EW_pair and arr[i+1] in EW_pair):
                    reduc_lst.append((i+1, i))

        if not reduc_lst:        #If the list of pairs is empty, we're done
            stop_flag = True
        else:
            for pair in reduc_lst:
                # check that the last pop didn't leave a pair index larger than the list
                  if max(pair) <= len(arr)-1:
                    arr.pop(pair[0])
                    arr.pop(pair[1])

    return arr


# a = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]
# print dirReduc(a)

# print
# b = ["EAST", "NORTH", "SOUTH", "WEST", "WEST", "NORTH", "WEST"]
# print dirReduc(b)
#
# print
c = ['NORTH', 'SOUTH', 'EAST', 'WEST', 'NORTH', 'NORTH', 'SOUTH', 'NORTH', 'WEST', 'EAST']
print dirReduc(c)
