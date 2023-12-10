import os
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(parent_dir)
from inputs.get_input import get_input

day = 4


def solve():
    input = get_input(day)
    output = 0
    
    for line in input:
        card = line.split(': ')
        numbers = card[1].split(' | ')

        winning = numbers[0].split(' ')
        mynumbers = numbers[1].split(' ')

        points = 0

        for number in mynumbers:
            if number != '':
                if number in winning:
                    if points == 0:
                        points = 1
                    else:
                        points = points * 2

        output += points        

    print(f"Solution for day {day}: \n\n{output}")



solve()
