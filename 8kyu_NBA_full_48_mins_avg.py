"""
NBA full 48 minutes average
https://www.codewars.com/kata/587c2d08bb65b5e8040004fd
Solved 01-26-2017

Description: 6 kyu

An NBA game runs 48 minutes (Four 12 minute quarters). Players do not typically play the full game, subbing in and out as necessary. Your job is to extrapolate a player's points per game if they played the full 48 minutes.

Write a function that takes two arguments, ppg (points per game) and mpg (minutes per game) and returns a straight extrapolation of ppg per 48 minutes rounded to the nearest tenth.

Examples:

nba_extrap(12, 20) #=> 28.8
nba_extrap(10, 10) #=> 48
nba_extrap(5, 17) #=> 14.1
nba_extrap(0, 0) #=> 0
Notes:
All inputs will be either be an integer or float.
Follow your dreams!
"""


def nba_extrap(ppg, mpg):
    if mpg == 0:
        return 0
    else:
        return round((float(ppg) / mpg) * 48, 1)