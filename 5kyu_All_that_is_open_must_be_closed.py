"""



Your challenge in this kata is to write a piece of code to validate that a supplied string is balanced.

You must determine if all that is open is then closed, and nothing is closed which is not already open!

You will be given a string to validate, and a second string, where each pair of characters defines an opening and closing sequence that needs balancing.

You may assume that the second string always has an even number of characters.

Example

# In this case '(' opens a section, and ')' closes a section
is_balanced("(Sensei says yes!)", "()")       # => True
is_balanced("(Sensei says no!", "()")         # => False

# In this case '(' and '[' open a section, while ')' and ']' close a section
is_balanced("(Sensei [says] yes!)", "()[]")   # => True
is_balanced("(Sensei [says) no!]", "()[]")    # => False

# In this case a single quote (') both opens and closes a section
is_balanced("Sensei says 'yes'!", "''")       # => True
is_balanced("Sensei say's no!", "''")         # => False
"""

def is_balanced(source, caps):
    # Strategy: 1. Create dictionary of matched brackets.  2. Create index of all brackets.  3. Loop through sequence of
    #     pairs of brackets and if matching pair found, pop off the pair from the list of brackets.  4. Recurse until no
    #     remaining pairs.  If no pairs left, then return True, else False.

    brack_pair={}
    for i in range(len(caps)):
        if i%2 == 0:
            brack_pair[caps[i]]='.'
        else:
            brack_pair[caps[i-1]]=caps[i]

    brack_list = [i for i in range(len(source)) if (source[i] in brack_pair.keys() or source[i] in brack_pair.values())]

    if len(brack_list)%2 is not 0:
        return False

    max_tries = len(brack_list)
    tries = 0
    while len(brack_list)>0 and tries <= max_tries:
        for i,key in enumerate(brack_list[:-1]):
            # print('Try:', source[brack_list[i]], source[brack_list[i + 1]])
            if source[key] in brack_pair.keys() and brack_pair[source[key]] == source[brack_list[i+1]]:
                # print('match')
                brack_list.pop(i + 1)
                brack_list.pop(i)
                break
        tries += 1

    if len(brack_list) == 0:
        return True
    else:
        return False


print(is_balanced("(Sensei says yes!)", "()") == True)
print(is_balanced("(Sensei says no!", "()") == False)

print(is_balanced("(Sensei ([says]) yes!)", "()[]") == True)
print(is_balanced("(Sensei [says) no!]", "()[]") == False)
#
print(is_balanced("Sensei says -yes-!", "--") == True)
print(is_balanced("Sensei -says no!", "--") == False)
print(is_balanced("(Sensei ([says]) [yes!])", "()[]") == True)
print(is_balanced("(Hello Mother can you hear me?)[Monkeys, in my pockets!!]", "()[]") == True)