import os
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(parent_dir)
from inputs.get_input import get_input

day = 1


def solve():
    input = get_input(day)
    output = 0
    
    for line in input:
        left = 0
        right = 0
        for i in range(len(line)):
            if line[i].isdigit():
                left = int(line[i])
                break
        for j in range(len(line)):
            if line[-j-1].isdigit():
                right = int(line[-j-1])
                break
        # print(f'{line} left: {left} right: {right}')
        numberToAdd = left * 10 + right
        output += numberToAdd 

    

    print(f"Solution for day {day}: \n\n{output}")



solve()
