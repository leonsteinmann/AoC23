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
    

    print(f"Solution for day {day}: \n\n{output}")



solve()
