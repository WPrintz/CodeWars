"""
Land perimeter
https://www.codewars.com/kata/5839c48f0cf94640a20001d3
Solved 01-30-2017

Description: 5 kyu

Task:

Given an array arr of strings complete the function landPerimeter by calculating the total perimeter of all the islands. Each piece of land will be marked with 'X' while the water fields are represented as 'O'. Consider each tile being a perfect 1 x 1piece of land. Some examples for better visulatization:

['XOOXO',
 'XOOXO',
 'OOOXO',
 'XXOXO',
 'OXOOO']
or


should return: "Total land perimeter: 24",
while


['XOOO',
 'XOXO',
 'XOXO',
 'OOXX',
 'OOOO']


should return: "Total land perimeter: 18"
"""

def land_perimeter(arr):
    output = [list(row) for row in arr]
    p_dict = {5:0, 4:1, 3:2, 2:3, 1:4}
    perimeter = 0
    for i,row in enumerate(arr):
        for j,char in enumerate(row):
            if arr[i][j] == 'X':
                count = 1
                if (j-1) >= 0 and arr[i][j-1] == 'X':
                    count += 1
                if (j+1) < len(row) and arr[i][j+1] == 'X':
                    count += 1
                if (i-1) >= 0 and arr[i-1][j] == 'X':
                    count += 1
                if (i+1) < len(arr) and arr[i+1][j] == 'X':
                    count += 1
                output[i][j] = [count]
                perimeter += p_dict[count]
            else:
                output[i][j] = [0]
    return "Total land perimeter: {}".format(perimeter)


#Test Cases Below
print(land_perimeter(["OXOOOX", "OXOXOO", "XXOOOX", "OXXXOO", "OOXOOX", "OXOOOO", "OOXOOX", "OOXOOO", "OXOOOO", "OXOOXX"]))# == "Total land perimeter: 60")
print(land_perimeter(["OXOOO", "OOXXX", "OXXOO", "XOOOO", "XOOOO", "XXXOO", "XOXOO", "OOOXO", "OXOOX", "XOOOO", "OOOXO"]) == "Total land perimeter: 52")
print(land_perimeter(["XXXXXOOO", "OOXOOOOO", "OOOOOOXO", "XXXOOOXO", "OXOXXOOX"]) == "Total land perimeter: 40")
print(land_perimeter(["XOOOXOO", "OXOOOOO", "XOXOXOO", "OXOXXOO", "OOOOOXX", "OOOXOXX", "XXXXOXO"]) == "Total land perimeter: 54")
print(land_perimeter(["OOOOXO", "XOXOOX", "XXOXOX", "XOXOOO", "OOOOOO", "OOOXOO", "OOXXOO"]) == "Total land perimeter: 40")