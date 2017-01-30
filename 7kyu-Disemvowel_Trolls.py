"""
Disemvowel Trolls
https://www.codewars.com/kata/52fba66badcd10859f00097e
Solved 01-24-2017

Description: 7 kyu

Trolls are attacking your comment section!

A common way to deal with this situation is to remove all of the vowels from the trolls' comments, neutralizing the threat.

Your task is to write a function that takes a string and return a new string with all vowels removed.

For example, the string "This website is for losers LOL!" would become "Ths wbst s fr lsrs LL!".
"""

def disemvowel(string):
    vowels = "aAeEiIoOuU"
    count = 0
    tempList=list(string)
    out=[]

    for i in range(0,len(string)):
        if tempList[i] not in vowels:
            out += tempList[i]
            count += 1

    return ''.join(out)